import z3


def z3_zero_if_below_threshold(value, threshold):
    return z3.If(value < threshold, 0, value)


o = z3.Optimize()


n_free = len(grid_text.splitlines()[0].split())
inputs_z3 = []
for i in range(n_free):
    inputs_z3.append(z3.Int(f"inputs_{i}"))
    o.add(inputs_z3[-1] >= 0)
    o.add(inputs_z3[-1] <= 1)

# nodes_z3 = {}
# for node, thickness in nodes.items():
#     nodes_z3[node] = z3.Int(f"node_{node}")
#     o.add(total == s1 + s2)

nodes = copy.deepcopy(nodes_o)  # Unchanged
nodes_incoming_z3 = collections.defaultdict(
    int
)  # node -> [(thickness1, z3_1), (thickness2, z3_2), ...] where incoming is sum of products
edges = copy.deepcopy(edges_o)  # Unchanged

todo = []  # nodes
for (to, thickness), input_z3 in zip(edges[None], inputs_z3):  # Free branches
    # nodes_incoming[to] += thickness # Old
    # nodes_incoming_z3[to].append((thickness, input_z3))
    nodes_incoming_z3[to] = z3.Sum(nodes_incoming_z3[to], thickness * input_z3)

    print(f"Done free brnach {to=} {thickness=}")

# Note: You could just have said todo = [None]
todo = sorted(nodes)
for node in todo:
    # if (
    #     nodes_incoming[node] < nodes[node]
    # ):  # Incoming does not exceed thickness, so don't propogate
    #     continue

    for to, thickness in edges[node]:
        # nodes_incoming[to] += nodes_incoming[node] * thickness # Old
        nodes_incoming_z3[to] = z3.Sum(
            nodes_incoming_z3[to],
            z3_zero_if_below_threshold(nodes_incoming_z3[node], nodes[node])
            * thickness,
        )

        # .append(
        #     z3_zero_if_below_threshold(
        #         z3.Sum(a * b for a, b in nodes_incoming_z3[node]) * thickness,
        #         nodes[node],
        #     )
        # )  # nodes_incoming[node] * thickness

    print(f"Done node {node=}")
    # Beware appending while iterating

# print(f"{nodes_incoming=}")
# last_node = max(nodes)
# if nodes_incoming[last_node] < nodes[last_node]:
#     return 0
# return nodes_incoming[last_node]

outputs = {}
for node in nodes:
    outputs[node] = z3.Int(f"outputs_{node}")
    o.add(
        outputs[node]
        == z3_zero_if_below_threshold(nodes_incoming_z3[node], nodes[node])
    )

last_node = max(nodes)
o.maximize(outputs[last_node])

o.check()
answer = o.model()[outputs[last_node]].as_long()
print(answer)
# 11186
