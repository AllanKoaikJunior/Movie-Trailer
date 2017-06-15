import webbrowser
class Movie():
    """This class provides related information about the website"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    """This class provides the trailer for the website"""    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
