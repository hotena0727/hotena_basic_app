import streamlit as st

st.set_page_config(page_title="하테나일본어 포털", layout="centered")
st.title("하테나일본어 학습 포털")

st.caption("원하는 학습을 선택하세요 🙂")

APPS = {
    "🧠 단어": "https://hotenaoneapp-cvztfxksphaafkgrftpx9f.streamlit.app/",
    "📚 문법": "https://yyyy.streamlit.app/",
    "✍️ 한자": "https://zzzz.streamlit.app/",
    "📝 퀴즈": "https://aaaa.streamlit.app/",
}

for label, url in APPS.items():
    st.link_button(label, url, use_container_width=True)

st.divider()
st.caption("※ 각 앱은 최초 1회 로그인만 해두면 이후 자동 로그인(쿠키)로 편해집니다.")
