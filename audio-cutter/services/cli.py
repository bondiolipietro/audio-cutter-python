from utils.cli_input_validators import *

PROMPT_INPUT_LINE = '> '

prompt_input_file = 'Insert absolute or relative path to the audio file:'
prompt_default_input_file = '(No defaults, you should specify the file path)'
prompt_error_input_file = 'Invalid path, the file doesn\'t exists.'
initial_prompts_input_file = [prompt_input_file, prompt_default_input_file]

prompt_input_format = 'Insert the audio file format: (mp3|wav|raw)'
prompt_default_input_format = '(Defaults to "mp3")'
prompt_error_input_format = 'Invalid format.'
allowed_input_formats = ['mp3', 'wav', 'raw']
default_input_format = 'mp3'
initial_prompts_input_format = [
    prompt_input_format, prompt_default_input_format]

prompt_audio_slices_in_min = 'Cut audio in parts of: (in minutes) '
prompt_default_audio_slices_in_min = '(Defaults to "15")'
prompt_error_audio_slices_in_min = 'Invalid number, it should be a positive number.'
default_audio_slices_in_min = '15'
initial_prompts_audio_slices_in_min = [
    prompt_audio_slices_in_min, prompt_default_audio_slices_in_min]

prompt_output_folder = 'Insert absolute or relative path to the output files:'
prompt_default_output_folder = '(Defaults to "/podcutter-python" folder (script folder))'
prompt_error_output_folder = 'Invalid path, the folder doesn\'t exists.'
default_output_folder = '.'
initial_prompts_output_folder = [
    prompt_output_folder, prompt_default_output_folder]

prompt_output_name = 'Insert the default name of the output files:'
prompt_default_output_name = '(Defaults to "podcutter")'
prompt_error_output_name = 'Invalid name. The name can\'t contain the ' + \
    'following symbols: . , \\ / | ? ! * \' " : ; < > ( ) ° ` ´ ^ ~ = + '
default_output_name = 'podcutter'
initial_prompts_output_name = [prompt_output_name, prompt_default_output_name]

prompt_output_format = 'Insert the format of the output files: (mp3|wav|raw)'
prompt_default_output_format = '(Defaults to "mp3")'
prompt_error_output_format = 'Invalid format.'
allowed_output_formats = ['mp3', 'wav', 'raw']
default_output_format = 'mp3'
initial_prompts_output_format = [
    prompt_output_format, prompt_default_output_format]


def prompt_and_get_input(prompts_list):
    print('-----------------------------')
    for prompt in prompts_list:
        print(prompt)
    value = input('\n' + PROMPT_INPUT_LINE)
    return value


def cli_get_input_file():
    value = prompt_and_get_input([*initial_prompts_input_file])
    if len(value) == 0:
        value = prompt_and_get_input(
            [prompt_error_input_file, *initial_prompts_input_file])
    while not validate_cli_input_is_file(value):
        value = prompt_and_get_input(
            [prompt_error_input_file, *initial_prompts_input_file])
    return value


def cli_get_input_format():
    value = prompt_and_get_input([*initial_prompts_input_format])
    if len(value) == 0:
        return default_input_format
    while not validate_cli_input_text(value, allowed_input_formats):
        value = prompt_and_get_input(
            [prompt_error_input_format, *initial_prompts_input_format])
    return value


def cli_get_audio_slices_in_min():
    value = prompt_and_get_input([*initial_prompts_audio_slices_in_min])
    if len(value) == 0:
        return default_audio_slices_in_min
    while not validate_cli_input_is_number(value):
        value = prompt_and_get_input(
            [prompt_error_audio_slices_in_min, *initial_prompts_audio_slices_in_min])
    return value


def cli_get_output_folder():
    value = prompt_and_get_input([*initial_prompts_output_folder])
    if len(value) == 0:
        return default_output_folder
    while not validate_cli_input_is_dir(value):
        value = prompt_and_get_input(
            [prompt_error_output_folder, *initial_prompts_output_folder])
    return value


def cli_get_output_name():
    value = prompt_and_get_input([*initial_prompts_output_name])
    if len(value) == 0:
        return default_output_name
    while not validate_cli_input_name(value):
        value = prompt_and_get_input(
            [prompt_error_output_name, *initial_prompts_output_name])
    return value


def cli_get_output_format():
    value = prompt_and_get_input([*initial_prompts_output_format])
    if len(value) == 0:
        return default_output_format
    while not validate_cli_input_text(value, allowed_output_formats):
        value = prompt_and_get_input(
            [prompt_error_output_format, *initial_prompts_output_format])
    return value


def cli():
    print('-----------------------------')
    print("Leave a field in blank to use its default value.")
    print('-----------------------------')

    input_file = cli_get_input_file()
    input_format = cli_get_input_format()
    audio_slices_in_min = cli_get_audio_slices_in_min()
    output_folder = cli_get_output_folder()
    output_name = cli_get_output_name()
    output_format = cli_get_output_format()

    return {
        'input_file': input_file,
        'input_format': input_format,
        'audio_slices_in_min': audio_slices_in_min,
        'output_folder': output_folder,
        'output_name': output_name,
        'output_format': output_format,
    }
