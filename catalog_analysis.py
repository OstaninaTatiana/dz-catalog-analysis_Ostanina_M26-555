import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies_list: list) -> float:
    """Возвращает среднюю оценку по каталогу, округленную до 1 знака"""
    total_rating = sum(movie["rating"] for movie in movies_list)
    return round(total_rating / len(movies_list), 1)


def catalog_age_stats(movies_list: list, current_year: int = 2026) -> tuple:
    """Возвращает кортеж: самый старый фильм, самый новый, среднее округленное вверх"""
    ages = [current_year - movie["year"] for movie in movies_list]
    oldest = max(ages)  
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average_age)


def duration_in_hours(minutes: int) -> str:
    """Переводит минуты в формат '2ч 35м'."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


def rating_tier(rating: float) -> str:
    """Возвращает категорию рейтинга"""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year: int) -> str:
    """Возвращает метку десятилетия"""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"
        case _:
            return "неизвестно"

def print_non_comedy_movies(movies_list: list) -> None:
    """Выводит названия фильмов, не относящихся к жанру comedy"""
    for movie in movies_list:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies_list: list) -> None:
    """Ищет первый фильм с рейтингом выше 9.0"""
    i = 0
    while i < len(movies_list):
        if movies_list[i]["rating"] > 9.0:
            print(f"Шедевр найден: {movies_list[i]['title']}")
            break
        i += 1
    else:
        # Ветка else срабатывает, если break не был вызван
        print("Шедевров не найдено")


def count_long_movies(movies_list: list, threshold: int = 120) -> int:
    """Считает количество фильмов длиннее threshold минут"""
    count = 0
    for movie in movies_list:
        if movie["duration_min"] > threshold:
            count += 1
    return count

def normalize_title(title: str) -> str:
    """Приводит строку к Title Case"""
    words = title.split()
    normalized_words = []
    for word in words:
        if word:
            normalized_word = word[0].upper() + word[1:]
            normalized_words.append(normalized_word)
    return " ".join(normalized_words)


def make_slug(title: str) -> str:
    """Превращает нормализованное название в слаг the-quiet-algorithm."""
    return title.lower().replace(" ", "-")


def format_report_line(movie: dict) -> str:
    """Возвращает единую строку с описанием фильма через f-строку."""
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'


def titles_sorted_by_rating(movies_list: list) -> list:
    """Возвращает названия фильмов, отсортированные по убыванию рейтинга."""
    sorted_movies = sorted(
        movies_list,
        key=lambda movie: movie["rating"],
        reverse=True,
    )
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies_list: list, n: int = 3) -> list:
    """Возвращает топ-N фильмов как список кортежей (title, rating)."""
    sorted_movies = sorted(
        movies_list,
        key=lambda movie: movie["rating"],
        reverse=True,
    )
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies_list: list) -> dict:
    """Возвращает словарь {жанр: количество фильмов}"""
    genre_count = {}
    for movie in movies_list:
        for genre in movie["genres"]:
            genre_count[genre] = genre_count.get(genre, 0) + 1
    return genre_count


def actor_filmography(movies_list: list) -> dict:
    """Возвращает словарь {актер: [список названий фильмов]}"""
    filmography = {}
    for movie in movies_list:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


def high_rated_movies_dict(movies_list: list) -> dict:
    """Возвращает словарь {title: rating} для фильмов выше среднего рейтинга"""
    avg_rating = average_rating(movies_list)
    return {
        movie["title"]: movie["rating"]
        for movie in movies_list
        if movie["rating"] > avg_rating
    }


def all_genres(movies_list: list) -> set:
    """Возвращает множество всех уникальных жанров каталога"""
    genres_set = set()
    for movie in movies_list:
        genres_set = genres_set | movie["genres"]
    return genres_set


def common_actors(movie1: dict, movie2: dict) -> set:
    """Возвращает множество актеров, снимавшихся в обоих фильмах"""
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    return actors1 & actors2


def genres_only_in_one(movies_a: list, movies_b: list) -> set:
    """Возвращает жанры, которые есть в movies_a, но нет в movies_b"""
    genres_a = set()
    for movie in movies_a:
        genres_a = genres_a | movie["genres"]

    genres_b = set()
    for movie in movies_b:
        genres_b = genres_b | movie["genres"]

    return genres_a - genres_b


def iter_high_rated(movies_list: list, min_rating: float = 8.0):
    """Функция-генератор, лениво отдающая фильмы с рейтингом >= min_rating"""
    for movie in movies_list:
        if movie["rating"] >= min_rating:
            yield movie


def total_duration_high_rated(movies_list: list, threshold: float = 7.0) -> int:
    """Считает суммарную длительность фильмов с рейтингом выше threshold"""
    return sum(
        movie["duration_min"]
        for movie in movies_list
        if movie["rating"] > threshold
    )


def build_report(movies_list: list) -> None:
    """Формирует и выводит итоговый консольный отчет по каталогу"""
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies_list)}")
    
    age_stats = catalog_age_stats(movies_list)
    print(f"Средний возраст фильмов: {age_stats[2]} лет")
    print()

    print("Топ-3 фильма:")
    top_movies = top_n_by_rating(movies_list, 3)
    for title, _ in top_movies:
        movie_dict = next(m for m in movies_list if m["title"] == title)
        print(f"  {format_report_line(movie_dict)}")
    print()

    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies_list)
    sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")
    print()

    print("Все жанры каталога:")
    all_unique_genres = sorted(all_genres(movies_list))
    print(", ".join(all_unique_genres))


if __name__ == "__main__":
    build_report(movies)