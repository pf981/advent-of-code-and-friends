import base64
import collections
import ctypes
import io
import ipaddress
import itertools
import pathlib
import string

from typing import Callable, Literal

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


PAYLOAD_SEP = "==[ Payload ]===============================================\n\n"
DATA_PATH = pathlib.Path("./data/")


def get_payload(layer: int) -> bytes:
    path = DATA_PATH / f"{layer:>02}.txt"
    with open(path) as f:
        text = f.read()

    payload = text.split(PAYLOAD_SEP)[1].strip()
    return base64.a85decode(payload, adobe=True)


def process(layer: int, decrypt_fn: Callable[[bytes], bytes]) -> None:
    payload = get_payload(layer)
    plaintext = decrypt_fn(payload).decode("utf-8")
    path = DATA_PATH / f"{layer + 1:>02}.txt"

    with open(path, "w", newline="") as f:
        f.write(plaintext)


def layer0(data: bytes) -> bytes:
    """
    This payload has been encoded with Adobe-flavoured ASCII85.
    """
    return data


def layer1(data: bytes) -> bytes:
    """
    Like all the layers, the payload is again encoded with
    Adobe-flavoured ASCII85. After ASCII85 decoding the payload,
    apply the following operations to each byte:

      1. Flip every second bit
      2. Rotate the bits one position to the right
    """
    output = bytearray()
    for byte in data:
        flipped = byte ^ 0b01010101
        rotated = (flipped >> 1) | ((flipped & 1) << 7)
        output.append(rotated)

    return bytes(output)


def layer2(data: bytes) -> bytes:
    """
    For each byte of the payload, the seven most significant
    bits carry data, and the least significant bit is the parity
    bit. Combine the seven data bits from each byte where the
    parity bit is correct, discarding bytes where the parity bit
    is incorrect.

    To determine if the parity bit is correct, first count how
    many '1' bits exist within the seven data bits. If the count
    is odd, the parity bit should be '1'. If the count is even,
    the parity bit should be '0'.
    """
    seven_bits_array = bytearray()
    for byte in data:
        parity_bit = byte & 1
        seven_bits = byte >> 1

        if (seven_bits.bit_count() & 1) != parity_bit:
            continue

        seven_bits_array.append(seven_bits)

    cur_byte = 0
    cur_byte_size = 0
    output = bytearray()
    for seven_bits in seven_bits_array:
        if cur_byte_size == 0:
            cur_byte = seven_bits << 1
            cur_byte_size = 7
            continue

        # Guaranteed to fill byte
        to_take = 8 - cur_byte_size
        cur_byte |= seven_bits >> (7 - to_take)
        output.append(cur_byte & 0b1111111)

        cur_byte_size = 7 - to_take
        cur_byte = (seven_bits & ((1 << cur_byte_size) - 1)) << (to_take + 1)

    assert cur_byte_size == 0

    return bytes(output)


def layer3(data: bytes) -> bytes:
    """
    The payload has been encrypted by XOR'ing each byte with a
    secret, cycling key. The key is 32 bytes of random data,
    which I'm not going to give you. You will need to use your
    hacker skills to discover what the key is, in order to
    decrypt the payload.
    """
    path = DATA_PATH / "03.txt"
    with open(path) as f:
        text = f.read()
    reference_text = text.split(PAYLOAD_SEP)[0].strip()
    reference_counts = collections.Counter(reference_text.encode("utf-8"))
    s = sum(reference_counts.values())
    reference_freqs = {byte: count / s for byte, count in reference_counts.items()}

    all_freqs = []
    for i in range(32):
        freqs = collections.Counter(data[i:1024:32])
        s = sum(freqs.values())
        for byte in freqs:
            freqs[byte] /= s
        all_freqs.append(freqs)

    key = []
    for freqs in all_freqs:
        best = (float("inf"), 0)  # d, k
        for k in range(256):
            new_freqs = collections.Counter()
            for byte, w in freqs.items():
                new_freqs[byte ^ k] = w

            d = 0
            for byte in set(new_freqs.keys()) | set(reference_freqs.keys()):
                if chr(byte) not in string.printable:
                    d = float("inf")
                    break
                freq1 = new_freqs.get(byte, 0)
                freq2 = reference_freqs.get(byte, 0)
                d += abs(freq1 - freq2)
            best = min(best, (d, k))
        key.append(best[1])

    return bytes(byte ^ k for byte, k in zip(data, itertools.cycle(key)))


