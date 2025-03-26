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
