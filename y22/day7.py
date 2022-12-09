from __future__ import annotations
import re

class Node():
    is_dir: bool = False
    name: str = ""
    size: int = 0
    parent: Node = None
    childs: list(Node) = list

    def __init__(self, is_dir: bool, name: str, parent: Node, size: int = 0):
        self.is_dir = is_dir
        self.name = name
        self.parent = parent
        self.size = size
        self.childs = list()

    def __str__(self):
        if (self.is_dir):
            return self.name + " (dir)"
        else:
            return self.name + " (file, size=" + str(self.size) + ")"

    def add(self, child: Node):
        self.childs.append(child)

    def get(self, name: str):
        for ch in self.childs:
            if (ch.name == name):
                return ch
        return None

    def contains(self, name: str):
        for ch in self.childs:
            if (ch.name == name):
                return True
        return False

    def get_size(self):
        total: int = 0
        if (self.is_dir):
            for ch in self.childs:
                total += ch.get_size()
        else:
            total = self.size
        return total

    def filter(self, dirs: list):
        if (self.is_dir):
            dirs.append(self)
        for ch in self.childs:
            if (ch.is_dir):
                ch.filter(dirs)
        return dirs


cols: int = 0


def walk(n: Node, c: int):
    print(" " * c, n)
    if (n.is_dir):
        for ch in n.childs:
            walk(ch, c + 2)


top = Node(True, "/", None)
current = top

with open("day7.dat") as file:
    lines = file.read().splitlines()
    index: int = 0
    while (index < len(lines)):
        line = lines[index].lstrip()
        if (line.lstrip().startswith("$")):
            found = re.match("\$ (cd|ls).?(.*)", line)
            if (found):
                # print(found.groups())
                if (found.group(1) == "cd"):
                    if (found.group(2) == "/"):
                        current = top
                    elif (found.group(2) == ".."):
                        current = current.parent
                    else:
                        current = current.get(found.group(2))
                elif (found.group(1) == "ls"):
                    while (True):
                        if (index + 1 >= len(lines)):
                            break
                        line = lines[index + 1].lstrip()
                        if (line.startswith("$")):
                            break
                        elif (line.startswith("dir")):
                            child = Node(True, line.split(" ")[1], current)
                        else:
                            child = Node(False, line.split(" ")[1], current, int(line.split(" ")[0]))
                        current.add(child)
                        index += 1
        index += 1

# walk(top, 0)

dirs = list()
dirs = top.filter(dirs)

size1: int = sum(int(d.get_size()) for d in dirs if d.get_size() < 100000)

free = 70000000 - top.get_size()
needed = 30000000 - free

size2: int = 999999999999999999
for d in dirs:
    size = d.get_size()
    if (size2 > size and size > needed):
        size2 = size

print(
    "Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?")
print(" Answer:", size1)

print(
    "Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?")
print(" Answer:", size2)
