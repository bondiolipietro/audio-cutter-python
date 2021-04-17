import os
from pathlib import Path
import re

REGEX_VALIDATE_OUTPUT_NAME = re.compile(
    r'[\.,\\\/|?!\*\'":;<>()°`´^~=+]', re.IGNORECASE)


def validate_cli_input_text(cli_input, allowed_inputs):
    if cli_input in allowed_inputs:
        return True
    return False


def validate_cli_input_is_number(cli_input):
    cli_input = cli_input.strip()
    try:
        cli_input = float(cli_input)
        if cli_input > 0:
            return True
        return False
    except Exception:
        return False


def validate_cli_input_is_dir(path):
    resolved_path = Path(path).resolve()
    return os.path.isdir(resolved_path)


def validate_cli_input_is_file(path):
    resolved_path = Path(path).resolve()
    return os.path.isfile(resolved_path)


def validate_cli_input_name(filename):
    if REGEX_VALIDATE_OUTPUT_NAME.search(filename):
        return False
    return True
