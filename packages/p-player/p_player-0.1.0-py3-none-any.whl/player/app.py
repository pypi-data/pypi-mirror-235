"""Player App

This script provides a command-line interface for launching programs or scripts specified by name. 
It allows users to list available programs, execute programs, and manage settings for Git Bash and data storage.

Usage:
    - To list available programs: player -l
    - To list program names and paths: player -ll
    - To run a specific program by name: player <program_name>
    - To initialize or update settings: player --init
    - To edit the data file with the default editor: player -ef

Note: This script requires a data.yaml file to store program information, and a program_launcher.py module 
to launch programs.
"""


import argparse

from player.const import DATA_FILE
from player.data_manager import DataManager
from player.program_launcher import ProgramLauncher
from player.printer import Printer


class App:
    """class for manage inputs"""

    def __init__(self):
        """Initialize the App class."""
        self.data_manager = DataManager(DATA_FILE)

    def run(self):
        """Run the application."""
        parser = argparse.ArgumentParser(
            description="Launch a program or script specified by name"
        )
        parser.add_argument(
            "program_name",
            default=None,
            nargs="?",
            help="Name of the program to launch",
        )
        parser.add_argument(
            "-l", "--list", action="store_true", help="List program names"
        )
        parser.add_argument(
            "-ll",
            "--long-list",
            action="store_true",
            help="List program names and paths",
        )
        parser.add_argument(
            "--init", action="store_true", help="Initialize or update data.yaml"
        )
        parser.add_argument(
            "-ef",
            "--edit-file",
            action="store_true",
            help="Edit data file .yaml with default editor",
        )

        args = parser.parse_args()

        if args.init:
            self.initialize_data()
        elif args.edit_file:
            self.data_manager.edit_data_file()
        else:
            self.data_manager.load_data()

            if args.list:
                Printer.print_list(self.data_manager.data)
            elif args.long_list:
                Printer.print_long_list(self.data_manager.data)
            elif args.program_name:
                ProgramLauncher.run_program(args.program_name, self.data_manager)
            else:
                print("No program specified. Use -h or --help for usage information.")

    def initialize_data(self):
        """Initialize data."""
        git_bash_path = Printer.ask_git_bash_path()
        self.data_manager.create_or_update_data_file(git_bash_path)
        print(f"Git Bash path has been updated: {git_bash_path}")


def main():
    """Main function"""
    app = App()
    app.run()


if __name__ == "__main__":
    main()
