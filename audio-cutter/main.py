from services.audio_cutter import cut_audio_into_parts
from services.cli import cli


def main():
    args = cli()
    cut_audio_into_parts(**args)
    print("Pronto, corno!")
