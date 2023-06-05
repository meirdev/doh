import ast
import shlex

import openai

from ..command import Command
from ..correct import Correct
from ..registry import registry
from ..settings import settings

ENGINE = "text-davinci-003"
TEMPERATURE = 1
MAX_TOKENS = 256
TOP_P = 1
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 0


def openai_correct(command: Command):
    openai.api_key = settings.openai_api_key

    output = command.stderr.decode()
    if output:
        output = f"""Produced the following output:\n{command.stderr.decode()}\n---\n"""

    try:
        results = openai.Completion.create(
            prompt=f"""The command:\n{shlex.join(command.args)}\n---\n{output}Return a valid python code of a list of possible fixes.""",
            engine=ENGINE,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            top_p=TOP_P,
            frequency_penalty=FREQUENCY_PENALTY,
            presence_penalty=PRESENCE_PENALTY,
        )

        text = results.choices[0].text  # type: ignore

        # Remove the variable name if it exists
        list_repr = text[text.find("[") : text.rfind("]") + 1]

        return [Correct(shlex.split(opt)) for opt in ast.literal_eval(list_repr)]
    except Exception:
        return


if settings.enable_openai:
    registry(openai_correct)
