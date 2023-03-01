thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
n = thisdict.keys()


# return the key in dict
print(n)


# accessing the dict
print(thisdict["brand"])



car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)

# add new item in list
car["color"] ="white"
print(car)

#gte the value in dict
c = car.values()
print(c)

#change the item from the list
car["color"] = "red"
print(car)

#get the item from the dict
v= car.items()
print(v)

#check the item peresent in the dict
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in car:
  print("yes ,'model' is in dict")
else:
  print("model is not in the dict")

#how to change the value in dict
car["year"] =2011
print(car)

#update the dict
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict.update({"year":2020})
print(dict)

#add item in the dict
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
