from PIL import Image
import time

fromer = input('URL : ')
toer = input('Name : ')
lvl = int(input('Level : '))
older_img = Image.open(fromer)
(old_width, old_height) = older_img.size
new_img = Image.new('RGB', (old_width, old_height), (0, 0, 0))
new_img.save(toer)

def lb_modify_img(old, new):
    before = time.time()
    for k in range(lvl):
        for i in range(old_width - 5):
            for j in range(old_height - 5):
                pixel_l = old.getpixel((i - 5, j - 5))
                pixel_p = old.getpixel((i + 5, j + 5))
                new.putpixel((i, j), ((pixel_l[0] + pixel_p[0]) // 2, (pixel_l[1] + pixel_p[1]) // 2, (pixel_l[2] + pixel_p[2]) // 2))
        new.save(toer)
        old = new
        new = Image.new('RGB', (old_width, old_height), (0, 0, 0))
    old.close()
    new.close()
lb_modify_img(older_img, new_img)
