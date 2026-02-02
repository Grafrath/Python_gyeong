from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import sqlite3
import os

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "nutrition.db")

# 1. init_db.py의 컬럼명과 100% 일치하도록 설정
RECOMMENDED_INTAKE = {
    "kcal": 2400, "carbs": 324, "protein": 65, "fat": 54, "sugar": 50,
    "sodium": 2000, "calcium": 700, "iron": 10, "magnesium": 350,
    "phosphorus": 700, "potassium": 3500, "zinc": 10, 
    "vit_a": 800, "vit_c": 100, "vit_d": 10, "vit_e": 11, 
    "vit_b1": 1.2, "vit_b2": 1.5, "vit_b6": 1.5, "vit_b12": 2.4, "folate": 400
}

EXCLUDE_FROM_RECOMMEND = ["sodium", "sugar", "fat"]
NUTRIENTS_LIST = list(RECOMMENDED_INTAKE.keys())

class MealLogRequest(BaseModel):
    food_code: str
    serving: float = 1.0

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# 2. 서버 시작 시 사용자 기록 테이블 초기화 및 생성
@app.on_event("startup")
def create_logs_table():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # 구조 불일치 에러 방지를 위해 기존 테이블 삭제 후 재생성
        cursor.execute("DROP TABLE IF EXISTS diet_logs") 
        
        nutrient_cols = ", ".join([f"{n} REAL DEFAULT 0" for n in NUTRIENTS_LIST])
        create_sql = f"""
            CREATE TABLE IF NOT EXISTS diet_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                food_code TEXT,
                food_name TEXT,
                eat_date TEXT,
                serving REAL,
                {nutrient_cols}
            )
        """
        cursor.execute(create_sql)
        conn.commit()
    print(f"✨ {len(NUTRIENTS_LIST)}개 영양소 구조로 diet_logs 테이블 준비 완료!")

# 3. 음식 검색 API
@app.get("/search")
def search_food(q: str = Query(..., min_length=1)):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM food_master WHERE food_name LIKE ? LIMIT 20", (f"%{q}%",))
        results = [dict(row) for row in cursor.fetchall()]
    return {"results": results}

# 4. 식단 기록 API
@app.post("/log/meal")
def log_meal(item: MealLogRequest):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM food_master WHERE food_code = ?", (item.food_code,))
        food = cursor.fetchone()
        
        if not food:
            raise HTTPException(status_code=404, detail="식품을 찾을 수 없습니다.")
        
        try:
            food_dict = dict(food)
            cols = ["user_id", "food_code", "food_name", "eat_date", "serving"] + NUTRIENTS_LIST
            
            # 영양소 값 계산 및 None 방어 로직
            nutrient_values = []
            for n in NUTRIENTS_LIST:
                val = food_dict.get(n, 0)
                if val is None: val = 0
                nutrient_values.append(val * item.serving)
            
            vals = [
                "test_user", 
                food_dict['food_code'], 
                food_dict['food_name'], 
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                item.serving
            ] + nutrient_values

            placeholders = ", ".join(["?"] * len(cols))
            cursor.execute(f"INSERT INTO diet_logs ({', '.join(cols)}) VALUES ({placeholders})", vals)
            conn.commit()
            return {"message": "✅ 식단이 기록되었습니다.", "log_id": cursor.lastrowid}
        except Exception as e:
            print(f"❌ 저장 에러: {e}")
            raise HTTPException(status_code=500, detail=str(e))

# 5. 영양 요약 및 분석 API
@app.get("/summary")
def get_daily_summary():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        today = datetime.now().strftime("%Y-%m-%d")
        
        try:
            # 21개 영양소 합계 조회
            select_clause = ", ".join([f"IFNULL(SUM({n}), 0) as {n}" for n in NUTRIENTS_LIST])
            cursor.execute(f"SELECT {select_clause} FROM diet_logs WHERE eat_date LIKE ?", (f"{today}%",))
            summary_row = cursor.fetchone()
            summary = dict(summary_row) if summary_row else {n: 0 for n in NUTRIENTS_LIST}

            # 달성률 계산 및 최저 영양소 도출
            rates = {}
            min_rate = 999.0
            deficit_nutrient = None

            for n in NUTRIENTS_LIST:
                current_val = summary[n]
                standard_val = RECOMMENDED_INTAKE[n]
                rate = (current_val / standard_val) * 100
                rates[n] = round(rate, 1)

                if n not in EXCLUDE_FROM_RECOMMEND and rate < min_rate:
                    min_rate = rate
                    deficit_nutrient = n

            # 보충 건기식 추천
            recommendations = []
            if deficit_nutrient and min_rate < 100:
                cursor.execute(f"""
                    SELECT food_name, brand, {deficit_nutrient} as value 
                    FROM food_master 
                    WHERE category = '건기식' AND {deficit_nutrient} > 0 
                    ORDER BY {deficit_nutrient} DESC LIMIT 3
                """)
                recommendations = [dict(r) for r in cursor.fetchall()]

            return {
                "summary": summary,
                "standards": RECOMMENDED_INTAKE,  # 프론트엔드 대시보드 필수 데이터
                "rates": rates,
                "recommendations": {
                    "nutrient": deficit_nutrient if min_rate < 100 else "모두 충족",
                    "items": recommendations,
                    "current_rate": round(min_rate, 1) if min_rate < 999 else 0
                }
            }
        except Exception as e:
            print(f"❌ 분석 에러: {e}")
            raise HTTPException(status_code=500, detail=str(e))