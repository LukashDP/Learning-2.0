# favorites = {
#     'movies': ['Interstellar', 'Fast & Furious', 'Pirates of the Caribbean'],
#     'music': ['Queen', 'The Beatles', 'Coldplay'],
#     'sports': ['football', 'basketball', 'tennis']
# }
# Видаліть з цього списку sports та додайте новий ключ 'serials' де значенням будуть ваші улюблені серіали.


favorites = {
    'movies': ['Interstellar', 'Fast & Furious', 'Pirates of the Caribbean'],
    'music': ['Queen', 'The Beatles', 'Coldplay'],
    'sports': ['football', 'basketball', 'tennis']
}
q = favorites.pop('sports')
a = favorites.setdefault('serials', ['Breaking Bad', 'The Sopranos', 'Game of Thrones'])
print(favorites)