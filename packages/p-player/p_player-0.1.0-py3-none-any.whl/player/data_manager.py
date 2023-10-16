"""
player.data_manager

This module provides the DataManager class for managing program data stored in a YAML file.

The DataManager class offers methods to load, create, or update data stored in a YAML file.
It also supports editing the data file with various text editors.
"""

import subprocess
import os
import yaml



class DataManager:
    """DataManager class for managing program data stored in a YAML file.

    This class provides methods to load, create, or update data stored in a YAML file.
    It also supports editing the data file with various editors.
    """

    def __init__(self, data_file):
        """
        Initializes a DataManager instance.

        Args:
            data_file (str): The path to the data YAML file.
        """
        self.data_file = os.path.join(os.path.dirname(__file__), data_file)
        self.data = {}

    def load_data(self):
        """
        Load program data from the YAML file.
        If the file does not exist or is empty, an empty dictionary is assigned to data.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as file:
                yaml_data = yaml.safe_load(file)
                if yaml_data is not None:
                    self.data = yaml_data
                else:
                    self.data = (
                        {}
                    )  # Le fichier est vide ou ne contient pas de données valides
        else:
            self.data = {}  # Le fichier n'existe pas

    def create_or_update_data_file(self, git_bash_path):
        """
        Create or update the data file with the provided Git Bash path.

        Args:
            git_bash_path (str): The path to Git Bash.
        """
        self.load_data()
        self.data["git_bash"] = git_bash_path
        with open(self.data_file, "w", encoding="utf-8") as file:
            yaml.dump(self.data, file)

    def edit_data_file(self):
        """
        Edit the data file with various text editors.

        If the data file does not exist, it is created.
        It attempts to open the file with a list of editors and stops at the first successful attempt.
        """
        if not os.path.exists(self.data_file):
            # Créez le fichier s'il n'existe pas
            with open(self.data_file, "w", encoding="utf-8"):
                pass

        editors = ["toto", "code", "notepad", "blocnote"]

        for editor in editors:
            try:
                process = subprocess.Popen(
                    [editor, self.data_file],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True,
                )
                _, stderr = process.communicate()
                if process.returncode == 0:
                    break  # Sort de la boucle si l'éditeur fonctionne
                if stderr:
                    print(
                        f"An error occurred while opening {editor}: {stderr.decode('utf-8')}"
                    )
            except Exception as e:
                print(f"An error occurred while opening {editor}: {str(e)}")
