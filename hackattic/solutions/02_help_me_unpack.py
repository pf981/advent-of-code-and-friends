import base64
import ctypes

from api import get_problem, submit_solution


class BigEndianDouble(ctypes.BigEndianStructure):
    _fields_ = [
        ("big_endian_double", ctypes.c_double),
    ]


class Struct(ctypes.Structure):
    _fields_ = [
        ("int", ctypes.c_int32),
        ("uint", ctypes.c_uint32),
        ("short", ctypes.c_short),
        ("float", ctypes.c_float),
        ("double", ctypes.c_double),
        ("big_endian_double_container", BigEndianDouble),
    ]


PROBLEM = "help_me_unpack"
problem = get_problem(PROBLEM)

struct = Struct.from_buffer_copy(base64.b64decode(problem["bytes"]))

solution = {
    "int": struct.int,
    "uint": struct.uint,
    "short": struct.short,
    "float": struct.float,
    "double": struct.double,
    "big_endian_double": struct.big_endian_double_container.big_endian_double,
}
result = submit_solution(PROBLEM, solution)
print(result)
