my_list = ["Micheal jackson","Thriller",1982,
           ("pop","rock" "r&H"),46.0,65,False]

print("touples are also like lists but data cant be changed")
print("touples are fixed size in nature while lists are dynamic")
print("touples are faster than list")
print("tpuples can also be used ase dic keys, list cnt be used")

print("tounples cannot be sorted")
mytouple = ("rock","pop","soul",1972,1977,1982)


album_list = ["Micheal Jackson","Thriller",1982,"00:42:19",
              ("pop","rock","R&B"),46.0,65,"30-Nov-82",
              False,10.0]

print(album_list)

genres_touple = ("pop","rock","hard rock","soft rock",
                 "progressive rock","folk rock","soul",
                 "disco","R&B")
print(genres_touple)

print("length function")

print(len(album_list))
print(len(genres_touple))
#print(min(album_list))
#print(max(album_list))

print(min(genres_touple))
print(max(genres_touple))

print(album_list.index(46.0))


#print(album_list.sort())
#print(album_list.sort(reverse=True))

album_list.reverse()
print(album_list)

print("converting touple into list")
genres_list = list(genres_touple)

print(genres_list )

print("build-in methods of list")
list.count()
list.pop()
list.append("new value")
list.extend(album_list)
list.remove(46.0)
list.index(46.0)