import inquirer


class Printer:
    @staticmethod
    def print_list(data):
        if data:
            print("List of program names:")
            for program_name in sorted(data.keys()):
                print(f" - {program_name}")
        else:
            print("No data found in the YAML file.")

    @staticmethod
    def print_long_list(data):
        if data:
            max_program_name_length = max(
                len(program_name) for program_name in data.keys()
            )
            print("List of program names:")
            for program_name, program_path in sorted(data.items()):
                print(f" - {program_name.ljust(max_program_name_length)} : {program_path}")
        else:
            print("No data found in the YAML file.")

    @staticmethod
    def suggest_programs(partial_name, data):
        suggestions = [key for key in data.keys() if partial_name in key]
        return suggestions

    @staticmethod
    def ask_git_bash_path():
        questions = [
            inquirer.Text("git_bash_path", message="Enter the path to Git Bash")
        ]
        answers = inquirer.prompt(questions)
        return answers["git_bash_path"]
