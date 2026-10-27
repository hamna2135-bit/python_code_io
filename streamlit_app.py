import streamlit as st
from pygments import highlight
from pygments.lexers import PythonLexer
import pygments.formatters as pf

st.title("Pythonコード実行環境")
st.write(
    "コードをここで試すことができるぞい"
)

raw_code = st.text_area("code")

st.html(highlight(raw_code,PythonLexer(),pf.HtmlFormatter()))
st.write(highlight(raw_code,PythonLexer(),pf.HtmlFormatter()))