# DICTIONARY ---> collection of pairs { key : value }


capitals = {"USA" : "Washington D.C",
            "India" : "New Delhi", 
            "Italy" : "Rome",
            "Spain" : "Madrid"}

# TO SHOW METHODS OF A DICTIONARY
# print(dir(capitals));
# print(help(capitals));

# .get gives you the value corrispondent to the given key
print(capitals.get("Italy"))

# ADDS A NEW KEY-VALUE PAIR TO THE DICTIONARY
capitals.update({"Germany" : "Berlin"})
print(capitals)

# TO REMOVE A KEY-VALUE PAIR TO THE DICTIONARY
capitals.pop("India")
print(capitals)

# TO REMOVE THE LATEST ELEMENT IN THE DICTIONARY
# capitals.popitem()
# print(capitals)

# TO REMOVE ALL ELEMENTS FROM THE DICTIONARY
# capitals.clear()
# print(capitals)

# TO GET ALL THE KEYS IN THE DICTIONARY
# keys = capitals.keys
# print(keys)

for key in capitals.keys():
    print(key)

for key, value in capitals.items():
    print(f"{key} : {value}")