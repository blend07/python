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

st.sidebar.header("Add a new data")
with st.sidebar.form("book_form"):
    newname = st.text_input("Book Name")
    newauthor = st.text_input("Author Name")
    newuserrating = st.slider("User Rating", 0.0,5.0,0.0,0.1)
    newreviews = st.number_input("Reviews", min_value=0, step=1)
    newprice = st.number_input("Price", min_value=0,step=1)
    newyear=st.number_input("Year", min_value=2009, max_value=2022)
    newgenre=st.selectbox("Genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")

if submit_button:
    new_data={
        'Name':newname,
        'Author':newauthor,
        'User Rating':newuserrating,
        'Reviews':newreviews,
        'Price':newprice,
        'Year':newyear,
        'Genre':newgenre
    }
    books_df = pd.concat([pd.DataFrame(new_data,index=[0]),books_df],ignore_index=True)
    books_df.to_csv('file.csv', index=False)
    st.sidebar.success("New book added succesfully")

st.sidebar.header("Filter Option")
selected_author = st.sidebar.selectbox("Select Author",["All"] + list(books_df['Author'].unique()))
selected_year = st.sidebar.selectbox("Select Year",["All"] + list(books_df['Year'].unique()))
selected_genre = st.sidebar.selectbox("Select Genre",["All"] + list(books_df['Genre'].unique()))
min_rating = st.sidebar.selectbox("Minimum User Rating",0.0,5.0,0.0,0.1)
max_price = st.sidebar.selectbox("Max Price",0,books_df['Price'].max(),books_df['Price'].max())

filered_books_df = books_df.copy()

if selected_author != "All":
    filered_books_df = filered_books_df[filered_books_df['Author']==selected_author]
if selected_year != "All":
    filered_books_df = filered_books_df[filered_books_df['Year']==selected_year]
if selected_genres != "All":
    filered_books_df = filered_books_df[filered_books_df['Genre']==selected_genre]

filered_books_df = filered_books_df[
    (filered_books_df['User Rating']>=min_rating)&(filered_books_df['Price']<=max_price)]



st.subheader("Summary Statistics")
totalbooks = filered_books_df.shape[0]
uniquename = filered_books_df['Name'].mean()
averageratin = filered_books_df['User Rating'].mean()
averageprice = filered_books_df['Price'].mean()

col1,col2,col3,col4 = st.columns(4)
col1.metric("Total Books", totalbooks)
col1.metric("Unique Title", uniquename)
col1.metric("Average Rating", f"{averageratin: .2f}")
col1.metric("Average Price", f"{averageratin: .2f}")

st.subheader("Dataset Preview")
st.write(filered_books_df.head())

col1,col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book titles")
    top_title = filered_books_df['Name'.value_counts().head(10)]
    st.bar_chart(top_title)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = filered_books_df['Author'].value_counts().head(10)

st.subheader("Genre Distribution")
fig = px.pie(filered_books_df, names="Genre", title="Most Liked Genre", color='Genre',
             color_discrete_sequence=px.colors.sequential.Plasma)

st.plotly_chart(fig)

st.subheader("Number of fiction vs non-fiction books over years")
size = filered_books_df.groupby(['Year', 'Genre']).size().reset_index(name='Count')
fig = px.bar(size, x='Year', y='Count',color = 'Genre', title="Number of Fiction vs Non-Fiction Books",
             color_discrete_sequence=px.colors.sequential.Plasma, barmode='group'
             )

st.plotly_chart(fig)

st.subheader("Top 15 authors by counts of books published (2009-2022)")

top_author=filered_books_df['Author'].value_counts().head(15)
top_authors.columns=['Author','Count']

fig = px.bar(top_authors,x='Count',y='Author', orientation='h',
             title='Top 15 authors by counts of books Published',
             labels={'Count':'Count of Books Published','Author':'Author'},
             color = 'Count', color_continuous_scale=px.color.sequential.Plasma)

st.plotly_chart(fig)

