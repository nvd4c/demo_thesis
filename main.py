
import streamlit as st

st.title("Đồ án tốt nghiệp")
st.header("Phân tích cảm xúc  ")

def main():
    user_question = st.text_input("Nhập input:")
    if st.button("Phân tích"):
        response_text = x(user_question)
        return st.write(response_text)
main()

#streamlit run main.py