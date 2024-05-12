import json
import os

# Path to the input JSON file
input_file_path = os.path.expanduser('~/Downloads/ad.json')

# Path to the output JSON file
output_file_path = os.path.expanduser('~/Downloads/processed_ad.json')

# Function to process the JSON data
def process_json(input_json_list):
    processed_data = []
    for item in input_json_list:
        result = item.get('result')
        if result is not None:
            ad_id = result.get('id')
            if ad_id is not None:
                # Extracting 'id' and renaming it to 'ad_id'
                ad_id_entry = {'ad_id': ad_id}

                # Extracting 'photos' and getting 'url' values
                photos_entry = {'photo_urls': [photo.get('url', '') for photo in result.get('photos', [])]}

                # Combining the extracted entries
                combined_entry = {**ad_id_entry, **photos_entry}

                processed_data.append(combined_entry)

    return processed_data

# Read the input JSON file
with open(input_file_path, 'r') as input_file:
    json_data = json.load(input_file)
    #print(json_data)

# # Process the JSON data
processed_data = process_json(json_data)
#print(processed_data)  

# # Write the processed data to the output JSON file
with open(output_file_path, 'w') as output_file:
     json.dump(processed_data, output_file, indent=2)

print(f"Processing complete. Results saved to {output_file_path}")


