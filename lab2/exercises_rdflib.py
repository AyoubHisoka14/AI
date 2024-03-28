import rdflib


def get_departments() -> list:
    """
    Query and return a list of all (distinct) departments.

    :return: List of departments.
    """
    query_result = g.query("""

       SELECT DISTINCT ?department WHERE {
  		?crew a :Crew;
            :department ?department.
       }
       """)
    result_list = [row['department'].toPython() for row in query_result.bindings]
    return result_list


def n_companies() -> int:
    """
    Query all companies and return the number of companies.

    :return: Number of (distinct) companies.
    """
    query_result = g.query("""

       SELECT (COUNT(distinct ?company) as ?number) WHERE {
           ?movie a :Movie;
               :production_companies ?company.
       }
       """)

    # Extracting the count value directly from the query result
    result_list = [row['number'].toPython() for row in query_result.bindings]
    return int(result_list[0])


def caesar_movies() -> list:
    """
    Query list of movies in which Julius Caesar was depicted.

    :return: List of movies.
    """
    query_result = g.query("""
        SELECT ?title WHERE {
            ?movie a :Movie;
                :title ?title;
                :cast ?cast.
          ?cast :character "Julius Caesar".
        }
        """)
    result_list = [row['title'].toPython() for row in query_result.bindings]
    return result_list


def most_expensive_movie() -> tuple:
    """
    Query the most expensive movie and return its title and budget.

    :return: Tuple of movie title and budget.
    """
    query_result = g.query("""

        SELECT ?title ?budget WHERE {
            ?movie a :Movie;
                :title ?title;
                :budget ?budget.
        }
        ORDER BY DESC(?budget)
        LIMIT 1
        """)

    # Extracting the title and budget directly from the query result
    result_list = [row['title'].toPython() for row in query_result.bindings]
    result_list2 = [row['budget'].toPython() for row in query_result.bindings]

    return (result_list[0], result_list2[0])


def most_successful_movie() -> tuple:
    """
    Query the movie with the highest revenue and return its title and revenue.

    :return: Tuple of movie title and budget.
    """
    query_result = g.query("""

        SELECT ?title ?revenue WHERE {
            ?movie a :Movie;
                :title ?title;
                :revenue ?revenue.
        }
        ORDER BY DESC(?revenue)
        LIMIT 1
        """)
    result_list = [row['title'].toPython() for row in query_result.bindings]
    result_list2 = [row['revenue'].toPython() for row in query_result.bindings]

    return (result_list[0], result_list2[0])


def most_popular_movie() -> str:
    """
    Query the most popular movie and return its title.

    :return: Movie title.
    """
    query_result = g.query("""

            SELECT ?title WHERE {
                ?movie a :Movie;
                    :title ?title;
                    :popularity ?popularity.
            }
            ORDER BY DESC(?popularity)
            LIMIT 1
            """)
    result_list = [row['title'].toPython() for row in query_result.bindings]
    return result_list[0]



def least_popular_movie() -> str:
    """
    Query the least popular movie and return its title.

    :return: Movie title.
    """
    query_result = g.query("""

                SELECT ?title WHERE {
                    ?movie a :Movie;
                        :title ?title;
                        :popularity ?popularity.
                }
                ORDER BY (?popularity)
                LIMIT 1
                """)
    result_list = [row['title'].toPython() for row in query_result.bindings]
    return result_list[0]


def most_recent_movie() -> tuple:
    """
    Query the most recent movie and return its title and release date.

    :return: Movie title and release date.
    """
    query_result = g.query("""

      SELECT ?title ?release_date WHERE {
          ?movie a :Movie;
              :title ?title;
              :release_date ?release_date.
      }
      ORDER BY (?release_date)
      LIMIT 1
      """)
    result_list = [row['title'].toPython() for row in query_result.bindings]
    result_list2 = [row['release_date'].toPython() for row in query_result.bindings]

    return (result_list[0],result_list2[0])


if __name__ == '__main__':

    path_to_graph = "TMDB.ttl"
    g = rdflib.Graph()
    g.parse(path_to_graph, format='turtle')


    # Check get_departments()
    departments = get_departments()
    print(f"Following departments exist: {departments}")

    # Check n_companies()
    n_comp = n_companies()
    print(f"{n_comp} companies exist.")

    # Check caesar_movies()
    movies = caesar_movies()
    print(f"Julius Caesar was depicted in the following movies: {movies}")

    # Check most_expensive_movie()
    movie = most_expensive_movie()
    print(f"The most expensive movie is {movie}.")

    # Check most_successful_movie()
    movie = most_successful_movie()
    print(f"The most successful movie is {movie}.")

    # Check most_popular_movie()
    movie = most_popular_movie()
    print(f"The most popular movie is {movie}.")

    # Check least_popular_movie()
    movie = least_popular_movie()
    print(f"The least successful movie is {movie}.")

    # Check most_recent_movie()
    movie = most_recent_movie()
    print(f"The most recent movie is {movie}.")
