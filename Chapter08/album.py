def make_album(artist, title, number_of_songs = None):
    album = {"artist": artist, "title": title}
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album

altered_state = make_album(artist="TesseracT",title= "Altered State")
even_in_arcadia = make_album(artist="Sleep Token", title= "Even In Arcadia")
remember_that_you_will_die = make_album("Polyphia", "Remember that you will die")
parrhesia = make_album(artist="Animals As Leaders", title= "Parrhesia", number_of_songs = 9)
print(altered_state)
print(even_in_arcadia)
print(remember_that_you_will_die)
print(parrhesia)