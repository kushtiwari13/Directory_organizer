import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

files = os.listdir()
files.remove("organizer.py")
#print(files)
createIfNotExist("Images")
createIfNotExist("Docs")
createIfNotExist("Media")
createIfNotExist("Torrents")
createIfNotExist("ZipFiles")
createIfNotExist("Softwares")
createIfNotExist("Others")

imgExts = [".png" , ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts= [".txt", ".docx", "doc", ".pdf", ".csv", ".xlsx"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp4", ".mp3", ".flv", ".webm", ".mkv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

torrentExts = [".torrent"]
torrent = [file for file in files if os.path.splitext(file)[1].lower() in torrentExts]

zipExts = [".zip"]
zip = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]

softwareExts = [".exe", ".msi"]
software = [file for file in files if os.path.splitext(file)[1].lower() in softwareExts]


others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in torrentExts) and os.path.isfile(file):
        others.append(file)
#print(others)



# for media in medias:
#     os.replace(media, f"Media/{media}")

move("Images", images)
move("Docs", docs)
move("Media", medias)
move("Torrents", torrent)
move("ZipFiles", zip)
#move("Softwares", software)
move("Others", others)