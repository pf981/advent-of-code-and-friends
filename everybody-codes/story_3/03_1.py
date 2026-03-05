from dataclasses import dataclass


@dataclass
class Node:
    id_: int
    plug: str
    left_socket: str
    right_socket: str
    data: str
    left: Node | None = None
    right: Node | None = None


with open("./story_3/input/everybody_codes_e3_q03_p1.txt") as f:
    lines = f.read().splitlines()
# lines = """id=1, plug=BLUE HEXAGON, leftSocket=GREEN CIRCLE, rightSocket=BLUE PENTAGON, data=?
# id=2, plug=GREEN CIRCLE, leftSocket=BLUE HEXAGON, rightSocket=BLUE CIRCLE, data=?
# id=3, plug=BLUE PENTAGON, leftSocket=BLUE CIRCLE, rightSocket=BLUE CIRCLE, data=?
# id=4, plug=BLUE CIRCLE, leftSocket=RED HEXAGON, rightSocket=BLUE HEXAGON, data=?
# id=5, plug=RED HEXAGON, leftSocket=GREEN CIRCLE, rightSocket=RED HEXAGON, data=?""".splitlines()


def place(node: Node, root: Node | None) -> Node | None:
    if not root:
        return False

    if not root.left and root.left_socket == node.plug:
        root.left = node
        return True

    if place(node, root.left):
        return True

    if not root.right and root.right_socket == node.plug:
        root.right = node
        return True

    if place(node, root.right):
        return True

    return False


root = None
for line in lines:
    id_, plug, left_socket, right_socket, data = [
        part.split("=")[1] for part in line.split(", ")
    ]
    node = Node(int(id_), plug, left_socket, right_socket, data)
    # print(node)
    if not root:
        root = node
    else:
        place(node, root)

result = []


def traverse(node):
    if not node:
        return

    traverse(node.left)
    result.append(node.id_)
    traverse(node.right)


traverse(root)

answer1 = 0
for i, id_ in enumerate(result, 1):
    answer1 += i * id_

print(answer1)
