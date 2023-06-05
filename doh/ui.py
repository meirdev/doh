from InquirerPy import inquirer
from InquirerPy.base.control import Choice


def select_command(commands: list[str]) -> int | None:
    choices = [Choice(i, cmd) for i, cmd in enumerate(commands)]
    choices.append(Choice(None, "# cancel"))

    choice = inquirer.select(  # type: ignore
        message="Select a command:",
        qmark="",
        amark="",
        pointer="",
        choices=choices,
        default=choices[0],
    ).execute()

    return choice
