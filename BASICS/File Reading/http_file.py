import yt_dlp

# Example URL
url = "https://youtu.be/MmpVAy35W0k?si=ZHVOZFEPrKI-ci9c"

# Set options for MP4 download
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Best MP4 video and audio
    'merge_output_format': 'mp4',  # Ensure output format is MP4
    'outtmpl': 'example_video.mp4',  # Output file name
}

# Download video as MP4
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully!")

