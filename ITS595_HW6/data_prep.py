import os
import json

# Set the path to the folder containing your movie files
folder_name = './cinema'  # Adjust this path as needed
output_file = 'cinema.jsonl'

# This function will prepare the data and write it to cinema.jsonl
def prepare_data():
    jsonl = ""

    # Iterate through all files in the folder
    for f in os.listdir(folder_name):
        if f.endswith('.txt'):
            file_path = os.path.join(folder_name, f)
            with open(file_path, 'r', encoding='utf-8') as movie_file:
                movie_data = movie_file.read().strip()  # Read the content of each movie file

                # Here, we're creating a simple dictionary for each movie
                entry = {
                    "role": "user",
                    "content": movie_data
                }

                # Convert the dictionary to a JSON line and add it to the jsonl string
                jsonl += json.dumps(entry) + "\n"

    # Write the formatted data to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(jsonl)

# Run the function
prepare_data()

print(f"Data successfully written to {output_file}")
