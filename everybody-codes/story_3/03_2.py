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


def get_bond(socket, plug):
    # 0: None, 1: Weak, 2: Strong
    return sum(a == b for a, b in zip(socket, plug))


def place(node: Node, root: Node | None) -> Node | None:
    if not root:
        return False

    if not root.left and get_bond(root.left_socket, node.plug):
        root.left = node
        return True

    if place(node, root.left):
        return True

    if not root.right and get_bond(root.right_socket, node.plug):
        root.right = node
        return True

    if place(node, root.right):
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


with open("./story_3/input/everybody_codes_e3_q03_p2.txt") as f:
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
        place(node, root)

answer2 = get_checksum(root)
print(answer2)


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


# with open("./story_3/input/e3q03p2_out.txt", "w") as f:
#     f.write(get_data(root))
