# 5052

import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]

        curr_node.data = True

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                return True
            curr_node = curr_node.children[char]

            if curr_node.data:
                return False

        return True


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list()
        for _ in range(n):
            temp = input().rstrip()
            arr.append((len(temp), temp))

        arr.sort()

        data = Trie()

        for _, number in arr:
            if data.search(number) == False:
                print('NO')
                break
            data.insert(number)
        else:
            print('YES')
