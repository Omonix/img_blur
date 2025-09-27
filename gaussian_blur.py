from PIL import Image
import math, time

def g_core(x, y, s):
    return (1 / (2 * math.pi * s ** 2)) * math.exp(-((x ** 2 + y ** 2) / (2 * s ** 2)))
def lb_gaussian_blur(image, sigma=1):
    width, height = image.size
    new_image = Image.new('RGB', (width, height), (0, 0, 0))
    for x in range(width):
        for y in range(height):
            ranged = sigma * 2 + 1
            neighbors = [{"x": x + i, "y": y + j, "g": g_core(i, j, sigma)} for i in range(max(-ranged, -4), min(ranged, 4) + 1, 1) for j in range(max(-ranged, -4), min(ranged, 4) + 1, 1) if (x + i >= 0 and y + j >= 0 and x + i < width and y + j < height)]
            coeffs = 0
            moy_r, moy_g, moy_b = 0, 0, 0
            for n in neighbors:
                coeffs += n["g"]
                r, g, b = image.getpixel((n["x"], n["y"]))
                moy_r += n["g"] * r
                moy_g += n["g"] * g
                moy_b += n["g"] * b
            new_image.putpixel((x, y), (int(moy_r / coeffs), int(moy_g / coeffs), int(moy_b / coeffs)))
    image.paste(new_image)

img = Image.open("./images.jpg").convert("RGB")
start_time = time.time()
lb_gaussian_blur(img, 3)
end_time = time.time()
print(f"Processing time: {end_time - start_time} seconds")
img.show()
