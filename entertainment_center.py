import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar=media.Movie("Avatar",
                   "A Marine on an alient planet",
                   "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                   "http://www.youtube.com/watch?v=-9ceBgWV8io")
school_of_rock=media.Movie("School of Rock",
                   "School of Rock",
                   "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                   "http://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille=media.Movie("Ratatouille",
                   "Ratatouille",
                   "http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg",
                   "http://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris=media.Movie("Midnight in Paris",
                   "Midnight in Paris",
                   "http://t3.gstatic.com/images?q=tbn:ANd9GcTk3ssys2bKM5-U6XMgvoD8yVoS5Io2YKg_1xA6x6GA8mKuuqID",
                   "http://www.youtube.com/watch?v=atLg2wQQxvU")
hunger_games=media.Movie("Hunger Games",
                   "Hunger Games",
                   "https://reelisticviewsdotcom.files.wordpress.com/2016/10/the-hunger-games-1.jpg",
                   "http://www.youtube.com/watch?v=PbA63a7H0bo")
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
