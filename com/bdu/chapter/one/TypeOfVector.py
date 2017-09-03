array = (1,2,3,4,5,6,7,8,9,10)
print(array)

myRange = range(1,11)

print(myRange)
print("logical vector")
rating_dict = {"Thriller":10.0,"Back in Black":8.5}
print(rating_dict)
isgrtr = rating_dict["Thriller"] > rating_dict["Back in Black"]
print(isgrtr)

minute_list=[42,42]
print(sum(minute_list))

print("set function")
Thriler_genre = set(["pop","pop","rock","R&B"])
print(Thriler_genre)

the_bodyguard_genre = set(["R&B","soul","pop"])
inter = Thriler_genre.intersection(the_bodyguard_genre)
sysmmetric_diff =  Thriler_genre.symmetric_difference(the_bodyguard_genre)
unique_values = Thriler_genre.union(the_bodyguard_genre)
print(inter)
print(sysmmetric_diff)
