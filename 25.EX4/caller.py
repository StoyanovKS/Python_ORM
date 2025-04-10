from django.db.models import Count, Q
from main_app.models import Label, Artist
from main_app.models import Album

def get_labels(search_string=None):
    if search_string is None:
        return "No search."

    labels = Label.objects.filter(name__icontains=search_string).order_by('-market_share', 'name')

    if not labels.exists():
        return "No labels match this search."

    result_lines = [
        f"Label: {label.name}, headquarters: {label.headquarters}, market share: {int(label.market_share)}%"
        for label in labels
    ]

    return "\n".join(result_lines)


def get_best_label():
    best_label = Label.objects.annotate(album_count=Count('albums')) \
                              .order_by('-album_count', 'name') \
                              .first()

    if not best_label:
        return "No data."

    return f"The best label is {best_label.name} with {best_label.album_count} albums."


def get_artists_by_albums_count():
    artists = Artist.objects.annotate(album_count=Count('albums')) \
                            .order_by('-album_count', 'name')[:3]

    if not artists:
        return "No data."

    return "\n".join([
        f"{artist.name}: {artist.album_count} album/s."
        for artist in artists
    ])

def get_most_productive_artist():
    """
    Returns the artist with the most albums.
    Tiebreaker: name ascending.
    """
    artist = Artist.objects.annotate(album_count=Count('albums')) \
                           .filter(album_count__gt=0) \
                           .order_by('-album_count', 'name') \
                           .first()

    if not artist:
        return "No data."

    album_titles = artist.albums.order_by('title').values_list('title', flat=True)
    return f"The most productive artist is {artist.name} with album titles: {', '.join(album_titles)}."


def get_latest_hit_album():
    """
    Returns the latest hit album (is_hit=True).
    Tiebreaker: title ascending.
    """
    album = Album.objects.filter(is_hit=True, release_date__isnull=False) \
                         .order_by('-release_date', 'title') \
                         .first()

    if not album:
        return "No data."

    artist_names = album.artists.order_by('name').values_list('name', flat=True)

    if artist_names:
        artists = ", ".join(artist_names)
    else:
        artists = "TBA"

    return f"The latest hit album is {album.title}, type: {album.type}, artists: {artists}."


def award_album(album_title: str):
    """
    Increases awards by 1 for each artist associated with the album of given title.
    """
    try:
        album = Album.objects.get(title=album_title)
    except Album.DoesNotExist:
        return "Updates not applicable."

    artists = album.artists.all()

    if not artists:
        return "Updates not applicable."

    for artist in artists:
        artist.awards += 1
        artist.save()

    return f"Updated awards for {artists.count()} artist/s."