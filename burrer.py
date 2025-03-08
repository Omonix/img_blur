from PIL import Image
import time, math

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
    return lb_sec_to_min(time.time() - before)
def lb_copy_path(path):
    spliter = path.split('.')
    return spliter[0] + '_blurred.' + spliter[1]
def lb_sec_to_min(sec):
    return [math.floor(sec // 60), math.floor(sec / 60 % 1 * 60), math.floor(sec % 1 * 1000)]

fromer = input('\033[1;32mURL : \033[1;35m')
toer = lb_copy_path(fromer)
lvl = int(input('\033[1;32mLevel : \033[1;35m'))
older_img = Image.open(fromer)
(old_width, old_height) = older_img.size
new_img = Image.new('RGB', (old_width, old_height), (0, 0, 0))
new_img.save(toer)
timing = lb_modify_img(older_img, new_img)
print(f'\033[1;33mFinished in {timing[0]}min {timing[1]}sec {timing[2]}ms\033[0m')
