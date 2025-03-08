from PIL import Image as img
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, showwarning
import time, math, string

def lb_modify_img():
    if url_from.get() != '' and url_to.get() != '' and lvl.get() != '':
        if lb_isdigit(lvl.get()):
            older = img.open(url_from.get())
            newer = img.new('RGB', (int(old_width.get()), int(old_height.get())), (0, 0, 0))
            before = time.time()
            for k in range(int(lvl.get())):
                for i in range(int(old_width.get()) - 5):
                    for j in range(int(old_height.get()) - 5):
                        pixel_l = older.getpixel((i - 5, j - 5))
                        pixel_p = older.getpixel((i + 5, j + 5))
                        newer.putpixel((i, j), ((pixel_l[0] + pixel_p[0]) // 2, (pixel_l[1] + pixel_p[1]) // 2, (pixel_l[2] + pixel_p[2]) // 2))
                newer.save(url_to.get())
                older = newer
                newer = img.new('RGB', (int(old_width.get()), int(old_height.get())), (0, 0, 0))
            older.close()
            newer.close()
            timing = lb_sec_to_min(time.time() - before)
            showinfo(title='Blurring finished', message=f'Finished in {timing[0]}min {timing[1]}sec {timing[2]}ms')
        else:
            showwarning(title='Warnings', message='Invalid lvl (number)')
    else:
        showwarning(title='Warnings', message='Missing argument(s)')
def lb_copy_path(path):
    spliter = path.split('.')
    return spliter[0] + '_blurred.' + spliter[1]
def lb_sec_to_min(sec):
    return [math.floor(sec // 60), math.floor(sec / 60 % 1 * 60), math.floor(sec % 1 * 1000)]
def lb_open_file():
    file_url = fd.askopenfilename(filetypes=[('JPEG (*.jpg, *.jpeg, *.JPG)', '*.jpg, *.jpeg, *.JPG'), ('PNG (*.png)', '*.png'), ('ICO (*.ico)', '*.ico'), ('All files', '*.*')])
    lb_load_file(file_url)
def lb_load_file(file_url):
    url_from.set(file_url)
    lb_gen_to()
    oldest = img.open(url_from.get())
    old_width.set(oldest.size[0])
    old_height.set(oldest.size[1])
    oldest.close()
def lb_gen_to():
    url_to.set(lb_copy_path(url_from.get()))
def lb_isdigit(str):
    for i in str.lower():
        for j in string.printable[10:][26:].lower():
            if i == j:
                return False
    return True


screen = Tk()
screen.geometry('400x250')
screen.title('Blurrer')
screen['bg'] = '#191919'
screen.resizable(height=False, width=False)
menu_bar = Menu(screen)
menu_file = Menu(menu_bar, tearoff=0, bg='#ffffff', fg='#191919', activebackground='#191919', activeforeground='#ffffff')
menu_file.add_command(label='Open file', command=lb_open_file)
menu_bar.add_cascade(label='File', menu=menu_file)

url_from, url_to, lvl, old_width, old_height = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
from_label = Label(screen, text='Image : ', font=(10), bg='#191919', fg='#ffffff').place(relx='0.5', y='20', anchor=CENTER)
fromer = Entry(screen, textvariable=url_from).place(x='10', y='40', width='315')
button_load = Button(screen, text='Load img', fg='#ffffff', bg='#191919', command=lambda: lb_load_file(url_from.get())).place(x='333', y='36')
to_label = Label(screen, text='Blurred image : ', font=(10), bg='#191919', fg='#ffffff').place(relx='0.5', y='80', anchor=CENTER)
toer = Entry(screen, textvariable=url_to).place(x='10', y='100', width='315')
to_label = Label(screen, text='Blur level : ', font=(10), bg='#191919', fg='#ffffff').place(relx='0.5', y='140', anchor=CENTER)
level = Entry(screen, textvariable=lvl).place(relx='0.5', y='170', width='20', anchor=CENTER)
button_blur = Button(screen, text='Blur', font=(10), fg='white', bg='#191919', command=lb_modify_img).place(relx='0.5', rely='0.85', anchor=CENTER)

screen.config(menu=menu_bar)
screen.mainloop()
