import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1191',
    db='my_diary_db',
    charset='utf8mb4'
)
curs = conn.cursor()

curs.execute("""
    CREATE TABLE IF NOT EXISTS entries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        content TEXT NOT NULL,
        created_at DATETIME DEFAULT NOW()
    )
""")
conn.commit() 

def print_menu():
    print("\n" + "="*30)
    print("📖 비밀 일기장(v0.2 Console)")
    print("="*30)
    print("1. 일기 쓰기(Create)")
    print("2. 일기 목록 보기 (Read)")
    print("3. 일기 수정하기(Update)")
    print("4. 일기 삭제하기 (Delete)")
    print("0. 종료")
    print("="*30)

while True:
    print_menu()
    choice = input("선택>> ")

    if choice == '0':
        print("일기장을 덮습니다.")
        break

    elif choice == '1':
        from datetime import date

        today = date.today()
        content = input("내용: ")
        sql = "INSERT INTO entries (date, content, created_at) VALUES (%s, %s, NOW())"
        curs.execute(sql,  (today, content))
        conn.commit()
        print("✅ 일기가 저장됐습니다.")
    
    elif choice == '2':
        sql = "SELECT id, date, content FROM entries ORDER BY date DESC"
        curs.execute(sql)
        rows = curs.fetchall()
        print("\n[일기 목록]")
        for row in rows:
            # row[0]: id, row[1]: date, row[2]: content
            print(f"[{row[0]}] {row[1]} : {row[2]}")
        
    elif choice == '3':
        target_id = input("수정할 일기 번호(ID)를 입력하세요: ")
        new_content = input("새로운 내용: ")

        sql = "UPDATE entries SET content = %s WHERE id = %s"
        curs.execute(sql, (new_content, target_id))
        conn.commit()

        if curs.rowcount > 0: 
            print("수정되었습니다.")
        else:
            print("해당 번호의 일기가 없습니다.")
        
    elif choice == '4':
        target_id = input("삭제할 일기 번호(ID)를 입력하세요:")
        confirm = input("정말 삭제하시겠습니까? (y/n): ")

        if confirm.lower() == 'y':
            sql = "DELETE FROM entries WHERE id = %s"
            curs.execute(sql, (target_id,))
            conn.commit()
            if curs.rowcount > 0:
                print("삭제되었습니다.")
            else:
                print("해당 번호의 일기가 없습니다.")
    
    else: 
        print("잘못된 입력입니다.")

conn.close()