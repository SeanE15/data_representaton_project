import pandas as pd

# CSV file path
csv_file_path = 'data/points.csv'

# Read CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

# Convert DataFrame to JSON and save to a file
json_file_path = 'points.json'
df.to_json(json_file_path, orient='records', lines=True)

print(f'CSV data successfully converted to JSON. Output file: {json_file_path}')
