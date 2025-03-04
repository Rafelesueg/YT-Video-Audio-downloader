import yt_dlp
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox

ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

# Verifica se FFmpeg è accessibile
if not os.path.exists(ffmpeg_path):
    raise FileNotFoundError("FFmpeg non trovato! Assicurati che ffmpeg.exe sia nella cartella del programma.")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class YouTubeDownloader(ctk.CTk):
    def __init__(self):
        super().__init__()

        window_width = 600
        window_height = 320
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.title("YouTube Downloader")
        self.resizable(False, False)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.sidebar.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar, text="Menu", font=("Arial", 24, "bold"))
        self.logo_label.grid(row=0, column=0, pady=30, padx=20)

        self.format_var = ctk.StringVar(value="video")
        self.video_button = ctk.CTkButton(self.sidebar, text="Video", command=lambda: self.set_format("video"))
        self.video_button.grid(row=1, column=0, pady=20, padx=20, sticky="ew")

        self.audio_button = ctk.CTkButton(self.sidebar, text="Audio", command=lambda: self.set_format("audio"))
        self.audio_button.grid(row=2, column=0, pady=20, padx=20, sticky="ew")

        self.content = ctk.CTkFrame(self)
        self.content.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.url_label = ctk.CTkLabel(self.content, text="Enter video URL:", font=("Arial", 18))
        self.url_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.url_entry = ctk.CTkEntry(self.content, width=400, placeholder_text="Paste the URL here...", font=("Arial", 16))
        self.url_entry.grid(row=1, column=0, padx=10, pady=5)

        self.format_label = ctk.CTkLabel(self.content, text="Format:", font=("Arial", 16))
        self.format_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.format_options = ctk.CTkComboBox(self.content, values=["mp4", "webm", "mkv"], state="readonly", font=("Arial", 16))
        self.format_options.grid(row=3, column=0, padx=10, pady=5)
        self.format_options.set("mp4")

        self.download_button = ctk.CTkButton(self.content, text="Download", command=self.download, font=("Arial", 16))
        self.download_button.grid(row=4, column=0, padx=10, pady=15)

        self.status_label = ctk.CTkLabel(self.content, text="", font=("Arial", 16))
        self.status_label.grid(row=5, column=0, padx=10, pady=5)

    def set_format(self, format):
        self.format_var.set(format)
        if format == "video":
            self.format_options.configure(values=["mp4", "webm", "mkv"])
            self.format_options.set("mp4")
        else:
            self.format_options.configure(values=["mp3", "aac", "flac", "wav", "ogg"])
            self.format_options.set("mp3")

    def download(self):
        url = self.url_entry.get().strip()
        format = self.format_var.get()
        extension = self.format_options.get()

        if not url:
            messagebox.showwarning("Error", "Please enter a valid URL!")
            return

        folder = filedialog.askdirectory(title="Select Save Folder")
        if not folder:
            return

        self.status_label.configure(text="Downloading...", text_color="yellow")
        self.update_idletasks()

        options = {
            'outtmpl': os.path.join(folder, f'[{format.upper()}] %(title)s.%(ext)s'),
            'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/best',
            'merge_output_format': 'mp4',
            'keepvideo': False
        }

        if format == "audio":
            options['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': extension,
                'preferredquality': '192',
            }]

        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])
            self.status_label.configure(text="Download completed!", text_color="green")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")
            self.status_label.configure(text="Download error", text_color="red")

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()
