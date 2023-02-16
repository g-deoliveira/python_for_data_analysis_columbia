
cats = {
    "Kingdom": "Animalia",
    "Phylum": "Chordata",
    "Class": "Mammalia",
    "Order": "Carnivora",
    "Suborder":	"Feliformia",
    "Family": "Felidae",
    "Subfamily": "Felinae",
    "Genus": "Felis",
}

assert cats["Kingdom"] == "Animalia"
assert cats.get("Kingdom") == "Animalia"

# query for non-existant key
assert cats.get("xya") == None

# query for non-existant key with default
assert cats.get("xya", 0) == 0

# update
D = {"x":  1, "y": 10}
E = {"x": 20, "z":  0}
D.update(E)
assert D["x"] == 20
assert D["y"] == 10
assert D["z"] == 0

