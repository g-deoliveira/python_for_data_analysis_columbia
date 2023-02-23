my_dict = {}

my_dict[5] = [1,2,3,4,5,"cat", "dog"]
my_dict["cat"] = 23
my_dict[(1, 2)] = "a string"
my_dict[("cat", 1)] = ("hello", "world")

my_dict[5]          # the key is an integer
my_dict["cat"]      # the key is a string
my_dict[(1, 2)]     # the key is a tuple
my_dict[("cat", 1)] # another tuple

assert my_dict[5] == [1,2,3,4,5,"cat", "dog"]
assert my_dict["cat"] == 23
assert my_dict[(1, 2)] == "a string"
assert my_dict[("cat", 1)] == ("hello", "world")


singer = {
    "first_name": "Tina",
    "last_name": "Turner",
    "grammy_awards": {
        "won": 8,
        "nominations": 25
    }
}

singer = dict(
    first_name="Tina",
    last_name="Turner",
    grammy_awards=dict(
        won=8,
        nominations=25
    )
)

# access
assert singer["first_name"] == "Tina"
assert singer["last_name"] == "Turner"

# add new item
singer["birth_year"] = 1039

# update item
singer["birth_year"] = 1939

# nested dictionaries
assert singer["grammy_awards"]["won"] == 8

# membership
assert "birth_year" in singer
assert "birth_month" not in singer

# length
assert len(singer) == 4
assert len(singer["grammy_awards"]) == 2

assert singer == \
{
    "first_name": "Tina",
    "last_name": "Turner",
    "grammy_awards": {
        "won": 8,
        "nominations": 25
    },
    "birth_year": 1939
}


if "birth_year" in singer:
    print(singer["birth_year"])

if "birth_month" in singer:
    print(singer["birth_month"])

singer[0]
