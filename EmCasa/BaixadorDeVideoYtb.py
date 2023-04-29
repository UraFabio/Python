import pytube

download_loc = './'

video_url = input('Digite a URL: ')

video_instance = pytube.YouTube(video_url)

Stream = video_instance.streams.get_highest_resolution()
Stream.download()