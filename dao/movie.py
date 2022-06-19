from dao.models.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).filter(Movie.id == mid).first()

    def get_by_director_id(self, director_id: int):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_by_genre_id(self, genre_id: int):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, data):
        movie = self.get_one(data.get('id'))
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.director_id = data.get('director_id')
        movie.genre_id = data.get('genre_id')

        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
