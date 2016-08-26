import media
import fresh_tomatoes

# Create instanes of Movie class
movie1 = media.Movie('Saving Private Ryan',
                     'http://goo.gl/EPaZGD',
                     'https://www.youtube.com/watch?v=zwhP5b4tD6g')
movie2 = media.Movie('The Bucket List',
                     'http://goo.gl/aXAl8E',
                     'https://www.youtube.com/watch?v=UvdTpywTmQg')
movie3 = media.Movie('The Shawshank Redemption',
                     'http://goo.gl/EbgjBk',
                     'https://www.youtube.com/watch?v=6hB3S9bIaco')

# Appending each object of Movie class in a list
movie = []
movie.append(movie1)
movie.append(movie2)
movie.append(movie3)

# Calling the function that renders the html page
fresh_tomatoes.open_movies_page(movie)
