import readline
from m4_Exceptions import input_error
from m2_AddressBook import AddressBook
from m7_InputParser import InputParser, CommandInvoker
from m9_UserInterface import ConsoleUserInterface


@input_error
class Bot:
    '''CLI user interface'''

    csv_file = 'contacts.csv'
    address_book = AddressBook()
    input_parser = InputParser()
    command_invoker = CommandInvoker()
    ui = ConsoleUserInterface()

    address_book.check_csv_file(csv_file)
    address_book.load_from_csv(csv_file)

    @classmethod
    def complete_command(cls, text, state):
        """
        Command completion function
        """
        options = [
            parsed_command for parsed_command in cls.command_invoker.commands if parsed_command.startswith(text)]
        if state < len(options):
            return options[state]
        else:
            return None

    @classmethod
    def run(cls, user_input=None):
        """
        Prompt the user for input and process it
        """

        # Set tab completion function
        readline.parse_and_bind("tab: complete")
        readline.set_completer(cls.complete_command)

        # Start an infinite loop for taking user input commands
        while True:
            try:
                # Print an information message
                print(
                    "[i] Enter a parsed_command or press Ctrl+L to clear or Ctrl+C to exit.")

                # Use colorized prompt
                prompt = '\033[32;49m>>> \033[0m'

                # Accept user input and store it in a variable
                user_input = input(prompt)

                # Parse the user input
                parsed_data = cls.input_parser.parse_input(user_input)

                # Check if a valid command is entered
                if parsed_data.get('command'):
                    # Execute a valid command
                    cls.command_invoker.execute(cls, parsed_data)
                else:
                    # Execute a valid command
                    print(f'[input] {user_input}',
                          '[-] Invalid input. Try help.', sep='\n')
            except KeyboardInterrupt:
                print("")
                cls.address_book.save_to_csv(cls.csv_file)
                print("[+] Exiting ...")
                exit(0)


def main():
    Bot().run()


if __name__ == "__main__":
    main()
