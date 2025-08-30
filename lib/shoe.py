#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size=1):
        self.brand = brand
        self.size = size
        self.condition = "New"

    # brand
    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        if not isinstance(value, str):
            print("brand must be a string")
        else:
            self._brand = value

    brand = property(get_brand, set_brand)

    # size
    def get_size(self):
        return getattr(self, "_size", None)

    def set_size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    size = property(get_size, set_size)

    # behavior
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
