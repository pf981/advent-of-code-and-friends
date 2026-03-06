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


def place(node: Node, root: Node | None) -> bool:
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


with open("./story_3/input/everybody_codes_e3_q03_p1.txt") as f:
    lines = f.read().splitlines()


root = None
for line in lines:
    id_, plug, left_socket, right_socket, data = [
        part.split("=")[1] for part in line.split(", ")
    ]
    node = Node(int(id_), plug, left_socket, right_socket, data)
    if not root:
        root = node
    else:
        place(node, root)

answer1 = get_checksum(root)
print(answer1)


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


# with open("./story_3/input/e3q03p1_out.txt", "w") as f:
#     f.write(get_data(root))
