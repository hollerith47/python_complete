import os

filesdirs = os.listdir('.')
for fd in filesdirs:
    if os.path.isfile(fd):
        print(fd)
    
if not os.path.exists("Folder1"):
    os.makedirs("Folder1")
else:
    os.removedirs("Folder1")