import os
import pandas as pd

# Set paths
csv_path = "C:/ModelTraining/Bengali/dataset/metadata.csv"
audio_dir = "C:/ModelTraining/Bengali/dataset/audio/wavs"
cleaned_csv_path = "C:/ModelTraining/Bengali/dataset/metadata_clean.csv"

# Load metadata
df = pd.read_csv(csv_path, sep='|', header=None, names=["filename", "text"])

# Filter only entries with existing .wav files
df_clean = df[df["filename"].apply(lambda x: os.path.exists(os.path.join(audio_dir, x)))]

# Save the cleaned CSV
df_clean.to_csv(cleaned_csv_path, sep='|', header=False, index=False)

print(f"Cleaned metadata saved to: {cleaned_csv_path}")
print(f"Kept {len(df_clean)} of {len(df)} entries.")
