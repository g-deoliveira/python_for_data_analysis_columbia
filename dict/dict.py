my_dict = {}


my_dict[5] = [1,2,3,4,5,"cat", "dog"]
my_dict["cat"] = 23
my_dict[(1, 2)] = "a string"
my_dict[("cat", "new york", 1)] = ("tuple", "hello", "world")


my_dict[5]
my_dict["cat"]
my_dict[(1, 2)]
my_dict[("cat", "new york", 1)]


tina_turner = {
    "first_name": "Tina",
    "last_name": "Turner",
    "grammy_awards": {
        "won": 8,
        "nominations": 25
    }
}

tina_turner = dict(
    first_name="Tina",
    last_name="Turner",
    grammy_awards=dict(
        won=8,
        nominations=25
    )
)

# indexing
assert tina_turner["first_name"] == "Tina"
# nested dictionaries
assert tina_turner["grammy_awards"]["won"] == 8

# assigning a new key-value pair
tina_turner["birth_year"] = 1039
# oops made a typo, need to update
tina_turner["birth_year"] = 1939

# membership
assert "birth_year" in tina_turner
assert "birth_month" not in tina_turner

# length
assert len(tina_turner) == 4
assert len(tina_turner["grammy_awards"]) == 2
