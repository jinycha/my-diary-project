from db_manager import DiaryDB

def print_menu():
    print("\n" + "="*30)
    print(" 📖 비밀 일기장 (v0.4 OOP)")
    print("="*30)
    print("1. 일기 쓰기")
    print("2. 일기 목록 보기")
    print("3. 일기 수정하기")
    print("4. 일기 삭제하기")
    print("0. 종료")
    print("="*30)

def main():
    db = DiaryDB()
    db.create_table()

    while True:
        print_menu()
        choice = input("선택 >> ")

        if choice == '0':
            print("일기장을 덮습니다.")
            db.close()
            break

        elif choice == '1':
            content = input("오늘의 내용: ")
            db.add_entry(content)
            print("저장되었습니다. ")

        elif choice == '2':
            rows = db.get_all_entries()
            print("\n[일기 목록]")
            for row in rows:
                print(f"[{row[0]}] {row[1]} : {row[2]}")
        
        elif choice == '3':
            target_id = input("수정할 번호: ")
            new_content = input("새 내용: ")
            if db.update_entry(target_id, new_content):
                print("수정 성공")
            else:
                print("수정 실패 (번호 확인 필요)")
        
        elif choice == '4':
            target_id = input("삭제할 번호: ")
            if input("진짜 지울까요? (y/n): ") == 'y':
                if db.delete_entry(target_id):
                    print("삭제 성공")
                else:
                    print("삭제 실패")

if __name__ == "__main__":
    main()