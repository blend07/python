import pandas as pd
import streamlit as st
import plotly.express as px

# df = pd.DataFrame({
#     'Name':['John', 'Bob', 'Marley'],
#     'Age':[22,27,25],
#     'city':['Tirane', 'San Antonio', 'Amsterdam']
# })

# st.write(df)

books_df = pd.read_csv("file.csv")

st.title('Best selling books')
st.write('This app shows the best selling books on amazon from 2009 to 2022')
st.subheader('Books')

totalbooks = books_df.shape[0]
uniquename = books_df('Name').nunique()
averageratin = books_df('User Rating').mean()
averageprice = books_df('Price').mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total books: ", totalbooks)
col2.metric("Name: ", uniquename)
col3.metric("Average Rating: ", averageratin)
col4.metric("Average Price: ", averageprice)

