from dataclasses import dataclass


@dataclass
class Node:
    id_: int
    plug: tuple[str, str]
    left_socket: tuple[str, str]
    right_socket: tuple[str, str]
    data: str
    left: Node | None = None
    right: Node | None = None


with open("./story_3/input/everybody_codes_e3_q03_p2.txt") as f:
    lines = f.read().splitlines()

# lines = """id=1, plug=RED TRIANGLE, leftSocket=RED TRIANGLE, rightSocket=RED TRIANGLE, data=?
# id=2, plug=GREEN TRIANGLE, leftSocket=BLUE CIRCLE, rightSocket=GREEN CIRCLE, data=?
# id=3, plug=BLUE PENTAGON, leftSocket=BLUE CIRCLE, rightSocket=GREEN CIRCLE, data=?
# id=4, plug=RED TRIANGLE, leftSocket=BLUE PENTAGON, rightSocket=GREEN PENTAGON, data=?
# id=5, plug=RED PENTAGON, leftSocket=GREEN CIRCLE, rightSocket=GREEN CIRCLE, data=?""".splitlines()


def place(node: Node, root: Node | None) -> Node | None:
    if not root:
        return False

    if not root.left and any(a == b for a, b in zip(root.left_socket, node.plug)):
        root.left = node
        return True

    if place(node, root.left):
        return True

    if not root.right and any(a == b for a, b in zip(root.right_socket, node.plug)):
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
    node = Node(
        int(id_),
        tuple(plug.split()),
        tuple(left_socket.split()),
        tuple(right_socket.split()),
        data,
    )
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

answer2 = 0
for i, id_ in enumerate(result, 1):
    answer2 += i * id_

print(answer2)
