from pydub import AudioSegment
import os

input_dir = "C:/ModelTraining/Bengali/dataset/audio"
output_dir = "C:/ModelTraining/Bengali/dataset/audio/wavs"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if file.endswith(".flac"):
        flac_path = os.path.join(input_dir, file)
        wav_path = os.path.join(output_dir, file.replace(".flac", ".wav"))
        audio = AudioSegment.from_file(flac_path, format="flac")
        audio = audio.set_frame_rate(22050).set_channels(1)
        audio.export(wav_path, format="wav")
