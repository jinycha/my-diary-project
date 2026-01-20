import streamlit as st
from db_manager import DiaryDB

db = DiaryDB()
db.create_table()

st.sidebar.title("비밀 일기장")
menu = ["일기 쓰기", "일기 목록 보기", "일기 수정하기", "일기 삭제하기"]
choice = st.sidebar.selectbox("메뉴 선택", menu)

st.title(f"✨ {choice}")

if choice == "일기 쓰기":
    st.subheader("오늘의 내용을 기록하세요.")
    content = st.text_area("내용 입력", placeholder="여기에 일기를 작성하세요...", height=200)
    
    if st.button("저장하기"):
        if content.strip():
            db.add_entry(content)
            st.success("✅ 일기가 성공적으로 저장되었습니다.")
        else:
            st.warning("⚠️ 내용을 입력해주세요.")

elif choice == "일기 목록 보기":
    st.subheader("저장된 모든 기록입니다.")
    rows = db.get_all_entries()

    if not rows:
        st.info("작성된 일기가 없습니다.")
    else:
        for row in rows:
            with st.container():
                st.write(f"**번호: {row[0]}** | 🕒 {row[2]}")
                st.info(row[0])
                st.divider()

elif choice == "일기 수정하기":
    st.subheader("수정할 일기 번호와 새 내용을 입력하세요.")
    target_id = st.number_input("수정할 번호", min_value=1, step=1)
    new_content = st.text_area("새 내용 입력", height=150)

    if st.button("수정 완료"):
        if db.update_entry(target_id, new_content):
            st.success(f"{target_id}번 일기가 수정되었습니다.")
        else: 
            st.error("수정 실패 (번호를 확인하세요)")

elif choice == "일기 삭제하기":
    st.subheader("삭제할 일기 번호를 입력하세요.")
    delete_id = st.number_input("삭제할 번호", min_value=1, step=1)

    if st.button("삭제하기", type="primary"):
        st.success(f"{delete_id}번 일기가 삭제되었습니다.")
    else:
        st.error("해당 번호의 일기가 없습니다.")