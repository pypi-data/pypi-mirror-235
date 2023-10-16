from setuptools import setup, find_packages



files = {
    "version": "VERSION",
    "requirements": "requirements.txt"
}

data = {
    "name": "p-player",
    "tag_run": "pl"
}

# Lire le contenu de chaque fichier spécifié dans "files"
for key, file_name in files.items():
    with open(file_name, "r") as file:
        data[key] = file.read()

print(data)
    

setup(
    name=data["name"],  # Remplacez 'monpackage' par le nom de votre package
    version=data["version"],
    packages=find_packages(include=["player"]),
    install_requires=data["requirements"].splitlines(),
    entry_points={
        'console_scripts': [
            f'{data["tag_run"]} = player.app:main',
        ],
    },
)
