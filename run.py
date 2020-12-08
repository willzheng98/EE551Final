import youtube_dl
import subprocess

def run():
    video_url = input("Please enter the Youtube URL: ")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )

    filename = f"{video_info['title']},mp3"

    options = {
        'format': 'bestsudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download(video_info['webpage_url'])

    subprocess.call(["open"])


if __name__ == '__main__':
    run()   
    