import media
import fresh_tomatoes

# movie 1: Demolition Man
demolition_man = media.Movie("Demolition Man",
                             "A police officer is brought out of suspended\
                              animation in prison to pursue an\
                              old ultra-violentnemesis who\
                              is loose in a non-violent future\
                              society.",
                             " http://t1.gstatic.com/images?q=tbn:ANd9GcTaXvsT6Dy-XkYhNax68Nfq73Iq1u72g8a19r6P7QYfL7H7bDv7",  # noqa
                             "https://www.youtube.com/watch?v=18e4GeUwVWs")
# movie 2:The Godfather
the_godfather = media.Movie("The Godfather",
                            "The aging patriarch of\
                            an organized crime dynasty\
                            transfers control of his clandestine\
                            empire to his reluctant son.",
                            " http://static.metacritic.com/images/products/movies/3/47c2b1f35087fc23c5ce261bbc3ad9e0.jpg",  # noqa
                            "https://www.youtube.com/watch?v=sY1S34973zA")
# movie 3: Dead Pool
dead_pool = media.Movie("Dead Pool",
                        "A mercenary with accelerated healing\
                        powers and a quest for revenge.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcTvrIHJfasS6poy34esN1O5hZonXaiqfEZb4WbnbAa9qJCIL8_9",  # noqa
                        "https://www.youtube.com/watch?v=FyKWUTwSYAs")
# movie 4: Team America
team_america = media.Movie("Team America",
                           "Popular Broadway actor Gary Johnston is recruited by\
                           the elite counter-terrorism organization\
                           Team America: World Police. As the world\
                           begins to crumble around him,\
                           he must battle with terrorists,\
                           celebrities and falling in love.",
                           "http://www.gstatic.com/tv/thumb/movieposters/34945/p34945_p_v8_aa.jpg",  # noqa
                           "https://www.youtube.com/watch?v=RPBX47zSktc")
# movie 5: brother Bear
brother_bear = media.Movie("Brother Bear",
                           "When a young Inuit hunter needlessly kills\
                           a bear, he is magically changed into a bear himself\
                           as punishment with a talkative\
                           cub being his only guide to changing back.",
                           "http://www.gstatic.com/tv/thumb/movieposters/33159/p33159_p_v8_af.jpg",  # noqa
                           "https://www.youtube.com/watch?v=B80VKbxZs6E")
# movie 6: Mulan
mulan = media.Movie("Mulan",
                    "To save her father from death in the army,\
                    a young maiden secretly goes in his place\
                    and becomes one of China's greatest\
                    heroines in the process.",
                    "http://www.gstatic.com/tv/thumb/movieposters/21118/p21118_p_v8_ac.jpg",  # noqa
                    "https://www.youtube.com/watch?v=wAbGAkkOgcM")

# this line opens website on the browser
movies = [demolition_man, the_godfather, dead_pool,
          team_america, brother_bear, mulan]
fresh_tomatoes.open_movies_page(movies)
