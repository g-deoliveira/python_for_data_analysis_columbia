from typing import Any, Optional

class Dataset:

    def __init__(self):
        """
        Initialize with an empty list.
        """
        self.data = []

    def add(self, input: Any) -> None:
        """
        Add an element to the dataset
        """
        self.data.append(input)

    def count(self) -> int:
        """
        Return the length of the dataset
        """
        return len(self.data)

    def _is_empty(self) -> bool:
        return self.count() == 0

    def _check_index(self, index: int) -> bool:
        """
        Raise a ValueError if the index is invalid
        """
        if abs(index) > self.count():
            message = f"Out of bounds error index {index} > {self.count()}"
            raise ValueError(message)

    def display(self):
        for i, item in enumerate(self.data):
            print(f"\t{i:2d}: {item}")

    def get(self, index: int) -> Any:
        """
        Return the element at the provided index.
        """
        self._check_index(index)
        return self.data[index]

    def pop(self, index: Optional[int] = None) -> Any:
        """
        Remove and return the last element if index is not specified,
        otherwise return the element at the provided index.

        If the dataset is empty, return None.
        """
        if self._is_empty():
            return None
        if index:
            self._check_index(index)
            return self.data.pop(index)
        return self.data.pop()


dataset = Dataset()
assert dataset.count() == 0

dataset.add(11)
assert dataset.data == [11]
assert dataset.count() == 1

dataset.add(22)
dataset.add(33)
assert dataset.data == [11, 22, 33]

assert dataset.get(1) == 22
assert dataset.data == [11, 22, 33]

assert dataset.pop(1) == 22
assert dataset.data == [11, 33]

assert dataset.pop() == 33
assert dataset.data == [11]

assert dataset.pop() == 11
assert dataset.data == []

assert dataset.pop() is None
assert dataset.data == []

