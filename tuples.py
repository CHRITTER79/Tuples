# myCars is a list and you can change it
# myCars = ["Ford", "Mercedes", "Audi"]
# myCars[0] = "Ford Titanium"

# myCars is a tuple and you cannot change it
# myCars = ("Ford", "Mercedes", "Audi")
# print(type(myCars))
# myCars[0]=" Harry ford" # This will throw error because tuple is unchangeable


myCars = ("Ford", "Maecedes", "Audi")
# del myCars 
# print(len(myCars[0]))


myCarsTemp = List(myCars)
print(myCarsTemp)
myCarsTemp[0] = harry
myCars = tuple(MyCarsTemp)
print(myCars)