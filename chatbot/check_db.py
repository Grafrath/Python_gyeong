import sqlite3
import os

# main.py와 동일한 경로의 DB 연결
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "nutrition.db")

def insert_test_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. 테스트용 food_master 테이블 생성 (없을 경우를 대비)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS food_master (
            food_code TEXT PRIMARY KEY,
            food_name TEXT,
            category TEXT,
            brand TEXT,
            kcal REAL,
            carbs REAL,
            protein REAL,
            fat REAL,
            sugar REAL,
            sodium REAL,
            calcium REAL,
            iron REAL,
            magnesium REAL,
            phosphorus REAL,
            potassium REAL,
            zinc REAL,
            vit_a REAL,
            vit_c REAL,
            vit_d REAL,
            vit_e REAL,
            vit_b1 REAL,
            vit_b2 REAL,
            vit_b6 REAL,
            vit_b12 REAL,
            folate REAL
        )
    """)
    
    # 2. 샘플 데이터 삽입
    test_food = ('F001', '사과', '과일', '농협', 52, 14, 0.3, 0.2, 10, 1, 6, 0.1, 5, 11, 107, 0.04, 1, 4.6, 0, 0.18, 0.017, 0.026, 0.041, 0, 3)
    cursor.execute("INSERT OR REPLACE INTO food_master VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", test_food)
    
    conn.commit()
    conn.close()
    print("✅ 테스트 데이터(사과)가 삽입되었습니다.")

if __name__ == "__main__":
    insert_test_data()