# Re-read the newly uploaded file and proceed with filtering

# Initialize an empty list to store the filtered words
from pathlib import Path


filtered_words = []
file_path = Path("words_alpha.txt")
output_file_path = Path("words_length_4_alpha_base.txt")

with file_path.open('r') as in_file, output_file_path.open('w') as out_file:
    filtered_words = set([line.strip().lower() for line in in_file if len(line.strip()) == 4 and line.strip().isalpha()])
    out_file.write('\n'.join(filtered_words))

