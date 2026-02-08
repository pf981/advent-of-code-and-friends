import os
from pathlib import Path

import typer

app = typer.Typer(help="A CLI to format Logic Mill transition rules files atomically.")

COMMENT_PREFIX = "//"


# BLANK
# COMMENT
# TRANSITION
# TRANSITION_AND_COMMENT
def format_content(text: str) -> str:
    lines = text.splitlines()

    if not lines:
        return ""

    # First pass to do validation and get max width of state and state2 columns
    tokens = []
    w1 = w2 = 1
    for line in lines:
        line = line.strip()

        if not line:
            tokens.append(("BLANK",))
            continue

        if line.startswith(COMMENT_PREFIX):
            tokens.append(("COMMENT", line.removeprefix(COMMENT_PREFIX).strip()))
            continue

        transition, *comment = line.split(COMMENT_PREFIX, 1)
        transition = transition.split()

        comment = comment[0].strip() if comment else None

        if len(transition) != 5:
            raise ValueError(
                f"Expected 5 values per transition rule, got {len(transition)}: {transition}\n{line=}"
            )

        w1 = max(w1, len(transition[0]))
        w2 = max(w2, len(transition[2]))

        if comment:
            tokens.append(("TRANSITION_AND_COMMENT", transition, comment))
        else:
            tokens.append(("TRANSITION", transition))

    result = []
    for token in tokens:
        match token:
            case ("BLANK",):
                result.append("")
            case ("COMMENT", comment):
                result.append(f"{COMMENT_PREFIX} {comment}")
            case ("TRANSITION", comment):
                state, symbol, state2, symbol2, move = transition
                out = f"{state:<{w1}}  {symbol}  {state2:<{w2}}  {symbol2}  {move}"
                result.append(out)
            case ("TRANSITION_AND_COMMENT", transition, comment):
                state, symbol, state2, symbol2, move = transition
                out = f"{state:<{w1}}  {symbol}  {state2:<{w2}}  {symbol2}  {move}"
                result.append(f"{out}  {COMMENT_PREFIX} {comment}")
            case _:
                raise ValueError(f"Unexpected token: {token}")
        line = line.strip()

    # End with blank line
    if result[-1]:
        result.append("")

    return "\n".join(result)


@app.command()
def main(
    file_path: Path = typer.Argument(
        ...,
        exists=True,
        readable=True,
        writable=True,
        help="Path to the Logic Mill transition rules file.",
    ),
):
    """
    Reads a Logic Mill transition rules file, formats, and overwrites it atomically.
    """
    try:
        content = file_path.read_text(encoding="utf-8")
        formatted_content = format_content(content)

        temp_file = file_path.with_suffix(f"{file_path.suffix}.tmp")
        try:
            temp_file.write_text(formatted_content, encoding="utf-8")

            os.replace(temp_file, file_path)
            typer.secho(f"Atomic update complete: {file_path}", fg=typer.colors.GREEN)

        except Exception as e:
            if temp_file.exists():
                temp_file.unlink()
            raise e

    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
