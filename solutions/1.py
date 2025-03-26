import re

from vm import Vm


def solution(vm: Vm):
    vm.run()
    output = vm.output()
    return re.findall(r"\w{12}", output)[0]
