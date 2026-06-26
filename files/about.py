from tkinter import *
from PIL import Image, ImageTk
import platform
import subprocess
import time
import webbrowser


# ================= CONFIG =================
WINDOW_W = 350
WINDOW_H = 520   # dipendekkan agar proporsional
BG = "#EDEDED"
CARD = "#F6F6F6"
PAD_BOTTOM = 40
BUTTON_FOOTER_GAP = 50


# ================= ROOT =================
root = Tk()
root.overrideredirect(True)
root.resizable(False, False)
root.configure(bg=BG)
root.attributes("-alpha", 0)

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w - WINDOW_W) // 2
y = (screen_h - WINDOW_H) // 2
root.geometry(f"{WINDOW_W}x{WINDOW_H}+{x}+{y}")

# ================= CANVAS =================
canvas = Canvas(
    root,
    width=WINDOW_W,
    height=WINDOW_H,
    bg=BG,
    highlightthickness=0
)
canvas.pack(fill="both", expand=True)

# ================= ROUND RECT =================
def round_rect(x1, y1, x2, y2, r=28, **kw):
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
    return canvas.create_polygon(points, smooth=True, **kw)

round_rect(8, 8, WINDOW_W-8, WINDOW_H-8, r=30, fill=CARD)

# ================= WINDOW BUTTONS =================
btn_y = 24
btn_x = 26
gap = 16
colors = ["#FF5F57", "#FFBD2E", "#28C840"]

btns = []
for i, c in enumerate(colors):
    btns.append(
        canvas.create_oval(
            btn_x+i*gap, btn_y,
            btn_x+i*gap+12, btn_y+12,
            fill=c, outline=""
        )
    )

canvas.tag_bind(btns[0], "<Button-1>", lambda e: root.destroy())

# ================= SYSTEM INFO =================
try:
    distro = subprocess.getoutput("lsb_release -ds").replace('"','')
except:
    distro = "Linux"

kernel = platform.release()
arch = platform.machine()
hostname = platform.node()

# ================= POSISI (GRID VERTIKAL) =================
Y_LOGO   = 130
Y_TITLE  = 240
Y_KERNEL = 270
Y_INFO   = 320
Y_BUTTON = 400


# ================= IMAGE =================
IMG_PATH = "/data/data/com.termux/files/usr/var/lib/proot-distro/containers/debian/rootfs/usr/share/conky_theme/macos-lock/laptop.png"

img_raw = Image.open(IMG_PATH)

# target width seperti macOS
TARGET_W = 200
ratio = TARGET_W / img_raw.width
TARGET_H = int(img_raw.height * ratio)

img = img_raw.resize((TARGET_W, TARGET_H), Image.LANCZOS)
img = ImageTk.PhotoImage(img)

canvas.create_image(
    WINDOW_W // 2,
    145,
    image=img
)

def get_device_name():
    if CUSTOM_DEVICE_NAME:
        return CUSTOM_DEVICE_NAME
    try:
        name = subprocess.getoutput("getprop ro.product.marketname").strip()
        if name:
            return name
        return subprocess.getoutput("getprop ro.product.model").strip()
    except:
        return platform.node()


#===================================================================================================================================================================================================
CUSTOM_DEVICE_NAME = "Samsung Galaxy Tab A9"
# ganti sesuai tablet kamu
#===================================================================================================================================================================================================
device_name = get_device_name()

# ================= TEXT =================
canvas.create_text(
    WINDOW_W//2, 255,
    text=device_name,
    font=("SF Pro Display", 18, "bold"),
    fill="#000000"
)

canvas.create_text(
    WINDOW_W//2, 282,
    text=f"Linux • Kernel {kernel}",
    font=("SF Pro Display", 12),
    fill="#666666"
)



canvas.create_text(
    WINDOW_W//2, Y_INFO,
    text=f"Machine   {hostname}",
    font=("SF Pro Display", 12),
    fill="#333333"
)

canvas.create_text(
    WINDOW_W//2, Y_INFO + 22,
    text=f"Architecture   {arch}",
    font=("SF Pro Display", 12),
    fill="#333333"
)




def open_website(event=None):
    webbrowser.open_new("https://bestmomen.com/shop")

# ================= BUTTON =================
# ================= BUTTON =================
BTN_W = 160
BTN_H = 36
BTN_X = WINDOW_W // 2
BTN_Y = 350


# Text tombol
btn_bg = round_rect(
    70, Y_BUTTON-18,
    280, Y_BUTTON+18,
    r=12,
    fill="#E5E5E5"
)

btn_text = canvas.create_text(
    WINDOW_W//2, Y_BUTTON,
    text="Info Lainnya…",
    font=("SF Pro Display", 12),
    fill="#000000"
)


# ================= CLICK ACTION =================
canvas.tag_bind(btn_bg, "<Button-1>", open_website)
canvas.tag_bind(btn_text, "<Button-1>", open_website)


# ================= FOOTER =================
FOOTER_START = Y_BUTTON + BUTTON_FOOTER_GAP

canvas.create_text(
    WINDOW_W // 2,
    FOOTER_START,
    text="Sertifikasi Pengatur",
    font=("SF Pro Display", 11),
    fill="#888888"
)

canvas.create_text(
    WINDOW_W // 2,
    FOOTER_START + 20,
    text="© 2025 Bestmomen",
    font=("SF Pro Display", 10),
    fill="#999999"
)

canvas.create_text(
    WINDOW_W // 2,
    FOOTER_START + 38,
    text="Semua Hak Cipta Dilindungi Undang-Undang.",
    font=("SF Pro Display", 10),
    fill="#AAAAAA"
)


# ================= DRAG WINDOW (BONUS) =================
def start_move(e):
    root.x = e.x
    root.y = e.y

def do_move(e):
    root.geometry(f"+{e.x_root-root.x}+{e.y_root-root.y}")

canvas.bind("<Button-1>", start_move)
canvas.bind("<B1-Motion>", do_move)

# ================= FADE IN =================
def fade_in():
    for i in range(21):
        root.attributes("-alpha", i/20)
        root.update()
        time.sleep(0.015)

fade_in()
root.mainloop()
