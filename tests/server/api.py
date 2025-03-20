import requests
import json
import time

# Test image URL
test_image_url = "https://fleea-image-upload-bucket.s3.eu-west-3.amazonaws.com/3.jpeg"

# Prepare the request payload
payload = {
    "image_url": test_image_url,
    "should_evaluate": True,
    "export_folder": "/test_export",
    "messages": []
}

# Send the request
print("Sending request to API...")
response = requests.post("http://127.0.0.1:8000/", json=payload, stream=True)

# Process the streaming response
print("Receiving streaming response:")
for line in response.iter_lines():
    if line:
        # Remove the "data: " prefix
        data = line.decode('utf-8').replace('data: ', '')
        try:
            # Parse the JSON data
            event_data = json.loads(data)
            print(json.dumps(event_data, indent=2))
        except json.JSONDecodeError:
            print(f"Could not decode JSON: {data}")
        
        # Add a small delay to make the output more readable
        time.sleep(0.1)
