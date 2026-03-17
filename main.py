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

# exporting top selling authors to a csv file
author_counts.head(10).to_csv("top_authors.csv")

# exporting avg ratings by genre to a csv file
avg_rating_by_genre.to_csv("avg_ratings_by_genre.csv")

