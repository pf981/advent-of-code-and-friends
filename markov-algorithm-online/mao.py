Rule = tuple[str, str, bool]


def parse(code: str, code_length_limit: int = 1000) -> list[Rule]:
    if len(code) > code_length_limit:
        raise ValueError(
            f"Unable to parse as code exceeds {code_length_limit} characters: {len(code)}"
        )

    rules = []
    for line in code.splitlines():
        if ":" not in line:
            continue

        match line.split(":"):
            case [pattern, replacement]:
                rules.append((pattern.strip(), replacement.strip(), False))
            case [pattern, "", replacement]:
                rules.append((pattern.strip(), replacement.strip(), True))
            case _:
                raise ValueError(f"Unable to parse as line: {line!r}")

    return rules


def run(
    input_: str,
    rules: list[Rule],
    step_limit: int = 50000,
    string_length_limit: int = 1000,
) -> tuple[str, list[str]]:
    steps = [input_]
    while True:
        if len(steps) > step_limit:
            raise ValueError(f"Number of steps exceeds {step_limit} limit")
        if len(input_) > string_length_limit:
            raise ValueError(
                f"String length exceeds {string_length_limit} limit: {input_!r}\n\n--- START STEPS ---\n{'\n'.join(steps)}\n--- END STEPS ---"
            )

        for pattern, replacement, terminate in rules:
            if not pattern:
                input_ = replacement + input_
                break

            if pattern in input_:
                input_ = input_.replace(pattern, replacement, 1)
                break
        else:
            break

        steps.append(input_)
        if terminate:
            break

    return input_, steps
