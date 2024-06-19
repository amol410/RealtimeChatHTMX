from pytube import YouTube

link = YouTube("https://www.youtube.com/watch?v=SQ4A7Q6_md8")

video = link.streams.get_highest_resolution()

video.download("D:\Python Courses")