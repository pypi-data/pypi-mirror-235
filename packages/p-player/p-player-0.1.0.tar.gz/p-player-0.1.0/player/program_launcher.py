import subprocess
from player.printer import Printer


class ProgramLauncher:
    @staticmethod
    def run_program(program_name, data_manager):
        if program_name in data_manager.data:
            ProgramLauncher.launch_program(
                data_manager.data[program_name], data_manager.data["git_bash"]
            )
        else:
            suggestions = Printer.suggest_programs(program_name, data_manager.data)
            if suggestions:
                print(f"Program '{program_name}' not found. Did you mean one of these?")
                for suggestion in suggestions:
                    print(f" - {suggestion}")
            else:
                print(f"Program '{program_name}' not found in the YAML data.")

    @staticmethod
    def launch_program(path, gitbash_path):
        try:
            if path.endswith(".sh"):
                subprocess.Popen([gitbash_path, path], shell=True)
                print(f"The script {path} has been launched.")
            elif path.endswith(".exe"):
                subprocess.Popen([path])
                print(f"The executable {path} has been launched.")
            else:
                print("File format not supported. Please use a .sh or .exe file.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
