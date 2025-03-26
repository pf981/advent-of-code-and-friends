import re

from vm import Vm


def solution(vm: Vm):
    vm.run()
    vm.output()
    vm.input("\n".join(["take tablet", "use tablet"]) + "\n")
    vm.run()
    output = vm.output()
    return re.findall(r"\w{12}", output)[0]
