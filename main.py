import streamlit as st
import langchain_helper

st.title('Resturant Name Generator')
cuisine=st.sidebar.selectbox("Pick a cusine",("Indian","Italian","Mexican","Japanees","Chineese"))

 
if cuisine:
    response=langchain_helper.generate_resturant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items=response['menu_items'].strip().split(",")

    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)
