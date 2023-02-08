counter = 0
for pet in ["cat", "bird", "dog"]:
    print(counter, pet)

for counter, pet in enumerate(["cat", "bird", "dog"]):
    print(counter, pet)