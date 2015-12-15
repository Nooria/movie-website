import webbrowser


class Details():
    def __init__(self, title, poster_image, trailer_youtube):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def continue_play(movie, movies, series):
    # out put the information of movie or series you input
        if movie in movies:
           print movie.title
           print movie.storyline
           print movie.genre
           print movie.valid_rating
           movie.show_trailer()
        if movie in series:
           print movie.title
           print movie.tv_channel
           print movie.from_to
           movie.show_trailer()

class Movie(Details):
# this is chid for Details class perents using for movie information  
    def __init__(self, title, poster_image, trailer_youtube, storyline, genre, valid_rating):
        Details.__init__(self, title, poster_image, trailer_youtube)
        self.storyline = storyline
        self.genre = genre
        self.valid_rating = valid_rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class Series(Details):
    # this is chid for Details class perents using for series information
    def __init__(self, title, poster_image, trailer_youtube, tv_channel, from_to):
        Details.__init__(self, title, poster_image, trailer_youtube)
        self.tv_channel = tv_channel
        self.from_to = from_to

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
