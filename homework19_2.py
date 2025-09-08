import requests

base_url = "http://127.0.0.1:8080"

# 1. Upload an image (POST /upload)
with open("background.jpg", "rb") as img:  # specify any local image here
    files = {"image": img}
    response = requests.post(f"{base_url}/upload", files=files)

if response.status_code == 201:
    data = response.json()
    image_url = data["image_url"]
    print(f"Image uploaded: {image_url}")
else:
    print(f"Upload failed: {response.status_code}")
    exit()

# 2. Get image URL (GET /image/<filename>)
filename = image_url.split("/")[-1]  # extract filename from URL
headers = {"Content-Type": "text"}   # server will return JSON with URL
response = requests.get(f"{base_url}/image/{filename}", headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"Image URL: {data['image_url']}")
else:
    print(f"Failed to get image: {response.status_code}")

# 3. Delete the image (DELETE /delete/<filename>)
response = requests.delete(f"{base_url}/delete/{filename}")

if response.status_code == 200:
    data = response.json()
    print(f"Deleted: {data}")
else:
    print(f"Delete failed: {response.status_code}")