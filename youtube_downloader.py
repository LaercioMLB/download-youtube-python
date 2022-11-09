from pytube import YouTube

link="https://www.youtube.com/watch?v=8YUTQkSZh-k"

youtube = YouTube(link)

print("Titulo: " + youtube.title)

res_youtube_max = youtube.streams.get_highest_resolution()

res_youtube_max.download()