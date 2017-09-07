name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "honey badger"]


def make_dict(arr1, arr2):
  new_dict = {}
  longest = arr1
  shortest = arr2
  if len(arr2) > len(arr1):
    longest = arr2
    shortest = arr1
  for i in range(len(shortest)):
    new_dict[longest[i]]=shortest[i]
  print new_dict





make_dict(name,favorite_animal)
