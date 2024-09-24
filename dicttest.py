thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
key_list = list(thisdict.keys())
val_list = list(thisdict.values())
if (1964 in thisdict.values()):
    # print key with val 100
    position = val_list.index(1964)
    print(key_list[position])
 
else:
    print("none")
