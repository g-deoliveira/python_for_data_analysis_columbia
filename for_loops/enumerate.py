PETS = ["cat", "bird", "dog"]

counter = 0
for pet in PETS:
    print(counter, pet)
    counter += 1

for counter, pet in enumerate(PETS):
    print(counter, pet)