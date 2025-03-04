
# YouTube Downloader Application

![alt text](https://i.imgur.com/UwLXD0I_d.webp?maxwidth=760&fidelity=grand)

## Description

This project is a simple YouTube downloader GUI application built using **yt-dlp**, **customtkinter**. The app allows users to download videos or audio from YouTube in different formats (mp4, webm, mkv for video, and mp3, aac, flac, wav, ogg for audio). The user can input the YouTube video URL, choose the download format, and select the destination folder.

## Features

- **Video & Audio Downloads:** Allows downloading videos and audio from YouTube in multiple formats.
- **GUI Interface:** The application uses `customtkinter` to create a modern-looking, dark mode interface with an intuitive layout.
- **Error Handling:** If the user inputs an invalid URL or if an error occurs during the download, the app shows appropriate error messages.

## Libraries Used

### yt-dlp

**yt-dlp** is a command-line program to download videos from YouTube and other sites. It is a fork of `youtube-dl` that provides additional features and fixes. In this project, **yt-dlp** is used to handle the video/audio downloading process.

- **Documentation:** [yt-dlp GitHub Repository](https://github.com/yt-dlp/yt-dlp)

### customtkinter

**customtkinter** is a modern and customizable version of Tkinter, providing additional widgets, themes, and features to create better user interfaces. In this project, we use **customtkinter** to create a dark-themed graphical user interface (GUI) for the YouTube downloader.

- **Documentation:** [customtkinter GitHub Repository](https://github.com/TomSchimansky/CustomTkinter)

## Setup Instructions

1. Install the necessary dependencies:
    ```bash
    pip install yt-dlp customtkinter
    ```
    [FFMPEG](https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-2025-03-03-git-d21ed2298e-full_build.7z)
    EXTRACT from BIN folder the ffmpeg.exe and put inside the repository folder

2. Save the provided Python script in a `.py` file and run it.

3. The application will launch with the following options:
    - **Video / Audio:** Choose whether you want to download a video or audio.
    - **Video Formats:** Available video formats: mp4, webm, mkv.
    - **Audio Formats:** Available audio formats: mp3, aac, flac, wav, ogg.
    - **URL Input:** Paste the URL of the YouTube video you want to download.
    - **Download Folder:** Select the folder where the downloaded content should be saved.
