"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.

"""
from collections import Counter, deque


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'0{self.left},1{self.right}'


class Huffman:

    def get_count(self, s):
        return deque(sorted(Counter(s).items(), key=lambda x: x[1]))

    def nodes_dict(self, dq):
        if len(dq) != 1:
            while len(dq) > 1:
                left = dq.popleft()
                right = dq.popleft()
                weigth = left[1] + right[1]
                left, right = left[0], right[0]
                node = Node(left, right)
                for i, el in enumerate(dq):
                    if weigth <= el[1]:
                        dq.insert(i, (node, weigth))
                        break
                    else:
                        continue
                else:
                    dq.append((node, weigth))
        else:
            left = dq.popleft()
            weigth = left[1]
            node = Node(left[0], None)
            dq.append((node, weigth))
        return dq[0][0]

    def huff_code_table(self, node, path=''):
        if not isinstance(node, Node):
            self.code_table.setdefault(node, path)
        else:
            self.huff_code_table(node.left, f'{path}0')
            self.huff_code_table(node.right, f'{path}1')

    def compress(self, s):
        self.nod_dict = self.nodes_dict(self.get_count(s))
        self.code_table = {}
        self.huff_code_table(self.nod_dict)
        res = ''
        for c in s:
            res = f'{res} {self.code_table[c]}'
        return res

    def decompress(self, s, code_table):
        code_table = dict(zip(code_table.values(), code_table.keys()))
        lst = s.split()
        res = ''
        for el in lst:
            res = f'{res}{code_table[el]}'
        return res


if __name__ == "__main__":
    s = "beep boop beer!"
    hf = Huffman()
    compressed = hf.compress(s)
    code_table = hf.code_table
    print(compressed)
    print(hf.decompress(compressed, code_table))
    print(code_table)

"""
beep boop beer!

 00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
 
{'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
"""
