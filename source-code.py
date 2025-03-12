import os
import shutil

# Dossier source contenant les fichiers à organiser
source_folder = source_folder = "E:\\Python Scripts


file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Vidéos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
    'Musique': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.7z']
}

# Fonction pour organiser les fichiers
def organize_files(source_folder):
    # Si le dossier source n'existe pas, afficher un message d'erreur
    if not os.path.exists(source_folder):
        print(f"Le dossier spécifié '{source_folder}' n'existe pas.")
        return

    # Créer des sous-dossiers pour chaque type de fichier s'ils n'existent pas
    for folder_name in file_types:
        folder_path = os.path.join(source_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Parcourir les fichiers dans le dossier source
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Vérifier si c'est un fichier
        if os.path.isfile(file_path):
            moved = False
            # Vérifier les extensions des fichiers et les déplacer vers le bon dossier
            for folder_name, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    destination_folder = os.path.join(source_folder, folder_name)
                    destination_path = os.path.join(destination_folder, filename)
                    
                    # Déplacer le fichier
                    shutil.move(file_path, destination_path)
                    print(f"Le fichier '{filename}' a été déplacé vers '{folder_name}'.")
                    moved = True
                    break

            # Si le fichier ne correspond à aucun type défini, le déplacer dans 'Autres'
            if not moved:
                other_folder = os.path.join(source_folder, 'Autres')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                destination_path = os.path.join(other_folder, filename)
                shutil.move(file_path, destination_path)
                print(f"Le fichier '{filename}' a été déplacé vers 'Autres'.")

# Lancer la fonction
organize_files(source_folder)
