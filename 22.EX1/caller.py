from django.db.models import Q, Count, Avg, F
from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    queryset = Director.objects.all()

    if search_name and search_nationality:
        queryset = queryset.filter(
            full_name__icontains=search_name,
            nationality__icontains=search_nationality
        )
    elif search_name:
        queryset = queryset.filter(full_name__icontains=search_name)
    elif search_nationality:
        queryset = queryset.filter(nationality__icontains=search_nationality)

    queryset = queryset.order_by('full_name')

    if not queryset.exists():
        return ""

    return "\n".join([
        f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}"
        for d in queryset
    ])


def get_top_director():
    top_director_qs = Director.objects.get_directors_by_movies_count()

    if not top_director_qs.exists():
        return ""

    top_director = top_director_qs.first()

    return f"Top Director: {top_director.full_name}, movies: {top_director.movie_count}."


def get_top_actor():
    # Get actors annotated with number of starring roles
    actors = Actor.objects.annotate(
        starred_count=Count('starring_movies'),
        avg_rating=Avg('starring_movies__rating')
    ).filter(starred_count__gt=0).order_by('-starred_count', 'full_name')

    if not actors.exists():
        return ""

    top_actor = actors.first()
    movie_titles = top_actor.starring_movies.values_list('title', flat=True)

    if not movie_titles:
        return ""

    formatted_titles = ", ".join(movie_titles)
    formatted_avg_rating = f"{top_actor.avg_rating:.1f}" if top_actor.avg_rating else "0.0"

    return f"Top Actor: {top_actor.full_name}, starring in movies: {formatted_titles}, movies average rating: {formatted_avg_rating}"

def get_actors_by_movies_count():
    actors = Actor.objects.annotate(
        movie_count=Count('movies')
    ).filter(movie_count__gt=0).order_by('-movie_count', 'full_name')[:3]

    if not actors:
        return ""

    return "\n".join([
        f"{actor.full_name}, participated in {actor.movie_count} movies"
        for actor in actors
    ])


def get_top_rated_awarded_movie():
    movies = Movie.objects.filter(
        is_awarded=True
    ).annotate().order_by('-rating', 'title')

    if not movies.exists():
        return ""

    top_movie = movies.first()
    title = top_movie.title
    rating = f"{top_movie.rating:.1f}"
    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else "N/A"
    cast = top_movie.actors.all().order_by('full_name')
    cast_names = ", ".join(actor.full_name for actor in cast)

    return (
        f"Top rated awarded movie: {title}, rating: {rating}. "
        f"Starring actor: {starring_actor}. Cast: {cast_names}."
    )


def increase_rating():
    updated = Movie.objects.filter(
        is_classic=True,
        rating__lt=10.0
    )

    updated_count = updated.update(rating=F('rating') + 0.1)

    if updated_count > 0:
        return f"Rating increased for {updated_count} movies."
    return "No ratings increased."