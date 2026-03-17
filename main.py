import pandas as pd

df= pd.read_csv('bestsellers.csv')

# first 5 rows of the spreadsheet
print(df.head())

# shape of the spreadsheet
print(df.shape)

# column names of the spreadsheet
print(df.columns)

# summary statistics for each column
print(df.describe())

# changes are made directly to the original DataFrame with inplace=true
df.drop_duplicates(inplace=True)

df.rename(columns={"Name":"Title","Year":"Publication Year","User Rating":"Rating"},inplace=True)

df["Price"]= df["Price"].astype(float)

# which Authors have the most books on the amazon best sellers list
author_counts= df["Author"].value_counts()
print(author_counts)

# average ratings by genre
avg_rating_by_genre= df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)



# the books with the most reviews categorized by rating (to see the most popular books)
# 1. handling the year duplicates - keeping the versio of the book with the highest num of reviews ever recorded
df_unique_books=df.sort_values("Reviews",ascending=False).drop_duplicates(subset=["Title","Author"])


# 2. sorting the entire list by rating (ascending) & reviews (descending)- to find the most reviewed book by each rating category
# and handling duplicate ratings
df_sorted = df_unique_books.sort_values(by=["Rating","Reviews"], ascending=[False,False])
df_sorted = df_sorted.drop_duplicates(subset=["Rating"])

# 4. picking the columns we want to see 
most_popular_books= df_sorted[["Rating","Title","Author","Reviews"]]
print(most_popular_books)


# exporting top selling authors to a csv file
author_counts.head(10).to_csv("top_authors.csv")

# exporting avg ratings by genre to a csv file
avg_rating_by_genre.to_csv("avg_ratings_by_genre.csv")

# exporting most_popular_books to a csv file
most_popular_books.to_csv("most_popular_books.csv",index=False)
