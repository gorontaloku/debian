from tkinter import *
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import os
import time
import datetime

# === PASSWORD ===
CORRECT_PASSWORD = "1234"  # Ganti password
password_visible = False

# === PATHS ===
BASE = "/data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/debian/usr/share/conky_theme/macos-lock/"
WALLPAPER = BASE + "background.jpg"
AVATAR = BASE + "avatar.png"
EYE_OPEN = BASE + "eye_open.png"
EYE_CLOSE = BASE + "eye_closed.png"
SPINNER = BASE + "spinner.png"

# === ROOT ===
root = Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.attributes("-alpha", 0)

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

# === BLUR WALLPAPER ===
img = Image.open(WALLPAPER)
img = img.filter(ImageFilter.GaussianBlur(12))
img = img.resize((screen_w, screen_h))
bg = ImageTk.PhotoImage(img)

canvas = Canvas(root, width=screen_w, height=screen_h, highlightthickness=0, bd=0)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, anchor="nw", image=bg)

# === HARI & TANGGAL ===
def update_datetime():
    from time import localtime, strftime

    hari = strftime("%A", localtime())
    tanggal = strftime("%d %B %Y", localtime())

    canvas.itemconfig(hari_text, text=hari)
    canvas.itemconfig(tanggal_text, text=tanggal)
    root.after(1000, update_datetime)

hari_text = canvas.create_text(
    screen_w/2, screen_h * 0.12,
    text="", fill="white",
    font=("Anurati", 53)
)

tanggal_text = canvas.create_text(
    screen_w/2, screen_h * 0.18,
    text="", fill="white",
    font=("JosefinSans", 26)
)

update_datetime()

# === AVATAR ===
avatar_img = Image.open(AVATAR).resize((60, 60))
avatar_img = ImageTk.PhotoImage(avatar_img)
canvas.create_image(screen_w/2, screen_h * 0.82, image=avatar_img)

# === USERNAME ===
canvas.create_text(
    screen_w/2, screen_h * 0.88,
    text="Bestmomen",
    font=("Anurati", 20, "bold"),
    fill="white"
)

# === SPINNER FRAMES ===
spinner_img_raw = Image.open(SPINNER).convert("RGBA").resize((28, 28))

enhancer = ImageEnhance.Brightness(spinner_img_raw)
spinner_img_raw = enhancer.enhance(1.6)

enhancer = ImageEnhance.Contrast(spinner_img_raw)
spinner_img_raw = enhancer.enhance(1.7)

shadow = spinner_img_raw.copy()
shadow = shadow.filter(ImageFilter.GaussianBlur(2))
spinner_img_raw = Image.alpha_composite(shadow, spinner_img_raw)

spinner_frames = []
for angle in range(0, 360, 30):
    spinner_frames.append(ImageTk.PhotoImage(spinner_img_raw.rotate(angle)))

# === GLASS BOX ===
pwd_y = int(screen_h * 0.93)

