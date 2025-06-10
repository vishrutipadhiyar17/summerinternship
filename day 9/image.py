import requests
import webbrowser
import os

prompt = input("Enter a prompt to generate an image: ")

api_key = "sk-yGqnVdpJiqTHjYSawKt159ZveWzQanTxbqCNUaP0rlwUYFbx"

url = "https://api.stability.ai/v2beta/stable-image/generate/core"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "image/*"  
}

files = {
    "prompt": (None, prompt),
    "output_format": (None, "png"),
}

response = requests.post(url, headers=headers, files=files)


if response.status_code == 200:
    image_path = "generated_image.png"
    with open(image_path, "wb") as f:
        f.write(response.content)
    print(f" Image saved as: {image_path}")
    webbrowser.open('file://' + os.path.realpath(image_path))
else:
    print(" Request failed:", response.status_code)
    print(response.text)
