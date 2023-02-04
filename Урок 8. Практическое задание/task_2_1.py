"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


class Node:
    def __init__(self, value):
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        self.value = value

    def print(self):
        res = ''
        if self.left_child or self.right_child:
            res = f'{res}/  \\\n'
        if self.left_child:
            res = f'{res}{self.left_child.value} '
        else:
            res = f'{res} '
        if self.right_child:
            res = f'{res} {self.right_child.value}'
        return res.rstrip()


class BinaryTree:
    def __init__(self):
        # корень
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left_child is not None:
                self._insert(value, node.left_child)
            else:
                node.left_child = Node(value)
        else:
            if node.right_child is not None:
                self._insert(value, node.right_child)
            else:
                node.right_child = Node(value)

    def find_val(self, val):
        if self.root.value is not None:
            return self._find_val(val, self.root)
        return None

    def _find_val(self, val, node):
        if node.value == val:
            return node
        elif val < node.value and node.left_child is not None:
            return self._find_val(val, node.left_child)
        elif val > node.value and node.right_child is not None:
            return self._find_val(val, node.right_child)


def str_sum(s1, s2: str):
    lst1 = s1.split('\n')
    lst2 = s2.split('\n')
    n = max(len(lst1), len(lst2))
    for _ in range(n-len(lst1)):
        lst1.append('')
    for _ in range(n-len(lst2)):
        lst2.append('')
    lst = []
    for i in range(n):
        space = ' ' * n
        lst.insert(0, f'{lst1.pop()}{space}{lst2.pop()}')
    return '\n'.join(lst)

tree = BinaryTree()
tree.insert(9)
tree.insert(40)
tree.insert(12)
tree.insert(7)
tree.insert(5)
tree.insert(8)
tree.insert(41)

print('   ', tree.root.value)
print(str_sum('', tree.root.print()))
print(str_sum(tree.root.left_child.print(), tree.root.right_child.print()))

print()
print(tree.find_val(6))
print(tree.find_val(7))
