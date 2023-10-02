import pandas as pd


columns = ['ISBN', 'Book-Title', 'Book-Author']

types = {
    'ISBN': str,
    'Book-Title': str,
    'Book-Author': str,
}

df = pd.read_csv("./dataset/Books.csv", usecols=columns, dtype=types)


print(df.head())

df.to_csv("./new_dataset/NewBooks.csv", index=False)

df = pd.read_csv("./dataset/Ratings.csv")

# Remove rows where 'Book-Rating' is 0
df = df[df['Book-Rating'] != 0]

# Save the filtered DataFrame to a new CSV file
df.to_csv('./new_dataset/NewRatings.csv', index=False)
