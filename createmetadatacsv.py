import csv
import os

import os
import csv
import parselmouth
import numpy as np

def detect_gender_pitch(audio_path):
    try:
        snd = parselmouth.Sound(audio_path)
        pitch = snd.to_pitch()
        pitch_values = pitch.selected_array['frequency']
        pitch_values = pitch_values[pitch_values > 50]  # Remove unvoiced or low pitch

        if len(pitch_values) == 0:
            return "unknown"

        mean_pitch = np.mean(pitch_values)
        if mean_pitch < 165:
            return "male"
        elif mean_pitch > 180:
            return "female"
        else:
            return "uncertain"
    except Exception as e:
        print(f"Error processing {audio_path}: {e}")
        return "unknown"

def generate_gendered_metadata(wav_dir, input_csv, output_csv):
    print("generate_gendered_metadata")
    with open(input_csv, "r", encoding="utf-8") as fin, \
         open(output_csv, "w", encoding="utf-8", newline='') as fout:

        reader = csv.reader(fin, delimiter='|')
        writer = csv.writer(fout, delimiter='|')

        for row in reader:
            if len(row) != 2:
                print(f"Skipping invalid row: {row}")
                continue

            wav_file, text = row
            full_path = os.path.join(wav_dir, wav_file)
            rel_path = os.path.relpath(full_path, start=os.path.dirname(output_csv)).replace("\\", "/")

            if not os.path.isfile(full_path):
                print(f"Missing file: {full_path}")
                continue

            gender = detect_gender_pitch(full_path)
            if gender not in ['male', 'female']:
                # Skip this row
                continue            
            writer.writerow([rel_path, gender, text.strip()])

    print(f"✅ Metadata with gender written to {output_csv}")


if __name__ == "__main__":
    print("hi")
    audiofile = input("Enter the path to the Bengali WAV file: ").strip('"')
    input_csv = input("Enter csv file with wav and text mapping: ").strip('"')
    output_csv = input("Enter output csv file with 3 col: ").strip('"')
    if not os.path.exists(audiofile):
        print("File not found!")
    else:
        generate_gendered_metadata(audiofile, input_csv, output_csv)