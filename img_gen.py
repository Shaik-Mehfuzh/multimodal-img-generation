import requests
import time

prompt = input("Enter image prompt:A cute cat wearing sunglasses on a beach")

url = f"https://image.pollinations.ai/prompt/{prompt}?seed={int(time.time())}"

img = requests.get(url).content

with open("generated_image.png", "wb") as f:
    f.write(img)

print("Image saved!")