def layer4(data: bytes) -> bytes:
    """
    The payload for this layer is encoded as a stream of raw
    network data, as if the solution was being received over the
    internet. The data is a series of IPv4 packets with User
    Datagram Protocol (UDP) inside. Extract the payload data
    from inside each packet, and combine them together to form
    the solution.

    Each valid packet of the solution has the following
    properties. Discard packets that do not have all of these
    properties.

     - The packet was sent FROM any port of 10.1.1.10
     - The packet was sent TO port 42069 of 10.1.1.200
     - The IPv4 header checksum is correct
     - The UDP header checksum is correct

    The packets appear in the correct order. No reordering is
    necessary.

    IPv4 Header:
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |Version|  IHL  |Type of Service|          Total Length         |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |         Identification        |Flags|      Fragment Offset    |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |  Time to Live |    Protocol   |         Header Checksum       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                       Source Address                          |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    Destination Address                        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    Options                    |    Padding    |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    UDP Header:
     0      7 8     15 16    23 24    31
    +--------+--------+--------+--------+
    |     Source      |   Destination   |
    |      Port       |      Port       |
    +--------+--------+--------+--------+
    |                 |                 |
    |     Length      |    Checksum     |
    +--------+--------+--------+--------+
    |
    |          data octets ...
    +---------------- ...
    """

    class IPv4Header(ctypes.BigEndianStructure):
        _pack_ = 1
        _fields_ = [
            ("version", ctypes.c_uint8, 4),
            ("ihl", ctypes.c_uint8, 4),
            ("type_of_service", ctypes.c_uint8),
            ("total_length", ctypes.c_uint16),
            ("identification", ctypes.c_uint16),
            ("flags", ctypes.c_uint16, 3),
            ("fragment_offset", ctypes.c_uint16, 13),
            ("time_to_live", ctypes.c_uint8),
            ("protocol", ctypes.c_uint8),
            ("header_checksum", ctypes.c_uint16),
            ("source_address", ctypes.c_uint32),
            ("destination_address", ctypes.c_uint32),
        ]

    class UdpHeader(ctypes.BigEndianStructure):
        _pack_ = 1
        _fields_ = [
            ("source_port", ctypes.c_uint16),
            ("destination_port", ctypes.c_uint16),
            ("length", ctypes.c_uint16),
            ("checksum", ctypes.c_uint16),
        ]

    def read_struct(stream: io.BytesIO, cls):
        size = ctypes.sizeof(cls)
        data = stream.read(size)
        if len(data) != size:
            raise EOFError(f"Expected {size} bytes, got {len(data)}")
        return cls.from_buffer_copy(data)

    def checksum16(data: bytes) -> int:
        if len(data) % 2 == 1:
            data += b"\x00"

        checksum = 0
        for i in range(0, len(data), 2):
            word = int.from_bytes(data[i : i + 2], "big")
            checksum += word
            checksum = (checksum & 0xFFFF) + (checksum >> 16)

        return ~checksum & 0xFFFF

    stream = io.BytesIO(data)
    stream_out = io.BytesIO()

    while stream.tell() < len(stream.getbuffer()):
        ipv4_header = read_struct(stream, IPv4Header)
        udp_header = read_struct(stream, UdpHeader)
        content = stream.read(udp_header.length - ctypes.sizeof(UdpHeader))

        assert ipv4_header.ihl == 5
        assert ipv4_header.total_length == udp_header.length + ctypes.sizeof(IPv4Header)

        if str(ipaddress.IPv4Address(ipv4_header.source_address)) != "10.1.1.10":
            continue
        if str(ipaddress.IPv4Address(ipv4_header.destination_address)) != "10.1.1.200":
            continue
        if udp_header.destination_port != 42069:
            continue

        udp_pseudo_header = b"".join(
            [
                ipv4_header.source_address.to_bytes(4, "big"),
                ipv4_header.destination_address.to_bytes(4, "big"),
                b"\x00",
                ipv4_header.protocol.to_bytes(1, "big"),
                udp_header.length.to_bytes(2, "big"),
            ]
        )
        udp_checksum_data = udp_pseudo_header + bytes(udp_header) + content

        if checksum16(bytes(ipv4_header)) != 0:
            continue
        if checksum16(udp_checksum_data) != 0:
            continue

        stream_out.write(content)

    return stream_out.getvalue()


