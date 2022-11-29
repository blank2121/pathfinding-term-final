from PIL import Image

def get_image(image_path):
    image = Image.open(image_path).convert("L")
    pixel_values = list(image.getdata())

    return pixel_values