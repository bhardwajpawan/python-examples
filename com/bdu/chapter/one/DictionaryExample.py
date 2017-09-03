album_dict = {1982: "Thriller",
        1980: "AC/DC",
        1973: "The dark side of the moon",
        1992: "The bodyguard",
        1977: ["Bat out of Hell", "Saturdat night fever", "Rumours"],
        1976: "their greatest hits"
        }


print(album_dict)

album_dict[1976] = "updated value"

album_dict[1990] = "inserted new value"

print("finding key from value")

album = "Thriller"

year = [key for key, value in album_dict.items()
        if(value == album)][0]

print(year)

len(album_dict)

#album_dict.clear() # to clear a dictionary

copy_album_dict = album_dict.copy()

print("dict with touple as keys")

genre_touple = ("pop","rock","soul","R&B","dicso","folk rock")

genre_dict = dict.fromkeys(genre_touple,"genre")

print(genre_dict)

print("other methods")

copy_album_dict.clear()
album_dict.copy()

album_dict.get(1999,"default value")

print(album_dict.__contains__(1982))

album_dict.keys()

album_dict.values()

print("merging two dic")

album_dict.update(copy_album_dict)

print(" paired items")

album_dict.items()

print("set default")
album_dict.setdefault("genre",["pop","rock"])