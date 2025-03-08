from PIL import Image
import urllib.request
import time

older_img = Image.open(input('URL : '))
(old_width, old_height) = older_img.size
new_img = Image.new('RGB', (old_width, old_height), (0, 0, 0))
new_img.save(input('Name : '))

def lb_modify_img():
    before = time.time()
    for i in range(10, old_width - 10):
        for j in range(10, old_height - 10):
            pixel_l = older_img.getpixel((i - 10, j - 10))
            pixel_p = older_img.getpixel((i + 10, j + 10))
            new_img.putpixel((i, j), ((pixel_l[0] + pixel_p[0]) // 2, (pixel_l[1] + pixel_p[1]) // 2, (pixel_l[2] + pixel_p[2]) // 2))
    new_img.save('test.jpg')
    new_img.close()
    older_img.close()
lb_modify_img()
