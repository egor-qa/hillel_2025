import requests
import os

# API URL
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
params = {
    "sol": 1000,              # Martian sol (analog of a day)
    "camera": "fhaz",         # Camera
    "api_key": "DEMO_KEY"     # Free key (can be replaced with your own)
}

# Request to API
response = requests.get(url, params=params)

# Check if request is successful
if response.status_code == 200:
    data = response.json()
    photos = data.get("photos", [])

    if not photos:
        print("No photos found for the given parameters")
    else:
        # Create a folder for saving
        os.makedirs("mars_photos", exist_ok=True)

        for i, photo in enumerate(photos, start=1):
            img_url = photo["img_src"]
            img_data = requests.get(img_url).content

            file_name = f"mars_photos/mars_photo{i}.jpg"
            with open(file_name, "wb") as f:
                f.write(img_data)

            print(f"Saved: {file_name}")

else:
    print(f"Request error: {response.status_code}")