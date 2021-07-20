import os

def iffoldernotexist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")



files = os.listdir()
files.remove("file_slotter.py")
iffoldernotexist("images")
iffoldernotexist("medias")
iffoldernotexist("docs")
iffoldernotexist("softwares")
iffoldernotexist("others")

images = []

for file in files :
    imgexts = [".jpg", ".jpeg", ".png"]
    if os.path.splitext(file)[1].lower() in imgexts :
        images.append(file)

move("images", images)

medias = []
for file in files:
    medexts = [".mp4", ".mp3", ".gif", ".mkv", ".flv", ".m4a"]
    if os.path.splitext(file)[1].lower() in medexts :
        medias.append(file)

move("medias", medias)

docs = []
for file in files:
    docexts = [".doc", ".docx", ".pdf", ".ppt"]
    if os.path.splitext(file)[1].lower() in docexts:
        docs.append(file)

move("docs", docs)

softwares = []
for file in files:
    softexts = [".exe"]
    if os.path.splitext(file)[1].lower() in softexts:
        softwares.append(file)

move("softwares", softwares)

others = []
for file in files:
    exts = os.path.splitext(file)[1].lower()
    if (exts not in imgexts) and (exts not in docexts) and (exts not in softexts) and os.path.isfile(file):
        others.append(file)

move("others", others)
