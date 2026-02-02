import sqlite3

def create_index():
    conn = sqlite3.connect(r"C:\Users\admin\Desktop\New\Python_gyeong\chatbot\nutrition.db")
    cursor = conn.cursor()
    # food_name 컬럼에 인덱스 추가 (이미 있으면 무시됨)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_food_name ON food_master (food_name)")
    conn.commit()
    conn.close()
    print("⚡ 검색 최적화(인덱스 생성) 완료!")

create_index()