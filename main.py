from os.path import getmtime
from os import listdir
from pathlib import Path
from pydub import AudioSegment

# location of where Rekordbox saves mixes
mixes_location = "/Volumes/Seagate/My Music/Raw Mixes/Unknown Artist/"

if __name__ == '__main__':
    directories = sorted(Path(mixes_location).iterdir(), key=getmtime, reverse=True)
    most_recent_folder = str(directories[0])
    files = listdir(most_recent_folder)
    latest_mix = [file for file in files if ".wav" in file][0]
    file_path = most_recent_folder + '/' + latest_mix
    file_name = latest_mix.split('.')[0]
    AudioSegment.from_wav(file_path).export(f"/Users/joelmunoz/Music/PioneerDJ/Recording/{file_name}.mp3", format="mp3")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
