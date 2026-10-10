from simple_image_download import simple_image_download as sim

my_downloader = sim.Downloader()

my_downloader.directory = 'my_dir/'
# Change File extension type
my_downloader.extensions = '.jpg'
print(my_downloader.extensions)

#my_downloader.download('chair', limit=100)
#my_downloader.download('speaker', limit=100)
#my_downloader.download('clock', limit=100)
#my_downloader.download('fans', limit=100)
my_downloader.download('rose', limit=100)