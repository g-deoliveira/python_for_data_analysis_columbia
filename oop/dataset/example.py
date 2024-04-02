from dataset import Dataset

dataset = Dataset()

dataset.add(111)
assert dataset.count() == 1
assert dataset.get(0) == 111

dataset.add(222)
assert dataset.count() == 2
assert dataset.get(0) == 111
assert dataset.get(1) == 222

dataset.add(333)

dataset.display()
