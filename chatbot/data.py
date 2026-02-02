import pandas as pd
import sqlite3
import os

def create_integrated_db():
    base_path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_path, "nutrition.db")
    
    # 1. 고정할 영양소 매핑 (FastAPI와 100% 일치)
    column_mapping = {
        '식품코드': 'food_code', '식품명': 'food_name', '제조사명': 'brand',
        '에너지(kcal)': 'kcal', '탄수화물(g)': 'carbs', '단백질(g)': 'protein',
        '지방(g)': 'fat', '당류(g)': 'sugar', '나트륨(mg)': 'sodium',
        '칼슘(mg)': 'calcium', '철(mg)': 'iron', '마그네슘(mg)': 'magnesium',
        '인(mg)': 'phosphorus', '칼륨(mg)': 'potassium', '아연(mg)': 'zinc',
        '비타민 A(μg RAE)': 'vit_a', '비타민 C(mg)': 'vit_c', '비타민 D(μg)': 'vit_d',
        '비타민 E(mg α-TE)': 'vit_e', '티아민(mg)': 'vit_b1', '리보플라빈(mg)': 'vit_b2',
        '비타민 B6 / 피리독신(mg)': 'vit_b6', '비타민 B12(μg)': 'vit_b12', '엽산(μg DFE)': 'folate'
    }

    files_info = [
        {'file': '음식DB.xlsx', 'cat': '일반'},
        {'file': '가공식품DB.xlsx', 'cat': '가공'},
        {'file': '건강기능식품DB.xlsx', 'cat': '건기식'}
    ]

    # DB 연결 (기존 파일이 있다면 연결 후 replace 방식으로 테이블 초기화)
    conn = sqlite3.connect(db_path)
    total_count = 0

    for info in files_info:
        file_name = info['file']
        category = info['cat']
        full_file_path = os.path.join(base_path, file_name)

        if not os.path.exists(full_file_path):
            print(f"⏩ 건너뜀: {file_name} 파일이 없습니다.")
            continue

        try:
            print(f"🔄 {category} 데이터 처리 중: {file_name}...")
            df = pd.read_excel(full_file_path)
            
            # [핵심] 모든 영문 컬럼을 미리 포함한 DataFrame 생성
            df_sub = pd.DataFrame(index=df.index)
            
            for kor, eng in column_mapping.items():
                if kor in df.columns:
                    # 데이터가 있으면 넣고, 숫자로 변환
                    df_sub[eng] = pd.to_numeric(df[kor], errors='coerce').fillna(0)
                else:
                    # 엑셀에 컬럼이 아예 없으면 0으로 생성
                    df_sub[eng] = 0.0
            
            # 카테고리 추가
            df_sub['category'] = category
            if 'brand' not in df_sub.columns or df_sub['brand'].iloc[0] == 0:
                df_sub['brand'] = 'N/A'

            # DB 저장
            mode = 'replace' if total_count == 0 else 'append'
            df_sub.to_sql('food_master', conn, if_exists=mode, index=False)
            
            total_count += len(df_sub)
            print(f"✅ {category} 완료: {len(df_sub)}행 적재됨.")

        except Exception as e:
            print(f"❌ {category} 처리 중 오류 발생: {e}")

    if total_count > 0:
        conn.execute("CREATE INDEX IF NOT EXISTS idx_food_name ON food_master(food_name)")
        print(f"\n✨ 모든 작업 완료! 총 {total_count}개의 데이터가 '{db_path}'에 저장되었습니다.")
    
    conn.close()

if __name__ == "__main__":
    create_integrated_db()