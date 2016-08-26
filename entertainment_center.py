import media
import fresh_tomatoes
movie1 = media.Movie('Saving Private Ryan','https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg','https://www.youtube.com/watch?v=zwhP5b4tD6g')
movie2 = media.Movie('The Bucket List','http://briansrunningadventures.com/wp-content/uploads/2014/12/bucketlist.jpg','https://www.youtube.com/watch?v=UvdTpywTmQg')
movie3 = media.Movie('The Shawshank Redemption','http://www.deckchaircinema.com/wp-content/uploads/2016/07/the-shawshank-redemption.jpg','https://www.youtube.com/watch?v=6hB3S9bIaco')

movie = []
movie.append(movie1)
movie.append(movie2)
movie.append(movie3)

fresh_tomatoes.open_movies_page(movie)