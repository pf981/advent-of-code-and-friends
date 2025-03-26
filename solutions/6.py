import re

from vm import Vm


actions = [
    "take tablet",
    "use tablet",
    "doorway",
    "north",
    "north",
    "bridge",
    "continue",
    "down",
    "east",
    "take empty lantern",
    "west",
    "west",
    "passage",
    "ladder",
    "west",
    "north",
    "south",
    "north",
    "take can",
    "use can",
    "use lantern",
    "west",
    "ladder",
    "darkness",
    "continue",
    "west",
    "west",
    "west",
    "west",
    "north",
    "take red coin",
    "north",
    "east",
    "take concave coin",
    "down",
    "take corroded coin",
    "up",
    "west",
    "west",
    "take blue coin",
    "up",
    "take shiny coin",
    "down",
    "east",
    "use blue coin",
    "use red coin",
    "use shiny coin",
    "use concave coin",
    "use corroded coin",
    "north",
    "take teleporter",
    "use teleporter",
    # "north",
    # "north",
    # "north",
    # "north",
    # "north",
    # "north",
    # "north",
    # "east",
    # "take journal",
    # "look journal",
    # "west",
    # "north",
    # "north",
    # "take orb",
    # "north",
    # "east",
    # "east",
    # "north",
    # "west",
    # "south",
    # "east",
    # "east",
    # "west",
    # "north",
    # "north",
    # "east",
    # "vault",
    # "take mirror",
    # "use mirror",
]

from vm import State

vm = Vm.from_file("./challenge.bin")
*pre_actions, last_action = actions
vm.input("\n".join(pre_actions) + "\n")

vm.run()
vm.input(last_action + "\n")

vm.memory[32775] = 25734
vm.run(breakpoints={5500})
vm.memory[32768] = 6
vm.ip = 5513

vm.output()

vm.resume()

while not (5500 <= vm.ip <= 5513):
# while not (5500 <= vm.ip <= 7000):
# while not (0 <= vm.ip <= 7000):
    # print(f'{vm.ip}')
    vm.step()
    if not vm.state == State.READY:
        print(f'not ready')
        break
    # i += 1
    # if i >= 100: break

# set-reg 0 6
# set-ip 5513


vm.resume()

# from vm import State

# vm = Vm.from_file("./challenge.bin")
# *pre_actions, last_action = actions
# vm.input("\n".join(pre_actions) + "\n")

# vm.run()
# vm.input(last_action + "\n")

# vm.memory[32775] = 25734
# # vm.resume()

# while not (5500 <= vm.ip <= 5513):
# # while not (5500 <= vm.ip <= 7000):
# # while not (0 <= vm.ip <= 7000):
#     # print(f'{vm.ip}')
#     vm.step()
#     if not vm.state == State.READY:
#         print(f'not ready')
#         break
#     # i += 1
#     # if i >= 100: break


# vm.resume()

# from vm import State

# vm = Vm.from_file("./challenge.bin")
# vm.input("\n".join(actions) + "\n")

# i = 0
# # while not (5500 <= vm.ip <= 5503):
# while not (5500 <= vm.ip <= 5513):
#     # print(f'{vm.ip}')
#     vm.step()
#     if not vm.state == State.READY:
#         print(f'not ready')
#         break
#     # i += 1
#     # if i >= 100: break
# vm.resume()

set-breakpoint 5500
set-reg 7 25734
run
set-reg 0 6
set-ip 5513
run


vm.memory[5500:5500+3]
vm.memory[5503:5503+2]

vm.memory[5505:5505+3]

vm.memory[5505:5505+3]
vm.memory[5508:5508+3]
vm.memory[5511:5511+2]
vm.memory[5513:5513+3]

vm = Vm.from_file("./challenge.bin")
vm.run()

*pre_actions, last_action = actions

vm.input("\n".join(pre_actions) + "\n")
vm.run()
vm.output()
vm.memory[32775] = 25734
vm.memory[0x0209] = 8
vm.memory[0x156D] = 6
vm.memory[0x1571] = 21
vm.memory[0x1572] = 21


vm.resume()

# vm.memory[32775] = 25734
# vm.memory[5494] = 4
# # vm.memory[6027] = 8
# # vm.memory[5495] = 7


# # self._poke(6027, 8) # change jt R0 6035 => jf R0 6035 (skip teleporter sanity)
# #         self._poke(5495, 7) # change jf R1 5579 to jt R1 5579 (skip valid value check)

# # vm.memory[32775] = 25734
# # # vm.memory[5485] = 6
# # # vm.memory[5489] = 21
# # # vm.memory[5490] = 21
# # # st:.synacor.editMemory[st;5485;6];
# # # st:.synacor.editMemory[st;5489;21];
# # # st:.synacor.editMemory[st;5490;21];
# # # don't check register 8 for 0 value during self-test
# # vm.memory[521] = 21
# # vm.memory[522] = 21
# # vm.memory[523] = 21

# # # don't call the teleporter confirmation process
# # vm.memory[5489] = 21
# # vm.memory[5490] = 21

# # # don't jump to the do nothing function
# # vm.memory[5491] = 21
# # vm.memory[5492] = 21
# # vm.memory[5493] = 21
# # vm.memory[5494] = 21
# # # vm.memory[0x0209] = 8
# # # vm.memory[0x156D] = 6
# # # vm.memory[0x1571] = 21
# # vm.memory[0x1572] = 21


# vm.input("\n".join(actions) + "\n")
# vm.run()
# # vm.output()
# vm.resume()


def solution(vm: Vm):
    *pre_actions, last_action = actions

    vm.input("\n".join(pre_actions) + "\n")
    vm.run()
    vm.output()
    vm.input(last_action + "\n")
    vm.run()
    output = vm.output()
    return re.findall(r"\w{12}", output)[0]
