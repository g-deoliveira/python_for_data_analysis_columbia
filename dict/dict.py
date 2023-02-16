my_dict = {}

my_dict[5]
my_dict["cat"]
my_dict[(1, 2)]
my_dict[("cat", "new york", 1)]

my_dict[5] = [1,2,3,4,5,"cat", "dog"]
my_dict["cat"] = 23
my_dict[(1, 2)] = "a string"
my_dict[("cat", "new york", 1)] = ("tuple", "hello", "world")

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

