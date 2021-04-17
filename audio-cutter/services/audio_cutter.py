from pathlib import Path
from pydub import AudioSegment
from utils.loading_animation import *


def cut_audio_into_parts(input_file,
                         input_format,
                         audio_slices_in_min,
                         output_folder,
                         output_name,
                         output_format):
    file_path = str(Path(input_file).resolve())
    output_folder = str(Path(output_folder).resolve())

    sound = AudioSegment.from_file(file_path, format=input_format)

    audio_slices_in_ms = int(float(audio_slices_in_min) * 60000)

    loading_animation_thread.start()

    for i, chunk in enumerate(sound[::audio_slices_in_ms]):
        with open(f"{output_name}-{i}.{output_format}", "wb") as f:
            chunk.export(f, format=output_format)

    stop_loading_animation_thread()
