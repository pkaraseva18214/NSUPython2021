def join_lines(*args):
    return Table([*args])


def join_columns(*args):
    if len(args) == 0:
        return Table([])
    matrix = []
    for i in range(len(args[0])):
        matrix.append([])
    for j in range(len(args[0])):
        for i in range(len(args)):
            matrix[j].append(args[i][j])
    return Table(matrix)


class Table:

    def __init__(self, matr):
        self.matr = matr

    def tail(self, n):
        return self.__class__(self.matr[-n:][:])

    def head(self, n):
        return self.__class__(self.matr[:n][:])

    def column_ids(self, *indexes):
        return join_columns(*[self[:, i] for i in indexes])

    def __str__(self):
        return str(self.matr)

    def __getitem__(self, item):
        try:
            if type(item) != tuple:
                return self.matr[item]
            lines = self.matr[item[0]]
            if len(lines) == 0:
                return lines[item[1]]
            if type(lines[0]) != list:
                if type(item[1]) == slice:
                    return lines[item[1]]
                else:
                    return Column(lines[item[1]])
            ans = list(map(lambda x: x[item[1]], lines))
            return ans if type(item[1]) == slice else Column(ans)
        except IndexError:
            raise IndexError("Matrix index out of bound")


class Column(list):

    def __init__(self, *args):
        if len(args) != 0:
            if isinstance(args[0], list):
                if len(args[0]) != 0:
                    if isinstance(args[0][0], list):
                        raise Exception("1d lists accepted only")

                    if len(args) == 1:
                        super().__init__(args[0])
                    else:
                        raise Exception("Only one list is accepted")
            else:
                super().__init__(args)
        else:
            super().__init__(args)

    def __str__(self):
        return f"Column({super().__str__()})"


t = Table(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
)

print("Head:")
print(t.head(2))
print("Tail:")
print(t.tail(2))
print("Column example:")
print(Column(1, 2, 3))
print("Column from table:")
print(t[1:, 1])
print("Join lines:")
print(join_lines(t[0], t[1]))
print("Join columns:")
print(join_columns(Column(1, 2, 3), Column(4, 5, 6)))
print("Construct a table by another table ids:")
print(t.column_ids(1, 2))
