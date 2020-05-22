dict1 = {
  "rushi": 10,
  "kevin": 20,
  "manan": 194,
  "harsh": 32,
  "parth": 65
}
print("1: To determine if a specified key is present in a dictionary")
if "manan" in dict1:
  print("Yes, 'manan' is one of the keys in the dict1 dictionary")

print("2: To determine how many items (key-value pairs) a dictionary")
print(len(dict1))

print("3: Adding an item to the dictionary ")
dict1["zeel"] = "78"
print(dict1)

print("4: remove the item with the specified key name")
dict1.pop("parth")
print(dict1)

print("5: remove the last inserted item")
dict1.popitem()
print(dict1)

print("6: Make a copy of a dictionary")
dict2 = dict1.copy()
print(dict2)

print("7: Make a copy of a dictionary with the dict()")
dict3 = dict(dict1)
print(dict3)

print("8: hange the value of a specific item")
dict3["rushi"] = 77

print("9:Loop through both keys and values, by using the items() method")
for x, y in dict1.items():
  print(x, y)



print("10: The clear() method empties the dictionary")
dict1.clear()
print(dict1)

