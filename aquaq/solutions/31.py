import re

with open("./input/31.txt") as f:
    text = f.read()

faces = {
    "F": [1, 1, 1, 1, 1, 1, 1, 1, 1],
    "U": [2, 2, 2, 2, 2, 2, 2, 2, 2],
    "L": [3, 3, 3, 3, 3, 3, 3, 3, 3],
    "R": [4, 4, 4, 4, 4, 4, 4, 4, 4],
    "D": [5, 5, 5, 5, 5, 5, 5, 5, 5],
    "B": [6, 6, 6, 6, 6, 6, 6, 6, 6],
}


def rotate_face_cw(face: list[int]) -> list[int]:
    return [
        face[6],
        face[3],
        face[0],
        face[7],
        face[4],
        face[1],
        face[8],
        face[5],
        face[2],
    ]


def rotate_face_ccw(face: list[int]) -> list[int]:
    return [
        face[2],
        face[5],
        face[8],
        face[1],
        face[4],
        face[7],
        face[0],
        face[3],
        face[6],
    ]


def move_u(ccw: bool = False) -> None:
    if ccw:
        faces["U"] = rotate_face_ccw(faces["U"])
        temp = [faces["F"][0], faces["F"][1], faces["F"][2]]
        faces["F"][0], faces["F"][1], faces["F"][2] = (
            faces["L"][0],
            faces["L"][1],
            faces["L"][2],
        )
        faces["L"][0], faces["L"][1], faces["L"][2] = (
            faces["B"][0],
            faces["B"][1],
            faces["B"][2],
        )
        faces["B"][0], faces["B"][1], faces["B"][2] = (
            faces["R"][0],
            faces["R"][1],
            faces["R"][2],
        )
        faces["R"][0], faces["R"][1], faces["R"][2] = temp[0], temp[1], temp[2]
    else:
        faces["U"] = rotate_face_cw(faces["U"])
        temp = [faces["F"][0], faces["F"][1], faces["F"][2]]
        faces["F"][0], faces["F"][1], faces["F"][2] = (
            faces["R"][0],
            faces["R"][1],
            faces["R"][2],
        )
        faces["R"][0], faces["R"][1], faces["R"][2] = (
            faces["B"][0],
            faces["B"][1],
            faces["B"][2],
        )
        faces["B"][0], faces["B"][1], faces["B"][2] = (
            faces["L"][0],
            faces["L"][1],
            faces["L"][2],
        )
        faces["L"][0], faces["L"][1], faces["L"][2] = temp[0], temp[1], temp[2]


def move_l(ccw: bool = False) -> None:
    if ccw:
        faces["L"] = rotate_face_ccw(faces["L"])
        temp = [faces["F"][0], faces["F"][3], faces["F"][6]]
        faces["F"][0], faces["F"][3], faces["F"][6] = (
            faces["D"][0],
            faces["D"][3],
            faces["D"][6],
        )
        faces["D"][0], faces["D"][3], faces["D"][6] = (
            faces["B"][8],
            faces["B"][5],
            faces["B"][2],
        )
        faces["B"][8], faces["B"][5], faces["B"][2] = (
            faces["U"][0],
            faces["U"][3],
            faces["U"][6],
        )
        faces["U"][0], faces["U"][3], faces["U"][6] = temp[0], temp[1], temp[2]
    else:
        faces["L"] = rotate_face_cw(faces["L"])
        temp = [faces["F"][0], faces["F"][3], faces["F"][6]]
        faces["F"][0], faces["F"][3], faces["F"][6] = (
            faces["U"][0],
            faces["U"][3],
            faces["U"][6],
        )
        faces["U"][0], faces["U"][3], faces["U"][6] = (
            faces["B"][8],
            faces["B"][5],
            faces["B"][2],
        )
        faces["B"][8], faces["B"][5], faces["B"][2] = (
            faces["D"][0],
            faces["D"][3],
            faces["D"][6],
        )
        faces["D"][0], faces["D"][3], faces["D"][6] = temp[0], temp[1], temp[2]


def move_r(ccw: bool = False) -> None:
    if ccw:
        faces["R"] = rotate_face_ccw(faces["R"])
        temp = [faces["F"][2], faces["F"][5], faces["F"][8]]
        faces["F"][2], faces["F"][5], faces["F"][8] = (
            faces["U"][2],
            faces["U"][5],
            faces["U"][8],
        )
        faces["U"][2], faces["U"][5], faces["U"][8] = (
            faces["B"][6],
            faces["B"][3],
            faces["B"][0],
        )
        faces["B"][6], faces["B"][3], faces["B"][0] = (
            faces["D"][2],
            faces["D"][5],
            faces["D"][8],
        )
        faces["D"][2], faces["D"][5], faces["D"][8] = temp[0], temp[1], temp[2]
    else:
        faces["R"] = rotate_face_cw(faces["R"])
        temp = [faces["F"][2], faces["F"][5], faces["F"][8]]
        faces["F"][2], faces["F"][5], faces["F"][8] = (
            faces["D"][2],
            faces["D"][5],
            faces["D"][8],
        )
        faces["D"][2], faces["D"][5], faces["D"][8] = (
            faces["B"][6],
            faces["B"][3],
            faces["B"][0],
        )
        faces["B"][6], faces["B"][3], faces["B"][0] = (
            faces["U"][2],
            faces["U"][5],
            faces["U"][8],
        )
        faces["U"][2], faces["U"][5], faces["U"][8] = temp[0], temp[1], temp[2]


