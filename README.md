# Audio Cutter - Python

It's a script that automate the process of split some video in various equal parts, you can configure the following parameters:

```
input_file // an absolute path or a relative (to the script folder) path to the audio file

input_format // the format of the input audio file (mp3|wav|raw), it should be the same of the input_file

audio_slices_in_min // the size (in minutes) of the audio slices

output_folder // an absolute path or a relative (to the script folder) path to some folder

output_name // the name of the audio files that will be generated, the following symbols are not allowed: .,\/|?!*'":;<>()°`´^~=+

output_format // the format of the audio files that will be generated, you can freely choose between mp3, wav or raw
```

## Why I created that

Few days ago I was on a Discord call with some friends and someone had the idea of hear podcasts together, but apparently Spotify does not allow podcasts to be executed on Discord (it only allow musics), and the podcast we wanted to hear is hosted only on spotify (NerdCast). After few minutes googling we found a workaround: Groovy (music bot) accepts users to send mp3 files to play on discord (_noice👍_), but another problem came to us: non-Nitro users of Discord can't send files larger than 8MB, so we had to split the podcast files into smaller parts and send it one by one. So, in short, i just made this script to automate the process of splitting the podcast file.

## Notes

'Pydub' requires installation of ffmpeg libraries, so if you're using Windows you can follow [this tutorial](https://websetnet.net/how-to-install-ffmpeg-on-windows-10-and-add-it-to-windows-path/). If you're using linux:

Arch and its derivatives:

```bash
sudo pacman -S ffmpeg
```

Debian and Ubuntu derivatives:

```bash
sudo apt-get install ffmpeg
```

Fedora:

```bash
sudo dnf install ffmpeg
```

## Usage

First you need to created python virtual environment, so navigate to the project folder:

```bash
cd "/path/to/pipocoin-python"
```

Create python _venv_:

```bash
python -m venv venv
```

Activate the _venv_ on Linux:

```bash
source venv/bin/activate
```

Activate the _venv_ on Windows:

```bash
venv\Scripts\activate.bat
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

If you intend to modify the code you also need to install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the script:

```bash
python audio-cutter
```

## Author

- Pietro Bondioli ([@bondiolipietro](https://github.com/bondiolipietro))

## License

[MIT](https://opensource.org/licenses/MIT)
