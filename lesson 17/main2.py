import streamlit as st

col1,col2,col3,col4,col5 = st.columns(5, gap="small", vertical_alignment="center")

with col1:
    st.header("Kolona 1")
    st.write("Kjo eshte kolona 1")
with col2:
    st.header("Kolona 2")
    st.write("Kjo eshte kolona 2")
with col3:
    st.header("Kolona 3")
    st.write("Kjo eshte kolona 3")
with col4:
    st.header("Kolona 4")
    st.write("Kjo eshte kolona 4")
with col5:
    st.header("Kolona 5")
    st.write("Kjo eshte kolona 5")