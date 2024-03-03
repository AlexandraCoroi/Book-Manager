import pandas as pd

class BookRec:
    def __init__(self, books_df):
        self.books_df = books_df

    def get_top_books(self, num, filter='all'):
        if filter == 'recent':
            recent_books = self.books_df[self.books_df['publish_year'] == self.books_df['publish_year'].max()]
            top_recent_books = recent_books.sort_values(by='rating', ascending=False).head(num)
            return top_recent_books
        elif filter == 'year_favorites':
            last_year = self.books_df['publish_year'].max() - 1
            year_favorites = self.books_df[self.books_df['publish_year'] == last_year]
            top_year_favorites = year_favorites.sort_values(by='rating', ascending=False).head(num)
            return top_year_favorites
        elif filter == 'most_read':
            most_read_books = self.books_df.sort_values(by='read_count', ascending=False).head(num)
            return most_read_books
        elif filter == 'all_time_favorites':
            all_time_favorites = self.books_df.sort_values(by='rating', ascending=False).head(num)
            return all_time_favorites
        else:
            top_books = self.books_df.sort_values(by='rating', ascending=False).head(num)
            return top_books

books_data = [
    {'title': 'Book 1', 'publish_year': 2020, 'rating': 4.5, 'read_count': 100},
    {'title': 'Book 2', 'publish_year': 2019, 'rating': 4.0, 'read_count': 150},
]


books_df = pd.DataFrame(books_data)
book_rec = BookRec(books_df)