def layer5(data: bytes) -> bytes:
    """
    The payload is structured like this:

    - First 32 bytes: The 256-bit key encrypting key (KEK).
    - Next 8 bytes: The 64-bit initialization vector (IV) for
    the wrapped key.
    - Next 40 bytes: The wrapped (encrypted) key. When
    decrypted, this will become the 256-bit encryption key.
    - Next 16 bytes: The 128-bit initialization vector (IV) for
    the encrypted payload.
    - All remaining bytes: The encrypted payload.

    The first step is to use the KEK and the 64-bit IV to unwrap
    the wrapped key. The second step is to use the unwrapped key
    and the 128-bit IV to decrypt the rest of the payload.
    """

    def aes_key_unwrap_with_iv(kek: bytes, wrapped: bytes) -> tuple[bytes, int]:
        n = len(wrapped) // 8 - 1

        A = int.from_bytes(wrapped[:8], "big")
        R = [None] + [wrapped[i * 8 : (i + 1) * 8] for i in range(1, n + 1)]

        cipher = Cipher(algorithms.AES(kek), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()

        for j in range(5, -1, -1):
            for i in range(n, 0, -1):
                t = n * j + i
                B = decryptor.update((A ^ t).to_bytes(8, "big") + R[i])
                A = int.from_bytes(B[:8], "big")
                R[i] = B[8:]

        return b"".join(R[1:]), A

    kek = data[:32]
    expected_iv = int.from_bytes(data[32:40], "big")
    wrapped_key = data[40:80]
    payload_iv = data[80:96]
    encrypted_payload = data[96:]

    data_key, got_iv = aes_key_unwrap_with_iv(kek, wrapped_key)
    assert got_iv == expected_iv
    assert len(data_key) == 32

    cipher = Cipher(
        algorithms.AES(data_key), modes.CTR(payload_iv), backend=default_backend()
    )
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(encrypted_payload) + decryptor.finalize()

    return plaintext


def layer6(data_: bytes) -> bytes:
    """
    - 12 registers (see [ Spec: Registers ])
    - a fixed amount of memory (see [ Spec: Memory ])
    - an output stream (see [ Spec: Output ])
    - 13 distinct instructions (see [ Spec: Instruction Set ])

    1. Reads one instruction from memory, at the address stored
    in the `pc` register.

    2. Adds the byte size of the instruction to the `pc`
        register.

    3. Executes the instruction.


    The 8-bit registers are:

    `a`  Accumulation register -- Used to store the result
            of various instructions.

    `b`  Operand register -- This is 'right hand side' of
            various operations.

    `c`  Count/offset register -- Holds an offset or index
            value that is used when reading memory.

    `d`  General purpose register

    `e`  General purpose register

    `f`  Flags register -- Holds the result of the
            comparison instruction (CMP), and is used by
            conditional jump instructions (JEZ, JNZ).

    The 32-bit registers are:

        `la`   General purpose register

        `lb`   General purpose register

        `lc`   General purpose register

        `ld`   General purpose register

        `ptr`  Pointer to memory -- holds a memory address which
                is used by instructions that read or write
                memory.

        `pc`   Program counter -- holds a memory address that
                points to the next instruction to be executed.

    In addition to these 12 registers, there is an 8-bit
    pseudo-register used to read and write memory. This is only
    used by the 8-bit move instructions (MV, MVI).

        `(ptr+c)`  Memory cursor -- Used to access one byte of
                    memory. Using this pseudo-register as the
                    {dst} of a move instruction will write to
                    memory. Using this as the {src} of a move
                    instruction will read from memory. The memory
                    address of the byte to be read/written is the
                    sum of the `ptr` and `c` registers.

    """

    def get_op(pc: int) -> tuple[str, tuple[int, ...], int]:
        opcode = instructions[pc]
        args = ()
        pc += 1
        match opcode:
            case 0xC2:
                op = "ADD"
            case 0xE1:
                op = "APTR"
                args = (instructions[pc],)
                pc += 1
            case 0xC1:
                op = "CMP"
            case 0x01:
                op = "HALT"
            case 0x21:
                op = "JEZ"
                args = (int.from_bytes(instructions[pc : pc + 4], "little"),)
                pc += 4
            case 0x22:
                op = "JNZ"
                args = (int.from_bytes(instructions[pc : pc + 4], "little"),)
                pc += 4
            case 0x02:
                op = "OUT"
            case 0xC3:
                op = "SUB"
            case 0xC4:
                op = "XOR"
            case _:
                match opcode >> 6:
                    case 0b01:
                        dest = (opcode >> 3) & 0b111
                        src = opcode & 0b111
                        if src == 0:
                            op = "MVI"
                            args = (
                                dest,
                                int.from_bytes(instructions[pc : pc + 1], "little"),
                            )
                            pc += 1
                        else:
                            op = "MV"
                            args = (dest, src)
                    case 0b10:
                        dest = (opcode >> 3) & 0b111
                        src = opcode & 0b111
                        if src == 0:
                            op = "MVI32"
                            args = (
                                dest,
                                int.from_bytes(instructions[pc : pc + 4], "little"),
                            )
                            pc += 4
                        else:
                            op = "MV32"
                            args = (dest, src)
                    case _:
                        raise ValueError(f"Unknown opcode: {opcode}")

        return op, args, pc

    def get_reg(src: int, reg_width: Literal[8, 32]) -> int:
        if reg_width == 8 and src == 7:
            return instructions[reg[PTR] + reg[C]]

        src += -(reg_width == 8) + 5 * (reg_width == 32)
        return reg[src]

    def set_reg(dest: int, val: int, reg_width: Literal[8, 32]) -> None:
        if reg_width == 8 and dest == 7:
            instructions[reg[PTR] + reg[C]] = val
            return

        dest += -(reg_width == 8) + 5 * (reg_width == 32)
        reg[dest] = val

    instructions = bytearray(data_)
    stream_out = io.BytesIO()

    # 8 bit registers: a, b, c, d, e, f
    # 32 bit registers: la, lb, lc, ld, ptr, pc
    A, B, C, D, E, F, LA, LB, LC, LD, PTR, PC = range(12)
    reg = [0] * 12

    while True:
        op, args, reg[PC] = get_op(reg[PC])

        match op, args:
            case "ADD", ():
                reg[A] = (reg[A] + reg[B]) & 0xFF
            case "APTR", (imm8,):
                reg[PTR] = (reg[PTR] + imm8) & 0xFFFF_FFFF
            case "CMP", ():
                reg[F] = 0 if reg[A] == reg[B] else 0x01
            case "HALT", ():
                break
            case "JEZ", (imm32,):
                if reg[F] == 0:
                    reg[PC] = imm32
            case "JNZ", (imm32,):
                if reg[F] != 0:
                    reg[PC] = imm32
            case "MV", (dest, src):
                set_reg(dest, get_reg(src, 8), 8)
            case "MV32", (dest, src):
                set_reg(dest, get_reg(src, 32), 32)
            case "MVI", (dest, imm8):
                set_reg(dest, imm8, 8)
            case "MVI32", (dest, imm32):
                set_reg(dest, imm32, 32)
            case "OUT", ():
                stream_out.write(reg[A].to_bytes())
            case "SUB", ():
                reg[A] = (reg[A] - reg[B]) & 0xFF
            case "XOR", ():
                reg[A] = (reg[A] ^ reg[B]) & 0xFF

    return stream_out.getvalue()


layers = [layer0, layer1, layer2, layer3, layer4, layer5, layer6]


def main() -> None:
    for layer, decrypt_fn in enumerate(layers):
        process(layer, decrypt_fn)


if __name__ == "__main__":
    main()
