import os
from pathlib import Path

import typer

app = typer.Typer(help="A CLI to format Logic Mill transition rules files atomically.")


RIGHT = "R"
LEFT = "L"
BLANK = "_"
COMMENT_PREFIX = "//"


def format_content(text: str) -> str:
    w1 = 15
    w2 = 15

    lines = text.splitlines()

    if not lines:
        return ""

    result = []
    for line in lines:
        line = line.strip()

        # Blank line
        if not line:
            result.append("")
            continue

        # Comment only
        if line.startswith(COMMENT_PREFIX):
            result.append(
                f"{COMMENT_PREFIX} {line.removeprefix(COMMENT_PREFIX).strip()}"
            )
            continue

        transition, *comment = line.split(COMMENT_PREFIX, 1)
        transition = transition.split()

        comment = f"{COMMENT_PREFIX} {comment[0].strip()}" if comment else None

        if len(transition) != 5:
            raise ValueError(
                f"Expected 5 values per transition rule, got {len(transition)}: {transition}\n{line=}"
            )

        state, symbol, state2, symbol2, move = transition

        out = f"{state:<{w1}}  {symbol}  {state2:<{w2}}  {symbol2}  {move}"
        if comment:
            out += f"  {comment}"
        result.append(out)

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
