import streamlit as st
from sections import set_sidebar

st.set_page_config(page_title="Dashbord" , page_icon="🌍" , layout="wide")
st.subheader("📧 Email Marketing analytics platform ")
st.markdown("### Actions")

set_sidebar(st)
