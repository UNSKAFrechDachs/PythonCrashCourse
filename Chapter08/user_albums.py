def make_album(artist, title, number_of_songs=None):
    album = {"artist": artist, "title": title}
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album


albums = []
while True:
    print("Enter your favourite album:")
    print("enter q to exit")

    artist = input("Name of the artist: ")
    if artist == "q":
        break
    title = input("Name of the album: ")
    if title == "q":
        break
    albums.append(make_album(artist, title))
print(f"Albums: {albums}")
