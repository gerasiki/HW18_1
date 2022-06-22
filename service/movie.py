from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, condition):

        if condition.get("director_id") is not None:
            movies = self.dao.get_by_director_id(condition.get("director_id"))
        elif condition.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(condition.get("genre_id"))
        elif condition.get("year") is not None:
            movies = self.dao.get_by_year(condition.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)

    def delete(self, mid):
        self.dao.delete(mid)
