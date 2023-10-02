import pandas as pd
import matplotlib.pyplot as plt

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

df = df[df['Book-Rating'] != 0]

df.to_csv('./new_dataset/NewRatings.csv', index=False)

ratings_df = pd.read_csv('./new_dataset/NewRatings.csv')

average_ratings = ratings_df.groupby('ISBN')['Book-Rating'].agg(['mean', 'count']).reset_index()

average_ratings.columns = ['ISBN', 'Average-Rating', 'Count']

average_ratings['ISBN'] = average_ratings['ISBN'].str.replace('[^0-9X]', '', regex=True)
average_ratings = average_ratings[average_ratings['ISBN'] != ""]
average_ratings['Average-Rating'] = average_ratings['Average-Rating'].round(2)

average_ratings = average_ratings.sort_values(by='Count', ascending=False)

print(average_ratings.head())

average_ratings.to_csv('./new_dataset/AverageRatings.csv', index=False)

average_ratings = pd.read_csv('./new_dataset/AverageRatings.csv')

average_rating_description = average_ratings['Average-Rating'].describe()

count_description = average_ratings['Count'].describe()

fig, axes = plt.subplots(2, 1, figsize=(8, 10))

bars = axes[0].bar(average_rating_description.index[1:], average_rating_description.values[1:], color='skyblue')
axes[0].set_title('Summary Statistics for Average-Rating')
axes[0].set_ylabel('Value')

for bar in bars:
    height = bar.get_height()
    axes[0].annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
                     textcoords="offset points", ha='center', fontsize=10)

bars = axes[1].bar(count_description.index[1:], count_description.values[1:], color='salmon')
axes[1].set_title('Summary Statistics for Count')
axes[1].set_ylabel('Value')

for bar in bars:
    height = bar.get_height()
    axes[1].annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
                     textcoords="offset points", ha='center', fontsize=10)


plt.savefig('./plots/plot.png', bbox_inches='tight')

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 1, figsize=(8, 10))

axes[0].boxplot(average_ratings['Average-Rating'], vert=False, showfliers=True)
axes[0].set_title('Box Plot for Average-Rating with Outliers')
axes[0].set_xlabel('Average-Rating')

axes[1].boxplot(average_ratings['Count'], vert=False, showfliers=True)
axes[1].set_title('Box Plot for Count with Outliers')
axes[1].set_xlabel('Count')

plt.tight_layout()

plt.savefig('./plots/boxplot.png', bbox_inches='tight')

plt.show()
