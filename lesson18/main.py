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
uniquename = books_df['Name'].nunique()
averageratin = books_df['User Rating'].mean()
averageprice = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total books: ", totalbooks)
col2.metric("Name: ", uniquename)
col3.metric("Average Rating: ", f"{averageratin:.2f}")
col4.metric("Average Price: ", f"${averageprice:.2f}")

st.subheader("Stats")
st.write(books_df.head())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 book titles")
    top_title = books_df["Name"].value_counts().head(10)
    st.bar_chart(top_title)

with col2:
    st.subheader("The top authors")
    top_title = books_df["Author"].value_counts().head(10)
    st.bar_chart(top_title)

st.subheader("Genre Distribution")
fig = px.pie(books_df, names="Genre", title='Most liked Genre 2009-2022', color="Genre",
color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)


st.subheader("Top 15 Authors")
top_authors=books_df["Author"].value_counts().head(15).reset_index()
top_authors.columns = ['Author','Count']

figg = px.bar(top_authors, x='Count', y='Author', orientation='h',
              title='Top 15 Authors',
              labels={'Count': 'Count of Books Published','Author':'Author'},
              color='Count', color_continuous_scale=px.colors.sequential.Plasma
              )

st.plotly_chart(figg)