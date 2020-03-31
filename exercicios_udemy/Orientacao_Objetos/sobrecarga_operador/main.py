"""
No Python. o coportamento dos operadores é definido por métodos especiais,
vamos alterar o comportamento de operadores com classes definidas pelo usuário
"""


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        area = self.x * self.y
        return area

    def __repr__(self):
        return f'Retangulo :({self.x},{self.y})'

    # método para somar
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    # método para verificar menor que
    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 < a2:
            return True
        return False

    # método para verificar maior que
    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 > a2:
            return True
        return False

    # método para verificar igualdade
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

# O Python não sabe como faz para somar dois objetos do tipo Retangulo, para isso deve ser usado um método 'mágico'


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2
print(r3)
print(r3 > r1)
print(r3 < r1)
print(r1 == r2)
print(r1 == r3)
