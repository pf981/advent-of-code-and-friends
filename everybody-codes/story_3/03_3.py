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


def get_bond(socket: tuple[str, str], plug: tuple[str, str]) -> int:
    # 0: None, 1: Weak, 2: Strong
    return sum(a == b for a, b in zip(socket, plug))


def place(root: Node | None) -> bool:
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
        bumped_right = True

    # Right empty, any bond
    if not root.right and get_bond(root.right_socket, carry.plug):
        root.right = carry
        return True

    if not bumped_right and place(root.right):
        return True

    return False


def get_checksum(root: Node) -> int:
    order = []

    def traverse(node):
        if not node:
            return

        traverse(node.left)
        order.append(node.id_)
        traverse(node.right)

    traverse(root)
    return sum(i * id_ for i, id_ in enumerate(order, 1))


with open("./story_3/input/everybody_codes_e3_q03_p3.txt") as f:
    lines = f.read().splitlines()


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
    if not root:
        root = node
    else:
        carry = node
        place(root)


answer3 = get_checksum(root)
print(answer3)


# def get_data(root: Node) -> list[str]:
#     result = []

#     def traverse(node):
#         if not node:
#             return

#         traverse(node.left)
#         result.append(node.data)
#         traverse(node.right)

#     traverse(root)
#     return "\n".join(result)


# with open("./story_3/input/e3q03p3_out.txt", "w") as f:
#     f.write(get_data(root))
