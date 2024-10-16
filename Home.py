import streamlit as st

st.title("Home")

pg = st.navigation([st.Page("test.py"), st.Page("page_2.py")])
pg.run()