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

st.sidebar.header("Sidebar")
st.sidebar.write("This is sidebar")
st.sidebar.radio("Choosse", ["Home","Contact Us","Settings"])

with st.form("My Form", clear_on_submit=True):
    name = st.text_input("Write your name")
    surname = st.text_input("Write your surname")
    age = st.slider("Age", min_value=0, max_value=100)
    email = st.text_input("Email")
    terms = st.checkbox("I agree to the terms and conditions")
    submitbutton = st.form_submit_button(label="Submit")

if submitbutton:
    

    if terms:
        st.write(f"Name: {name}")
        st.write(f"Surname: {surname}")
        st.write(f"Age: {age}")
        st.write(f"Email: {email}")
        st.write("You have agreed to the terms and conditions")
    else:
        st.write("You haven't agreed to the terms and conditions")

tab1,tab2,tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])

with tab1:
    st.header("Tab1")


with tab2:
    st.header("Tab2")

    with st.form("yourForm", clear_on_submit=True):
        name = st.text_input("Write your name")
        surname = st.text_input("Write your surname")
        age = st.slider("Age", min_value=0, max_value=100)
        email = st.text_input("Email")
        terms = st.checkbox("I agree to the terms and conditions")
        submitbutton = st.form_submit_button(label="Submit")

    if submitbutton:
    

        if terms:
            st.write(f"Name: {name}")
            st.write(f"Surname: {surname}")
            st.write(f"Age: {age}")
            st.write(f"Email: {email}")
            st.write("You have agreed to the terms and conditions")
        else:
            st.write("You haven't agreed to the terms and conditions")

with tab3:
    st.header("Tab3")
