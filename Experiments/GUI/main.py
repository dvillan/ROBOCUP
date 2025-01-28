from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk
import cProfile, time, threading, os

ct.set_appearance_mode("dark")
root = ct.CTk(fg_color="black")
root.resizable(True, True)
root.geometry("720x640")
root.title("Rescue")
root.iconbitmap("gmail.ico")

class LoadingApp:
    def __init__(self, root):
        self.root = root

        theme = "dark" 
        threading.Thread(target=self.get_gui).start()
        threading.Thread(target=self.load_data).start()

    def get_gui(self):
        self.loaded = False

        self.loading_frame = ct.CTkFrame(root, fg_color="black")
        self.loading_frame.pack(fill=BOTH, expand=True)

        self.progress_frame = ct.CTkFrame(self.loading_frame, fg_color="black")
        self.progress_frame.pack(fill=BOTH, expand=True, padx=200, pady=40)

        logo_src = Image.open("images\\icons8-gmail-480.png")
        logo_img = ImageTk.PhotoImage(logo_src.resize((300, 300)))
        ct.CTkLabel(self.progress_frame, text="", image=logo_img, compound=LEFT, text_color="white").pack(pady=10)       

        self.progressbar = ct.CTkProgressBar(self.progress_frame, orientation="horizontal", width=350, mode="determinate", determinate_speed=0.5, fg_color="gray", height=7, progress_color="#1e5bf1", corner_radius=1)
        self.progressbar.start()
        self.progressbar.set(0)
        self.progressbar.pack(side=TOP, pady=20)

        self.label = ct.CTkLabel(self.progress_frame, text="Initializing robot...", font=("Poppins", 30, "normal"), compound=LEFT, text_color="white").pack(pady=5)

    def load_data(self):
        time.sleep(3.4)
        self.loaded = True
        self.hide_loading()
        self.main()

    def hide_loading(self):
        self.progressbar.stop()
        self.loading_frame.destroy()

    def destroy_loader(self):
        if not self.loaded:
            self.hide_loading()
        else:
            pass

    def main(self):
        self.root.resizable(True, True)
        ct.CTkLabel(self.root, text="Welcome User", text_color="white", font=("monospace", 50, "bold")).pack(side=TOP, pady=80)

LoadingApp(root)

root.mainloop()