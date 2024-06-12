import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube, Playlist
import os
import re

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def download_video(url, directory_path):
    try:
        yt = YouTube(url)
        selected_res = resolution.get()
        streams = yt.streams.filter(res=selected_res)

        if streams:
            print(f"Video: {yt.title}")
            print(f"Download started, selected resolution: {selected_res}.")
            video_file = streams.first().download(directory_path)
            sanitized_title = sanitize_filename(yt.title)
            new_video_title = f"VIDEO_{sanitized_title}_{selected_res}.mp4"
            new_video_path = os.path.join(directory_path, new_video_title)
            os.rename(video_file, new_video_path)
            print(f"Download completed! {selected_res}")
            #messagebox.showinfo("Success", f"Video downloaded successfully in {selected_res}:\n{yt.title}")
            return

        print(f"No video available in the selected resolution ({selected_res}). Downloading the best quality video available.")
        resolutions = ["2160p", "1440p", "1080p", "720p", "480p", "360p", "144p"]
        for res in resolutions:
            streams = yt.streams.filter(res=res)
            if streams:
                print(f"Video: {yt.title}")
                print(f"Download started, best resolution found: {res}.")
                video_file = streams.first().download(directory_path)
                sanitized_title = sanitize_filename(yt.title)
                new_video_title = f"VIDEO_{sanitized_title}_{res}.mp4"
                new_video_path = os.path.join(directory_path, new_video_title)
                os.rename(video_file, new_video_path)
                print(f"Download completed! {res}")
                #messagebox.showinfo("Success", f"Video downloaded successfully in {res}:\n{yt.title}")
                return

        messagebox.showerror("Error", "No video streams available in resolution above or equal to 720p.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during video download:\n{e}")

def download_audio(url, directory_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        if stream:
            print(f"Download audio started: {yt.title}")
            audio_file = stream.download(output_path=directory_path)
            sanitized_title = sanitize_filename(yt.title)
            audio_title = "AUDIO_" + sanitized_title + ".mp3"
            new_audio_path = os.path.join(directory_path, audio_title)
            os.rename(audio_file, new_audio_path)
            print("Download completed!")
            #messagebox.showinfo("Success", f"Audio downloaded successfully:\n{yt.title}")
        else:
            messagebox.showerror("Error", "No audio available in MP3 format.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during audio download:\n{e}")

def download_video_or_audio(is_audio=False):
    directory_path = filedialog.askdirectory()

    if not directory_path:
        return
    print("Directory saved, ready to download...")

    url = link.get()
    if not url or not (url.startswith("https://www.youtube.com/") or url.startswith("youtube.com")):
        messagebox.showerror("Error", "Insert a valid YouTube URL!")
        return

    if 'playlist' in url:
        print("Playlist detected.")
        pl = Playlist(url)
        for video_url in pl.video_urls:
            if is_audio:
                download_audio(video_url, directory_path)
            else:
                download_video(video_url, directory_path)
    else:
        print("Single video detected.")
        if is_audio:
            download_audio(url, directory_path)
        else:
            download_video(url, directory_path)

bg_color = "#00103C"
fg_color = "white"

window = tk.Tk()
window.title("Video&Audio Downloader")
window.geometry('640x480')
window.config(bg=bg_color)

print("YouTube video&audio downloader by Rafelesueg\nGithub:https://github.com/Rafelesueg\n\n")
print("Debug console:")

label = tk.Label(window,
                 text="YOUTUBE VIDEO&AUDIO DOWNLOADER",
                 bg=bg_color,
                 fg=fg_color,
                 font=("Arial", 20, 'bold'))
label.pack(fill='x', pady=10)

entry_text = tk.Label(window,
                      text="Insert link",
                      bg=bg_color,
                      fg=fg_color,
                      font=('Arial', 16, 'bold'))
entry_text.pack(fill='x')

link = tk.Entry(window,
                cursor='hand2',
                bg="#09235E",
                fg=fg_color,
                highlightthickness=0,
                bd=0,
                font=('Arial', 14))
link.pack(fill='x', padx=20, pady=10)

resolution = tk.StringVar(value="720p")

res_label = tk.Label(window,
                     text="Select resolution",
                     bg=bg_color,
                     fg=fg_color,
                     activebackground=bg_color,
                     font=('Arial', 14, 'bold'))
res_label.pack()

res_options = ["2160p", "1440p", "1080p", "720p"]
for res in res_options:
    tk.Radiobutton(window, text=res, variable=resolution, value=res,
                   bg=bg_color, fg=fg_color, selectcolor=bg_color, activebackground=bg_color, activeforeground=fg_color,
                   font=('Arial', 12, 'bold')).pack()

info_label = tk.Label(text="WARNING: Video up to 720p does not include audio, you must download it separately!",
                      bg=bg_color, fg=fg_color,
                      font=('Arial', 10, 'bold'))
info_label.pack(pady=10)

download_video_button = tk.Button(window,
                                  text="Download video",
                                  bg='#FF4D00',
                                  fg=fg_color,
                                  activebackground='#FF4D00',
                                  activeforeground=fg_color,
                                  highlightthickness=5,
                                  bd=0,
                                  font=("Arial", 14, 'bold'),
                                  command=lambda: download_video_or_audio(is_audio=False))
download_video_button.pack(padx=50, pady=20)

download_audio_button = tk.Button(window,
                                  text="Download audio",
                                  bg='#14452F',
                                  fg=fg_color,
                                  activebackground='#14452F',
                                  activeforeground=fg_color,
                                  highlightthickness=5,
                                  bd=0,
                                  font=("Arial", 14, 'bold'),
                                  command=lambda: download_video_or_audio(is_audio=True))
download_audio_button.pack(padx=50, pady=10)

window.mainloop()
