from pathlib import Path

chemin =Path.cwd().parent #comme je suis déjà dans un sous-dossiers
nouvo_dossier = chemin /"Organiser_donnees"

nouvo_dossier.mkdir(exist_ok=True)