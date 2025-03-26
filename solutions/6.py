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
    "_set-register 7 25734",
    "_set-breakpoint 5500",
    "use teleporter",
    "_set-register 0 6",
    "_set-ip 5513",
]


def solution(vm: Vm):
    pre_actions = actions[:-3]
    last_actions = actions[-3:]

    vm.input("\n".join(pre_actions) + "\n")
    vm.run()
    vm.output()
    vm.input("\n".join(last_actions) + "\n")
    vm.run()
    output = vm.output()
    return re.findall(r"\w{12}", output)[0]
