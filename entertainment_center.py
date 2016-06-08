import media
import fresh_tomatoes

#Instances of class Movie
saving_private_ryan = media.Movie("Saving Private Ryan",
								  "A group of soldiers are on a mission to find private James Francis Ryan and bring him back home",
								  "https://upload.wikimedia.org/wikipedia/en/thumb/a/ac/Saving_Private_Ryan_poster.jpg/220px-Saving_Private_Ryan_poster.jpg",
								  "https://www.youtube.com/watch?v=zwhP5b4tD6g")
forrest_gump = media.Movie("Forrest Gump", "A man on an epic journey",
						   "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
						   "https://www.youtube.com/watch?v=uPIEn0M8su0")

the_dark_knight = media.Movie("The Dark Knight", 
							  "Batman must stop the Joker from wreaking havoc on Gotham",
							  "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",
							  "https://www.youtube.com/watch?v=EXeTwQWrcwY")
the_godfather = media.Movie("The Godfather", 
							"The son of a notorious mobster must take control of his organized crime group",
							"https://upload.wikimedia.org/wikipedia/en/thumb/1/1c/Godfather_ver1.jpg/220px-Godfather_ver1.jpg",
							"https://www.youtube.com/watch?v=sY1S34973zA")
#List of our movies
movies = [saving_private_ryan, forrest_gump, the_dark_knight, the_godfather]
fresh_tomatoes.open_movies_page(movies)
