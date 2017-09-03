album_set = set(["Back in Black","AC/DC","The dark side of the moon"])

print("AC/DC" in album_set)

print("AC/DC" not in album_set)

print("country" not in album_set)

print("country"  in album_set)

print("copying a set")

album_set_backup = album_set.copy()

print("math functions: elements needs to be number")

number_set = set([23,65,23,87,32,98,13,89,76,45,34,75])

number_set2 = set([13,89,76])

print(sum(number_set))

print(sum(number_set) / len(number_set))

print("adding new element")

album_set.add("country")

print(number_set.issubset(number_set2))

print(number_set.issuperset(number_set2))

print(number_set2.issubset(number_set))

print(number_set2.issuperset(number_set))

print("remove or discard")

number_set.remove(23)

number_set.discard(65)

print(number_set)

print("removing all eleent")

number_set.clear()

