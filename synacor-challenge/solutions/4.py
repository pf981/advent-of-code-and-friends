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
]


def solution(vm: Vm):
    *pre_actions, last_action = actions

    vm.input("\n".join(pre_actions) + "\n")
    vm.run()
    vm.output()
    vm.input(last_action + "\n")
    vm.run()
    output = vm.output()
    return re.findall(r"\w{12}", output)[0]
