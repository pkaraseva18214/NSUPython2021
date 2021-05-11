class Vector(object):
    def __init__(self, *args):
        self.values = args

    def scalar_prod(self, vector):
        if not isinstance(vector, Vector):
            raise ValueError('The dot product requires another vector')
        return sum(a * b for a, b in zip(self, vector))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.scalar_prod(other)
        elif isinstance(other, (int, float)):
            product = tuple(a * other for a in self)
            return self.__class__(*product)
        else:
            raise ValueError("Multiplication with type {} not supported".format(type(other)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if isinstance(other, Vector):
            added = tuple(a + b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            added = tuple(a + other for a in self)
        else:
            raise ValueError(f"Addition with type {type(other)} not supported")

        return self.__class__(*added)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            subbed = tuple(a - b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            subbed = tuple(a - other for a in self)
        else:
            raise ValueError(f"Subtraction with type {type(other)} not supported")

        return self.__class__(*subbed)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __str__(self):
        return str(self.values)


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1 + v2)
print(v1 * v2)
print(v1 * 4)
print(10 * v2)
print(v2 - v1)
