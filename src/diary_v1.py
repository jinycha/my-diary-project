
import pymysql

# --- 설정 시작 (본인 비밀번호로 수정하세요!) ---
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = '1191'       # <--- ⚠️ 여기에 설치할 때 정한 MariaDB 비밀번호 입력!!
DB_NAME = 'my_diary_db'
# ------------------------------------------

# 1. DB 연결
conn = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    db=DB_NAME,
    charset='utf8'
)
cur = conn.cursor()

# 2. 기능 함수 정의
def write_diary():
    print("\n📝 [일기 쓰기]")
    date = input("날짜(YYYY-MM-DD): ")
    weather = input("날씨: ")
    content = input("내용: ")
    
    # DB에 저장하는 주문서(SQL) 만들기
    sql = "INSERT INTO diary (date, weather, content) VALUES (%s, %s, %s)"
    cur.execute(sql, (date, weather, content))
    conn.commit()  # 도장 쾅! (저장 확정)
    print(">> ✅ 일기가 저장되었습니다!")

def read_diary():
    print("\n📖 [일기 목록]")
    sql = "SELECT * FROM diary ORDER BY date DESC"
    cur.execute(sql)
    rows = cur.fetchall()
    
    if not rows:
        print(">> 📭 저장된 일기가 하나도 없습니다.")
    else:
        for row in rows:
            # 수정된 부분: 맨 앞에 id(row[0])를 보여줍니다!
            # 예: [1] 2026-01-04 ...
            print(f"[{row[0]}] {row[1]} | 날씨:{row[2]} | {row[3]}")
            
def delete_diary():
    print("\n🗑 [일기 삭제]")
    # 먼저 목록을 보여줘야 무엇을 지울지 알 수 있습니다.
    read_diary() 
    
    target_id = input("\n>> 삭제할 일기 번호(id)를 입력하세요: ")
    
    # 정말 지울지 한번 확인 (안전장치)
    check = input(f"{target_id}번 일기를 정말 삭제할까요? (y/n): ")
    
    if check.lower() == 'y':
        sql = "DELETE FROM diary WHERE id = %s"
        cur.execute(sql, (target_id,))
        conn.commit() # 삭제도 '저장'을 해야 반영됩니다!
        print(f">> ✅ {target_id}번 일기가 삭제되었습니다.")
    else:
        print(">> 삭제를 취소했습니다.")

# 3. 메인 실행 루프
# (기존)
# print("3. 종료")
# ...
# elif choice == '3': ...

# (변경 후 - 이렇게 바꾸세요!)
while True:
    print("\n=== 📔 나의 비밀 일기장 v1 ===")
    print("1. 일기 쓰기")
    print("2. 일기 몰아보기")
    print("3. 일기 삭제")  # <--- 추가됨
    print("4. 종료")      # <--- 번호 밀림
    
    choice = input("선택: ")

    if choice == '1':
        write_diary()
    elif choice == '2':
        read_diary()
    elif choice == '3':     # <--- 추가됨
        delete_diary()
    elif choice == '4':     # <--- 3번에서 4번으로 변경
        print("일기장을 덮습니다. 안녕!")
        break
    else:
        print("잘못된 입력입니다.")

print("go")

conn.close()