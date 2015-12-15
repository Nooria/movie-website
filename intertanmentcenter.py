import media
import fresh_tomatoes

troy = media.Movie("Troy",
                   "http://mycatbirdseat.com/wp-content/uploads/2013/06/troy-duel-.jpg",
                   "https://www.youtube.com/watch?v=znTLzRJimeY",
                   "An adaptation of Homer's great epic,the film follows the assault on Troy by the united Greek forces and chronicles the fates of the men involved.",
                   ['Advanture', 'Drama'], "R")


the_godfather = media.Movie("The Godfather",
                            "http://www.faithmeetsworld.com/wp-content/uploads/2014/05/Godfather.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA",
                            "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                            ["Crime,Drama"], "R")

despicable_me = media.Movie("Despicable Me",
                            "http://www.mascotshowsblog.com/wp-content/uploads/2015/06/despicable-me-2-2013-spoiler-alert-level-minions.jpeg",
                            "https://www.youtube.com/watch?v=bvXMWcUhKMY",
                            "When a criminal mastermind uses a trio of orphan girls as pawns for a grand scheme, he finds their love is profoundly changing him for the better.",
                            ["Animation", "Comedy"], "PG")


spy = media.Movie("Spy",
                  "http://www.flickeringmyth.com/wp-content/uploads/2015/03/SPY_1SHEET.jpg",
                  "https://www.youtube.com/watch?v=ltijEmlyqlg",
                  "A desk-bound CIA analyst volunteers to go undercover to infiltrate the world of a deadly arms dealer, and prevent diabolical global disaster.",
                  ["Action", "Comedy", "Crime"], "R")


les_miserables = media.Movie("Les Miserables",
                             "http://www.heyuguys.com/images/2012/11/Les-Mis%C3%A9rables-International-Poster.jpg",
                             "https://www.youtube.com/watch?v=IuEFm84s4oI",
                             "In 19th-century France, Jean Valjean, who for decades has been hunted by the ruthless policeman Javert after breaking parole, agrees to care for a factory worker's daughter. The decision changes their lives for ever",
                             ["Musical", "Drama", "Romance"], "PG-13")


v_for_vendetta = media.Movie("V for Vendetta",
                             "http://comicwallpapers10.net/wp-content/uploads/images/67/v-for-vendetta.jpg",
                             "https://www.youtube.com/watch?v=k_13fFIrhPk",
                             "In a future British tyranny, a shadowy freedom fighter, known only by the alias of V, plots to overthrow it with the help of a young woman.",
                             ["Action", "Drama", "Thriller"], "R")


modern_family = media.Series("Modern Family",
                             "https://en.wikipedia.org/wiki/Modern_Family#/media/File:Modern_Family_Promo_Season_1.jpg",
                             "https://www.youtube.com/watch?v=aogZUDx51vQ",
                             "abc", "2000-")
the_simpsons = media.Series("The Simpsons",
                            "https://tstoaddicts.files.wordpress.com/2014/04/the-simpsons-springfield.jpg",
                            "https://www.youtube.com/watch?v=UGr0UIX8T_k",
                            "FOX", "1989-")

csi = media.Series("CSI: Crime Scene Investigation",
                   "http://www.seat42f.com/wp-content/uploads/2014/07/CSI-Season-14-DVD-Cover.jpg",
                   "https://www.youtube.com/watch?v=Y8IYh8pzXGo",
                   "SYFY", "2000 to 2015")

movies = [troy, the_godfather, despicable_me, spy, les_miserables,
          v_for_vendetta]
fresh_tomatoes.open_movies_page(movies)

series = [modern_family, the_simpsons, csi]

continueing = raw_input("Do you want to play? ")
while continueing == "yes":
    movie = input("Write your favorate movie or series: ")
    continue0 = media.Details.continue_play(movie, movies, series)
    continueing = raw_input("Do you want to play? ")