def move_b(ccw: bool = False) -> None:
    if ccw:
        faces["B"] = rotate_face_ccw(faces["B"])
        temp = [faces["U"][0], faces["U"][1], faces["U"][2]]
        faces["U"][0], faces["U"][1], faces["U"][2] = (
            faces["L"][6],
            faces["L"][3],
            faces["L"][0],
        )
        faces["L"][6], faces["L"][3], faces["L"][0] = (
            faces["D"][8],
            faces["D"][7],
            faces["D"][6],
        )
        faces["D"][8], faces["D"][7], faces["D"][6] = (
            faces["R"][2],
            faces["R"][5],
            faces["R"][8],
        )
        faces["R"][2], faces["R"][5], faces["R"][8] = temp[0], temp[1], temp[2]
    else:
        faces["B"] = rotate_face_cw(faces["B"])
        temp = [faces["U"][0], faces["U"][1], faces["U"][2]]
        faces["U"][0], faces["U"][1], faces["U"][2] = (
            faces["R"][2],
            faces["R"][5],
            faces["R"][8],
        )
        faces["R"][2], faces["R"][5], faces["R"][8] = (
            faces["D"][8],
            faces["D"][7],
            faces["D"][6],
        )
        faces["D"][8], faces["D"][7], faces["D"][6] = (
            faces["L"][6],
            faces["L"][3],
            faces["L"][0],
        )
        faces["L"][6], faces["L"][3], faces["L"][0] = temp[0], temp[1], temp[2]


def move_d(ccw: bool = False) -> None:
    if ccw:
        faces["D"] = rotate_face_ccw(faces["D"])
        temp = [faces["F"][6], faces["F"][7], faces["F"][8]]
        faces["F"][6], faces["F"][7], faces["F"][8] = (
            faces["R"][6],
            faces["R"][7],
            faces["R"][8],
        )
        faces["R"][6], faces["R"][7], faces["R"][8] = (
            faces["B"][6],
            faces["B"][7],
            faces["B"][8],
        )
        faces["B"][6], faces["B"][7], faces["B"][8] = (
            faces["L"][6],
            faces["L"][7],
            faces["L"][8],
        )
        faces["L"][6], faces["L"][7], faces["L"][8] = temp[0], temp[1], temp[2]
    else:
        faces["D"] = rotate_face_cw(faces["D"])
        temp = [faces["F"][6], faces["F"][7], faces["F"][8]]
        faces["F"][6], faces["F"][7], faces["F"][8] = (
            faces["L"][6],
            faces["L"][7],
            faces["L"][8],
        )
        faces["L"][6], faces["L"][7], faces["L"][8] = (
            faces["B"][6],
            faces["B"][7],
            faces["B"][8],
        )
        faces["B"][6], faces["B"][7], faces["B"][8] = (
            faces["R"][6],
            faces["R"][7],
            faces["R"][8],
        )
        faces["R"][6], faces["R"][7], faces["R"][8] = temp[0], temp[1], temp[2]


def move_f(ccw: bool = False) -> None:
    if ccw:
        faces["F"] = rotate_face_ccw(faces["F"])
        temp = [faces["U"][6], faces["U"][7], faces["U"][8]]
        faces["U"][6], faces["U"][7], faces["U"][8] = (
            faces["R"][0],
            faces["R"][3],
            faces["R"][6],
        )
        faces["R"][0], faces["R"][3], faces["R"][6] = (
            faces["D"][2],
            faces["D"][1],
            faces["D"][0],
        )
        faces["D"][2], faces["D"][1], faces["D"][0] = (
            faces["L"][8],
            faces["L"][5],
            faces["L"][2],
        )
        faces["L"][8], faces["L"][5], faces["L"][2] = temp[0], temp[1], temp[2]
    else:
        faces["F"] = rotate_face_cw(faces["F"])
        temp = [faces["U"][6], faces["U"][7], faces["U"][8]]
        faces["U"][6], faces["U"][7], faces["U"][8] = (
            faces["L"][8],
            faces["L"][5],
            faces["L"][2],
        )
        faces["L"][8], faces["L"][5], faces["L"][2] = (
            faces["D"][2],
            faces["D"][1],
            faces["D"][0],
        )
        faces["D"][2], faces["D"][1], faces["D"][0] = (
            faces["R"][0],
            faces["R"][3],
            faces["R"][6],
        )
        faces["R"][0], faces["R"][3], faces["R"][6] = temp[0], temp[1], temp[2]


moves = {"U": move_u, "D": move_d, "F": move_f, "B": move_b, "L": move_l, "R": move_r}

for face, *counter in re.findall(r".'?", text.strip()):
    cc = bool(counter)
    moves[face](cc)

answer = 1
for val in faces["F"]:
    answer *= val

print(answer)
