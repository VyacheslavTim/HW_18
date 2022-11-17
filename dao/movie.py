from model.movie import Movie

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, value):
        return self.session.query(Movie).filter(Movie.director_id == value).all()

    def get_by_genre_id(self, value):
        return self.session.query(Movie).filter(Movie.genre_id == value).all()

    def get_by_year(self, value):
        return self.session.query(Movie).filter(Movie.year == value).all()

    def create(self, movie_d):
        m_keys = Movie(**movie_d)
        self.session.add(m_keys)
        self.session.commit()
        return m_keys

    def update(self, movie_d):
        m_keys = Movie(**movie_d)
        self.session.get_one(movie_d.get(m_keys))
        self.session.commit()
        return m_keys

    def delete(self, uid):
        movie = self.get_one(uid)
        self.session.delete(movie)
        self.session.commit()





