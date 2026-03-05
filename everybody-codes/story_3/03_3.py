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


with open("./story_3/input/everybody_codes_e3_q03_p3.txt") as f:
    lines = f.read().splitlines()
# lines = """id=1, plug=RED TRIANGLE, leftSocket=BLUE TRIANGLE, rightSocket=GREEN TRIANGLE, data=?
# id=2, plug=GREEN TRIANGLE, leftSocket=BLUE CIRCLE, rightSocket=GREEN CIRCLE, data=?
# id=3, plug=BLUE PENTAGON, leftSocket=BLUE CIRCLE, rightSocket=GREEN CIRCLE, data=?
# id=4, plug=RED TRIANGLE, leftSocket=BLUE PENTAGON, rightSocket=GREEN PENTAGON, data=?
# id=5, plug=BLUE TRIANGLE, leftSocket=GREEN CIRCLE, rightSocket=RED CIRCLE, data=?
# id=6, plug=BLUE TRIANGLE, leftSocket=GREEN CIRCLE, rightSocket=RED CIRCLE, data=?""".splitlines()


def get_bond(socket, plug):
    # 0: None, 1: Weak, 2: Strong
    return sum(a == b for a, b in zip(socket, plug))


carry = None


def place(root: Node | None) -> Node | None:
    global carry
    bumped_left = bumped_right = False

    if not root:
        return False

    # Left weak, replace strong
    if root.left and get_bond(root.left_socket, carry.plug) > get_bond(
        root.left_socket, root.left.plug
    ):
        carry2 = root.left
        root.left = carry
        carry = carry2
        # return place(root)
        bumped_left = True

    # Left empty, any bond
    if not root.left and get_bond(root.left_socket, carry.plug):
        root.left = carry
        return True

    if not bumped_left and place(root.left):
        return True

    # Right weak, replace strong
    if root.right and get_bond(root.right_socket, carry.plug) > get_bond(
        root.right_socket, root.right.plug
    ):
        carry2 = root.right
        root.right = carry
        carry = carry2
        # return place(root)

        # This will happen anyway
        # if place(root.right):
        #     return True
        bumped_right = True

    # Right empty, any bond
    if not root.right and get_bond(root.right_socket, carry.plug):
        root.right = carry
        return True

    if not bumped_right and place(root.right):
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
        carry = node
        place(root)

result = []


def traverse(node):
    if not node:
        return

    traverse(node.left)
    result.append(node.id_)
    traverse(node.right)


traverse(root)

answer3 = 0
for i, id_ in enumerate(result, 1):
    answer3 += i * id_

print(answer3)
# 404863
# Your answer length is: correct
# The first character of your answer is: correct

# 407808
# Your answer length is: correct
# The first character of your answer is: correct
