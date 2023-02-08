dangerous_animals = [
    "crocodile",
    "lion",
    "snake",
]
cute_animals = [
    "dog",
    "cat",
]

animals = [
    "dog",
    "cat",
    "lion",
    "rabbit",
]

for animal in animals:
    if animal in dangerous_animals:
        print(f"Skipping {animal}")
        continue

    if animal in cute_animals:
        print(f"Yaaay! {animal}")
    else:
        print(f"oh no... {animal}")