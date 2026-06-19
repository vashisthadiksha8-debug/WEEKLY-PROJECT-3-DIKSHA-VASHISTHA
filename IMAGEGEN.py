import requests

prompt = input("enter image description:")
print("Choose size:")
print("1. Square (1024x1024)")
print("2. Landscape (1344x768)")
print("3. Portrait (768x1344)")
size = input("Enter 1, 2 or 3: ")

if size == "1":
    dimensions = "1024x1024"
elif size == "2":
    dimensions = "1344x768"
else:
    dimensions = "768x1344"

prompt = prompt.replace(" ", "%20")
url = f"https://image.pollinations.ai/prompt/{prompt}"
response = requests.get(url,timeout=60)
with open("xoxo.png" , "wb") as f:
    f.write(response.content)
    print("done , check ur folder for the image")
