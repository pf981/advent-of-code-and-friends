import argparse
import collections

from vm import State, Vm

def parse_room(s: str) -> tuple:
    paragraphs = s.split("\n\n")
    assert paragraphs[0] == "", f"First line not blank: '{paragraphs[0]}' ->\n{s}"
    title, text = paragraphs[1].splitlines()
    assert title.startswith("=="), f"Incorrect title format '{title}' ->\n{s}"
    title = title.removeprefix("== ").removesuffix(" ==")

    interests = []
    exits = []

    if len(paragraphs) == 5:
        interests = [line[2:] for line in paragraphs[2].splitlines()[1:]]
        exits = [line[2:] for line in paragraphs[3].splitlines()[1:]]
    elif len(paragraphs) == 4:
        exits = [line[2:] for line in paragraphs[2].splitlines()[1:]]
    else:
        assert False, f"Unexpected number of paragraphs '{len(paragraphs)}' ->\n{s}"

    assert paragraphs[-1] == "What do you do?\n", f"Incorrect footer '{paragraphs[-1]}' ->\n{s}"
    return title, text, interests, exits


def resume(vm: Vm) -> None:
    print('--- Resuming VM ---')
    vm.input("look\n")
    while True:
        assert vm.state == State.READY
        vm.run()

        print(vm.output())

        # dump = vm.dump()
        # if dump in seen:
        #     print('--- State seen previously ---')
        # seen.add(dump)

        if vm.state == State.INPUT_BLOCKED:
            # Parse Room
            vm.input("look\n")
            vm.run()
            # title, text, interests, exits = parse_room(vm.output())
            # print(f'{title=} {interests=} {exits=}')

            inp = input()
            if inp == "q":  # Custom quit command
                break
            if inp.startswith("d "):  # Custom dump command
                with open(inp.split(" ", 1)[1], "w") as f:
                    f.write(str(vm.dump()))
            vm.input(inp + "\n")
        else:
            break
    print("--- VM Exited ---")

def main() -> None:
    parser = argparse.ArgumentParser("vm")
    parser.add_argument(
        "file", help="Path of bin file.", default="./challenge.bin", type=str, nargs="?"
    )
    args = parser.parse_args()

    vm = Vm.from_file(args.file)

    vm.input("\n".join([
        'take tablet',
        'doorway',
        'north',
        'north',
        'bridge',
        'continue',
        'down',
        'east',
        'take empty lantern',
        'west',
        'west',
        'passage',
        'ladder' # Twisty passages
    ]) + "\n")
    vm.run()
    vm.output()


    # vm.input("look\n")
    # resume(vm)

    seen = {vm.dump()}
    q = collections.deque([vm.dump()])
    while q:
        dump = q.popleft()
        vm = Vm.from_dump(dump)

        vm.input("look\n")
        vm.run()
        title, text, interests, exits = parse_room(vm.output())

        if title != "Twisty passages":
            print(f"New title: {title}")
            resume(vm)
        elif interests:
            print(f"New interests: {interests}")
            resume(vm)
        elif any(exit not in ["ladder", "north", "east", "south", "west"] for exit in exits):
            print(f"New exits: {exits}")
            resume(vm)

        for exit in exits:
            if exit == "ladder":
                continue

            vm = Vm.from_dump(dump)
            vm.input(f"{exit}\n")
            vm.run()

            dump2 = vm.dump()
            if dump2 in seen:
                continue
            seen.add(dump2)
            q.append(dump2)


if __name__ == "__main__":
    main()


# Results:
# $ echo -n "<Code Here>" | md5sum

# 76ec2408e8fe3f1753c25db51efd8eb3
# 0e6aa7be1f68d930926d72b3741a145c DONE (first output)
# 7997a3b2941eab92c1c0345d5747b420 DONE (successful self-test)
# 186f842951c0dcfe8838af1e7222b7d4 DONE (tablet)
# 2bf84e54b95ce97aefd9fc920451fc45
# e09640936b3ef532b7b8e83ce8f125f4 DONE (teleporter)
# 4873cf6b76f62ac7d5a53605b2535a0c
# d0c54d4ed7f943280ce3e19532dbb1a6
