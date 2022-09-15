from pytube import YouTube

link = str(input("Enter the link of your Video : "))

# link = "https://www.youtube.com/watch?v=mNEUkkoUoIA"

youTube_01 = YouTube(link)

# print(youTube_01.title,end="\n")
# print(youTube_01.thumbnail_url,end="\n")

videos = youTube_01.streams.all()

# videos = youTube_01.streams.filter(only_audio=True)

vid = list(enumerate(videos))

for i in vid:
    print(i)

print("\n")

strm = int(input("Choose from above index numbers: "))

videos[strm].download()

print("\n\n\n\n")
print("="*24)
print("Download Successfully")