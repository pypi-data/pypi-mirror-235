import math

I = complex(0, 1)

class Matrix:
    def __init__(self, l: list[list[complex]]=[]) -> None:
            self.__m = l
            if l == []:
                  self.__m = [[0, 0], [0, 0]]
            self.__size = (len(self.__m), len(self.__m[0]))
    
    def __mul__(self, __value: "Matrix") -> "Matrix":
        l: list[list[complex]] = []
        for i in range(self.__size[0]*__value.__size[0]):
            l.append([0]*(self.__size[1]*__value.__size[1]))
        
        for i in range(self.__size[0]):
            for j in range(self.__size[1]):
                for x in range(__value.__size[0]):
                    for y in range(__value.__size[1]):
                        pos = (i*__value.__size[0]+x, j*__value.__size[1]+y)
                        l[pos[0]][pos[1]] = self.__m[i][j]*__value.__m[x][y]
        
        return Matrix(l)
    
    def __apply(self, x: list[complex]) -> list[complex]:
        assert(self.__size[1] == len(x))

        y: list[complex] = [0]*self.__size[0]
        for i in range(self.__size[0]):
            for j in range(self.__size[1]):
                y[i] += self.__m[i][j]*x[j]
        return y
    
    def __str__(self) -> str:
        return str(self.__m)
    
    @staticmethod
    def I() -> "Matrix":
        return Matrix([
            [1, 0],
            [0, 1]
        ])
    
    @staticmethod
    def H() -> "Matrix":
        s = 1/math.sqrt(2)
        return Matrix([
            [s, s],
            [s, -s]
        ])

    @staticmethod
    def X() -> "Matrix":
        return Matrix([
            [0, 1],
            [1, 0]
        ])

    @staticmethod
    def Y() -> "Matrix":
        return Matrix([
            [0, -I],
            [I, 0]
        ])

    @staticmethod
    def Z() -> "Matrix":
        return Matrix([
            [1, 0],
            [0, -1]
        ])
    
    @staticmethod
    def S() -> "Matrix":
        return Matrix([
            [1, 0],
            [0, I]
        ])

    @staticmethod
    def T() -> "Matrix":
        s = math.e**(I*math.pi/4)
        return Matrix([
            [1, 0],
            [0, s]
        ])
    
    @staticmethod
    def Rx(phi: float) -> "Matrix":
        c = math.cos(phi/2)
        s = math.sin(phi/2)
        return Matrix([
            [c, -I*s],
            [-I*s, c]
        ])
    
    @staticmethod
    def Ry(phi: float) -> "Matrix":
        c = math.cos(phi/2)
        s = math.sin(phi/2)
        return Matrix([
            [c, -s],
            [s, c]
        ])
    
    @staticmethod
    def Rz(phi: float) -> "Matrix":
        s = math.e**(I*phi/2)
        return Matrix([
            [1/s, 0],
            [0, s]
        ])
    
    @staticmethod
    def R1(phi: float) -> "Matrix":
        s = math.e**(I*phi)
        return Matrix([
            [1, 0],
            [0, s]
        ])

    @staticmethod
    def CNOT() -> "Matrix":
        return Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ])
    
    @staticmethod
    def SWAP() -> "Matrix":
        return Matrix([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def Cu(u: "Matrix") -> "Matrix":
        assert(u.size == (2, 2))
        l = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, u[0][0], u[0][1]],
            [0, 0, u[1][0], u[1][1]]
        ]

if __name__=="__main__":
    m1 = Matrix([[1]])
    m2 = Matrix([[1, 1], [0, 1]])

    print(m1*m2)