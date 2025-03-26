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
    # "use teleporter",
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

vm = Vm.from_file("./challenge.bin")
# vm.run()
# vm.memory[32775 - 7] = 25734

# # don't check register 8 for 0 value during self-test
# vm.memory[521] = 21
# vm.memory[522] = 21
# vm.memory[523] = 21

# # don't call the teleporter confirmation process
# vm.memory[5489] = 21
# vm.memory[5490] = 21

# # don't jump to the do nothing function
# vm.memory[5491] = 21
# vm.memory[5492] = 21
# vm.memory[5493] = 21
# vm.memory[5494] = 21
# # vm.memory[0x0209] = 8
# # vm.memory[0x156D] = 6
# # vm.memory[0x1571] = 21
# # vm.memory[0x1572] = 21
vm.input("\n".join(actions) + "\n")
vm.run()
vm.resume()


def solution(vm: Vm):
    *pre_actions, last_action = actions

    vm.input("\n".join(pre_actions) + "\n")
    vm.run()
    vm.output()
    vm.input(last_action + "\n")
    vm.run()
    output = vm.output()
    return re.findall(r"\w{12}", output)[0]