def round_rectangle(x1, y1, x2, y2, r=25, **kwargs):
    points = [
        x1+r, y1,
        x2-r, y1,
        x2, y1,
        x2, y1+r,
        x2, y2-r,
        x2, y2,
        x2-r, y2,
        x1+r, y2,
        x1, y2,
        x1, y2-r,
        x1, y1+r,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

glass_box = round_rectangle(
    screen_w/2 - 140, pwd_y - 18,
    screen_w/2 + 140, pwd_y + 18,
    r=20,
    fill="#D0D0D0",
    outline="#FFFFFF",
    width=2
)



# === EYE ICON ===
eye_open_img = ImageTk.PhotoImage(Image.open(EYE_OPEN).resize((32, 32)))
eye_close_img = ImageTk.PhotoImage(Image.open(EYE_CLOSE).resize((32, 32)))

eye_icon = canvas.create_image(
    screen_w/ + 115,
    pwd_y,
    image=eye_open_img
)

def update_eye_position():
    root.update_idletasks()

    x = pwd.winfo_x()
    y = pwd.winfo_y()
    w = pwd.winfo_width()

    eye_x = x + w - 18
    eye_y = y + 20

    canvas.coords(eye_icon, eye_x, eye_y)

root.after(30, update_eye_position)
root.after(150, update_eye_position)
root.after(300, update_eye_position)

def toggle_password():
    global password_visible
    password_visible = not password_visible

    if password_visible:
        pwd.config(show="")
        canvas.itemconfig(eye_icon, image=eye_close_img)
    else:
        pwd.config(show="●")
        canvas.itemconfig(eye_icon, image=eye_open_img)

canvas.tag_bind(eye_icon, "<Button-1>", lambda e: toggle_password())



# === ENTRY PASSWORD ===
pwd = Entry(
    root,
    show="●",
    font=("Helvetica", 16),
    justify="center",
    bd=0,
    bg="#D0D0D0",
    fg="black",
    insertbackground="black",
    highlightthickness=0
)
pwd.place(x=screen_w//2, y=pwd_y, anchor="center")





# === SPINNER ===
spinner_icon = canvas.create_image(
    screen_w/2, pwd_y + 45,
    image=spinner_frames[0],
    state="hidden"
)
canvas.tag_raise(spinner_icon)

def animate_spinner(frame=0):
    canvas.itemconfig(spinner_icon, image=spinner_frames[frame])
    return root.after(60, animate_spinner, (frame + 1) % len(spinner_frames))

# === PLACEHOLDER ===
PLACEHOLDER_TEXT = "Masukkan kata sandi..."
PLACEHOLDER_COLOR = "#787878"
TEXT_COLOR = "#000000"
placeholder_active = True
first_launch = True

def apply_placeholder():
    global placeholder_active
    placeholder_active = True
    pwd.config(fg=PLACEHOLDER_COLOR, show="")
    pwd.delete(0, END)
    pwd.insert(0, PLACEHOLDER_TEXT)

def remove_placeholder(event=None):
    global placeholder_active, first_launch
    if placeholder_active:
        pwd.delete(0, END)
        pwd.config(fg=TEXT_COLOR, show="●")
        placeholder_active = False
    first_launch = False

def restore_placeholder(event=None):
    if pwd.get() == "":
        apply_placeholder()

def delayed_placeholder():
    if first_launch:
        apply_placeholder()

pwd.bind("<FocusIn>", remove_placeholder)
pwd.bind("<FocusOut>", restore_placeholder)
root.after(300, delayed_placeholder)

# === ERROR TEXT ===
error_text = canvas.create_text(
    screen_w/2, pwd_y + 35,
    text="",
    font=("Helvetica", 14),
    fill="white"
)

# === SHAKE EFFECT ===
def shake():
    original_x = root.winfo_x()
    original_y = root.winfo_y()
    offset = 12

    for _ in range(8):
        root.geometry(f"+{original_x + offset}+{original_y}")
        root.update()
        time.sleep(0.015)
        root.geometry(f"+{original_x - offset}+{original_y}")
        root.update()
        time.sleep(0.015)
        offset *= 0.75

    root.geometry(f"+{original_x}+{original_y}")

# === FADE OUT ===
def fade_out():
    for i in range(20, -1, -1):
        root.attributes("-alpha", i/20)
        root.update()
        time.sleep(0.02)

# === UNLOCK ===
def unlock():
    if pwd.get() == CORRECT_PASSWORD:
        fade_out()
        root.destroy()
    else:
        canvas.itemconfig(spinner_icon, state="normal")
        spin = animate_spinner()

        def stop_spinner():
            root.after_cancel(spin)
            canvas.itemconfig(spinner_icon, state="hidden")

            # Tampilkan error
            canvas.itemconfig(error_text, text="Wrong password")

            # Hapus error setelah 5 detik
            root.after(5000, lambda: canvas.itemconfig(error_text, text=""))

            pwd.delete(0, END)
            shake()

        root.after(1000, stop_spinner)


root.bind("<Return>", lambda e: unlock())
pwd.bind("<Return>", lambda e: unlock())

# === FADE IN ===
def fade_in():
    for i in range(0, 21):
        root.attributes("-alpha", i/20)
        root.update()
        time.sleep(0.02)

fade_in()
pwd.lift()
root.mainloop()
