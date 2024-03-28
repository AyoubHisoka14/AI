from SPARQLWrapper import SPARQLWrapper, JSON
server_address = "http://localhost:3030/new/sparql"
sparql = SPARQLWrapper(server_address)
sparql.setReturnFormat(JSON)


def most_profitable_movie() -> str:
    """
    Calculate and return the most profitable movie (revenue - budget).

    :return: Most profitable movie.
    """
    query = """
        PREFIX : <https://www.themoviedb.org/kaggle-export/>

        SELECT ?title WHERE {
          ?movie a :Movie;
            :revenue ?revenue;
           :budget ?budget;
           :title ?title.
        }
        ORDER BY DESC(?revenue-?budget)
        LIMIT 1
        """
    sparql.setQuery(query)
    results_dict = sparql.query().convert()
    return results_dict['results']['bindings'][0]['title']['value']


def least_profitable_movie() -> str:
    """
    Calculate and return the least profitable movie (revenue - budget).

    :return: Least profitable movie.
    """
    query = """
        PREFIX : <https://www.themoviedb.org/kaggle-export/>

        SELECT ?title WHERE {
          ?movie a :Movie;
            :revenue ?revenue;
           :budget ?budget;
           :title ?title.
        }
        ORDER BY (?revenue-?budget)
        LIMIT 1
        """
    sparql.setQuery(query)
    results_dict = sparql.query().convert()
    return results_dict['results']['bindings'][0]['title']['value']


def longest_name() -> str:
    """
    Return the name of the actor with the longest name.

    :return: Name of actor.
    """
    query = """
        PREFIX : <https://www.themoviedb.org/kaggle-export/>

        SELECT ?cast_name WHERE {
            ?cast a :Cast;
                :name ?cast_name.  
        }
        ORDER BY DESC(STRLEN(?cast_name))
        LIMIT 1
        """
    sparql.setQuery(query)
    results_dict = sparql.query().convert()
    return results_dict['results']['bindings'][0]['cast_name']['value']


def shortest_title() -> str:
    """
    Return the title of the movie with the shortest title.

    :return: Movie title.
    """
    query = """
        PREFIX : <https://www.themoviedb.org/kaggle-export/>

        SELECT ?title WHERE {
          ?movie a :Movie;
           :title ?title.
        }
        ORDER BY (STRLEN(?title))
        LIMIT 1
        """
    sparql.setQuery(query)
    results_dict = sparql.query().convert()
    return results_dict['results']['bindings'][0]['title']['value']


def most_expensive_per_time() -> str:
    """
    Return the title of the movie with the highest cost per time (in USD / min).

    :return: Movie title.
    """
    query = """
        PREFIX : <https://www.themoviedb.org/kaggle-export/>

        SELECT ?title WHERE {
            ?movie a :Movie;
                :title ?title;
                :budget ?budget;
                :runtime ?runtime.
          FILTER(?runtime!=0).
        }
        ORDER BY DESC(?budget/?runtime)
        LIMIT 1
        """
    sparql.setQuery(query)
    results_dict = sparql.query().convert()
    return results_dict['results']['bindings'][0]['title']['value']


def cheap_popular_movie() -> str:
    """
    Return the title of the movie with popularity >= 10 and the lowest budget.

    :return: Movie title.
    """
    query = """
        PREFIX : <https://www.themoviedb.org/kaggle-export/>

        SELECT ?title WHERE {
            ?movie a :Movie;
                :title ?title;
                :popularity ?popularity;
                :budget ?budget.
          FILTER(?popularity>=10).
        }
        ORDER BY (?budget)
        LIMIT 1
        """
    sparql.setQuery(query)
    results_dict = sparql.query().convert()
    return results_dict['results']['bindings'][0]['title']['value']


def expensive_unpopular_movie() -> str:
    """
    Return the title of the movie with popularity <= 1 and the highest budget.

    :return: Movie title.
    """
    query = """
        PREFIX : <https://www.themoviedb.org/kaggle-export/>

        SELECT ?title WHERE {
            ?movie a :Movie;
                :title ?title;
                :popularity ?popularity;
                :budget ?budget.
          FILTER(?popularity<=1).
        }
        ORDER BY DESC(?budget)
        LIMIT 1
        """
    sparql.setQuery(query)
    results_dict = sparql.query().convert()
    return results_dict['results']['bindings'][0]['title']['value']


if __name__ == '__main__':
    # Check most_profitable_movie()
    movie = most_profitable_movie()
    print(f"The most profitable movie is {movie}.")

    # Check least_profitable_movie()
    movie = least_profitable_movie()
    print(f"The least profitable movie is {movie}.")

    # Check longest_name()
    actor = longest_name()
    print(f"The actor with the longest name is {actor}.")

    # Check shortest_title()
    movie = shortest_title()
    print(f"The movie with the shortest title is {movie}.")

    # Check most_expensive_per_time()
    movie = most_expensive_per_time()
    print(f"The movie with the highest cost per time is {movie}.")

    # Check cheap_popular_movie()
    movie = cheap_popular_movie()
    print(f"The cheapest movie with popularity >= 10 is {movie}.")

    # Check expensive_unpopular_movie()
    movie = expensive_unpopular_movie()
    print(f"The most expensive movie with popularity <= 10 is {movie}.")