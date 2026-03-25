import streamlit as st
from datetime import date

def form_mentee_agreement():
    st.markdown("### 서약서 내용")
    agree = st.checkbox("동의")
    name = st.text_input("성명")
    return {"동의": agree, "성명": name}

def form_mentee_info():
    return {"연락처": st.text_input("연락처")}

def form_lesson_plan_basic():
    return {"과목": st.text_input("과목")}

def form_first_class_plan():
    return {"첫수업": st.text_area("내용")}

def form_session_plan():
    n = st.selectbox("회차", list(range(1,9)))
    return {"회차": n, "내용": st.text_area("내용")}

def form_mentor_info():
    return {"멘토정보": st.text_area("내용")}

def form_mentor_report():
    return {"보고서": st.text_area("내용")}

def form_mentor_checklist():
    return {"체크": st.text_area("내용")}

def form_mentor_eval():
    return {"평가": st.text_area("내용")}