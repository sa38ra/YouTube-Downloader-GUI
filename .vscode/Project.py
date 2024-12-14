from tkinter import *
from tkinter import messagebox
from yt_dlp import YoutubeDL
from PIL import Image, ImageTk

# Function to download video or audio
def download_video(resolution="high", is_audio=False):
    url = url_entry.get()  # Get the URL from the entry field
    save_path = filename_entry.get()  # Get the filename from the entry field

    if not url or not save_path:
        messagebox.showerror("Error", "Please enter both URL and filename.")
        return

    # Define the download options
    ydl_opts = {
        'outtmpl': f'downloads/{save_path}-%(title)s.%(ext)s',  # File output template
        'quiet': True,  # Suppress unnecessary output
    }

    # Adjust options based on user choice
    if is_audio:
        ydl_opts['format'] = 'bestaudio/best'  # Best audio only
    else:
        if resolution == "high":
            ydl_opts['format'] = 'bestvideo+bestaudio/best'  # Best video and audio
        elif resolution == "low":
            ydl_opts['format'] = 'worstvideo+bestaudio/worst'  # Low quality video

    try:
        # Use YoutubeDL to download
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Download completed: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the GUI
root = Tk()
root.title("YouTube Downloader")
root.geometry("600x650")
root.configure(bg="#e6f2ff")

# Load and display a logo image
try:
    logo_image = Image.open("social-media-logo-design/10464410.png")
    logo_image = logo_image.resize((100, 100), Image.Resampling.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = Label(root, image=logo_photo, bg="#e6f2ff")
    logo_label.pack(pady=15)
except:
    logo_label = Label(root, text="YouTube Downloader", font=("Arial", 20, "bold"), bg="#e6f2ff")
    logo_label.pack(pady=15)

# URL input field
url_label = Label(root, text="Enter Video URL:", font=("Arial", 12), bg="#e6f2ff", fg="#333")
url_label.pack(pady=10)
url_entry = Entry(root, width=50, font=("Arial", 12), bg="#f0f8ff", fg="#333", borderwidth=2, relief="solid")
url_entry.pack(pady=5)

# Filename input field
filename_label = Label(root, text="Enter Filename to Save As:", font=("Arial", 12), bg="#e6f2ff", fg="#333")
filename_label.pack(pady=6)
filename_entry = Entry(root, width=50, font=("Arial", 12), bg="#f0f8ff", fg="#333", borderwidth=2, relief="solid")
filename_entry.pack(pady=5)

# Buttons for download options
low_res_button = Button(root, text="Download Low Res Video", 
                        width=30, height=2, font=("Arial", 12), 
                        bg="#ff6666", fg="#fff", borderwidth=2, relief="raised", 
                        command=lambda: download_video("low"))
low_res_button.pack(pady=10)

high_res_button = Button(root, text="Download High Res Video", 
                         width=30, height=2, font=("Arial", 12), 
                         bg="#66b3ff", fg="#fff", borderwidth=2, relief="raised", 
                         command=lambda: download_video("high"))
high_res_button.pack(pady=10)

audio_button = Button(root, text="Download Audio Only", 
                       width=30, height=2, font=("Arial", 12), 
                       bg="#99ff99", fg="#fff", borderwidth=2, relief="raised", 
                       command=lambda: download_video(is_audio=True))
audio_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
