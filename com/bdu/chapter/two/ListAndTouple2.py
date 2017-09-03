album_list1=["Thriller","Back in Black","AC/DC"]
album_list2 = ["Back in Black","AC/DC","The dark side of the moon"]

print("Difference function")
print(set(album_list1).difference(album_list2))
print(set(album_list2).difference(album_list1))

print("remove function")
album_list1.remove("AC/DC")

print("pop")
album_list1.pop(1)

print("insert")
album_list1.insert(3,"new value")

print("count")
sound_track_list = ["N","Y","N","Y","N","Y","N","Y","N","Y"]
rating_touple = (10,9,3,7,7,5,9,10,6,8)

print(len(sound_track_list))
print(len(rating_touple))

print(sound_track_list.count("N"))

my_tuple = (123, 'Mike')
print "value is ", my_tuple * 2
