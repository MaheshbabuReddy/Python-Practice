import os

class Article:
    def _init_(self, name, author, views):
        self.name = name
        self.author = author
        self.views = views

    def _str_(self):
        return f"{self.name} by {self.author}, Views: {self.views}"

class JournalManager:
    def _init_(self, directory_path):
        self.directory_path = directory_path
        self.articles_by_genre = {}

    def process_files(self):
        for filename in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, filename)
            if os.path.isfile(file_path):
                genre, articles = self.read_file(file_path)
                self.articles_by_genre[genre] = articles

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            genre = file.readline().strip()
            articles = []
            for line in file:
                article_info = line.strip().split(',')
                name, author, views = article_info
                article = Article(name, author, int(views))
                articles.append(article)

            return genre, articles
    def display_articles_by_genre(self):
        for genre, articles in self.articles_by_genre.items():
            print(f"\nGenre: {genre}")
            for article in articles:
                print(article)

# Example usage:
journal_manager = JournalManager()
journal_manager.process_files()
journal_manager.display_articles_by_genre()