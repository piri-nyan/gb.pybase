print("Custom matrix class")

class Matrix():
    def __init__(self, *lists) -> None:
        self.lists = lists

    def __str__(self) -> str:
        return "\n".join(" ".join(str(x) for x in lst) for lst in self.lists)

    def __add__(self, other):
        res = []
        if len(self.lists)!=len(other.lists):
            print("Matrices size mismatch")
        else:
            for i in range(0, len(self.lists)):
                if len(self.lists[i])!=len(other.lists[i]):
                    print("Matrices size mismatch")
                else:
                    tmp = []
                    for j in range(0, len(self.lists[i])):
                        tmp.append(self.lists[i][j]+other.lists[i][j])
                    res.append(tmp)
            return Matrix(*res)

mx1 = Matrix([1, 2, 5, 7], [3, 5, 7, 2], [2, 6, 8, 2])
mx2 = Matrix([1, 2, 5, 7], [3, 5, 7, 2], [2, 6, 8, 2])
print(mx1+mx2+mx1+mx2)