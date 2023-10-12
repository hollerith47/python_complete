from pathlib import Path

filtre ={".mp3": "Musique",
         ".wav": "Musiaue",
         ".flac": "Musique",
         ".avi": "Videos",
         ".mp4": "Videos",
         ".gif": "Videos",
         ".bmp": "Images",
         ".png": "Images",
         ".jpg": "Images",
         ".txt": "Documents",
         ".pptx": "Documents",
         ".csv": "Documents",
         ".xls": "Documents",
         ".odp": "Documents",
         ".pages": "Documents"}
tri_dir_data = Path.cwd()/"data"
fichiers =[f for f in tri_dir_data.iterdir() if f.is_file]
for fichier in fichiers :
    dossier_sorti = tri_dir_data / filtre.get(fichier.suffix, "Divers")
    dossier_sorti.mkdir(exist_ok=True)
    fichier.rename(dossier_sorti / fichier.name)
print()