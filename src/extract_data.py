import os
import tarfile
import json
import pandas as pd


# Function to process and save JSON files to CSV for analysis
def process_json_files(tar_file_path):
    with tarfile.open(tar_file_path, 'r') as tar:
        for member in tar.getmembers():
            if member.name.endswith('.json'):
                
                # Extract data from JSON file
                file_name = os.path.basename(member.name).replace('.json', '')
                json_file = tar.extractfile(member)
                json_data = [json.loads(line) for line in json_file]

                # Convert data to DataFrame
                df = pd.DataFrame(json_data)

                # Set the path to save the CSV file
                csv_file_path = f'../data/{file_name}.csv'

                # Save DataFrame to CSV
                df.to_csv(csv_file_path, index=False)
                print(f'Saved {csv_file_path}')


if __name__ == "__main__":
    # Source data comes from yelp_dataset.tar in the data folder
    tar_file_path = '../data/yelp_dataset.tar'
    process_json_files(tar_file_path)