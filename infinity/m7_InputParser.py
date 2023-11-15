from m6_InputSanitizer import SanitizeInput
from m8_CommandInvoker import CommandInvoker
import re
import shlex


class InputParser:
    '''Parses user input'''

    def __init__(self):
        self.parsed_command = None
        self.parsed_name = None
        self.parsed_birthday = None
        self.parsed_phones = []
        self.parsed_emails = []
        self.parsed_tags = []
        self.parsed_new_name = None
        self.parsed_search_query = None
        self.parsed_unrecognized = []

    def parse_input(self, user_input):
        self.reset_parser()

        if not user_input:
            print('[-] Unrecognized command. Try "help".')
            return {}

        user_input_lower = user_input.lower()

        for key in CommandInvoker().commands:
            if user_input_lower.startswith(key.lower()):
                self.parsed_command = key
                rest_of_string = user_input[len(self.parsed_command):].strip()
                break
        else:
            print('[-] Unrecognized command. Try "help".')
            return {}

        arguments = shlex.split(rest_of_string)

        if self.parsed_command in ["help", "exit", "show all records", "show all notes"]:
            self.parse_no_args(arguments)
        elif self.parsed_command in ["search record", "search note", "show records page", "show notes page"]:
            self.parse_search(arguments)
        elif self.parsed_command in ["update record", "change note"]:
            self.parse_change(arguments)
        else:
            self.parse_multi_args(arguments)

        if self.parsed_unrecognized:
            print('[!] Extraneous arguments detected. Review parser debug output.')

        return {
            'command': self.parsed_command,
            'name': self.parsed_name,
            'birthday': self.parsed_birthday,
            'phones': self.parsed_phones,
            'emails': self.parsed_emails,
            'tags': self.parsed_tags,
            'new_name': self.parsed_new_name,
            'search_query': self.parsed_search_query,
            'unrecognized': self.parsed_unrecognized
        }

    def reset_parser(self):
        self.parsed_command = None
        self.parsed_name = None
        self.parsed_birthday = None
        self.parsed_phones = []
        self.parsed_emails = []
        self.parsed_tags = []
        self.parsed_new_name = None
        self.parsed_search_query = None
        self.parsed_unrecognized = []

    def parse_no_args(self, arguments):
        self.parsed_unrecognized = arguments

    def parse_search(self, arguments):
        if arguments:
            self.parsed_search_query = arguments[0]
            self.parsed_unrecognized = arguments[1:]
        else:
            self.parsed_search_query = None
            self.parsed_unrecognized = []

    def parse_change(self, arguments):
        for arg in arguments:
            if not self.parsed_name and re.match(r'^[a-zA-Z\-\_ ]+$', arg):
                self.parsed_name = arg
            elif self.parsed_name and not self.parsed_new_name and re.match(r'^[a-zA-Z\-\_ ]+$', arg):
                self.parsed_new_name = arg
            elif not self.parsed_birthday and re.match(r'^(?=.{1,10}$)\d{4}[^0-9]+\d{2}[^0-9]+\d{2}$', arg):
                self.parsed_birthday = SanitizeInput.sanitize_date(arg)
            elif re.match(r'^(?:\+?\d*-*\(*\d\)*-*\d*){11}\d*$', arg):
                self.parsed_phones.append(SanitizeInput.sanitize_phone(arg))
            elif re.match(r'^[a-zAZ0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', arg):
                self.parsed_emails.append(arg)
            elif re.match(r'^#[a-zA-Z0-9\-\_]+$', arg):
                self.parsed_tags.append(arg)
            else:
                self.parsed_unrecognized.append(arg)

    def parse_multi_args(self, arguments):
        for arg in arguments:
            if not self.parsed_name and re.match(r'^[a-zA-Z\-\_ ]+$', arg):
                self.parsed_name = arg
            elif not self.parsed_birthday and re.match(r'^(?=.{1,10}$)\d{4}[^0-9]+\d{2}[^0-9]+\d{2}$', arg):
                self.parsed_birthday = SanitizeInput.sanitize_date(arg)
            elif re.match(r'^(?:\+?\d*-*\(*\d\)*-*\d*){11}\d*$', arg):
                self.parsed_phones.append(SanitizeInput.sanitize_phone(arg))
            elif re.match(r'^[a-zAZ0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zAZ0-9-.]+$', arg):
                self.parsed_emails.append(arg)
            elif re.match(r'^#[a-zA-Z0-9\-\_]+$', arg):
                self.parsed_tags.append(arg)
            else:
                self.parsed_unrecognized.append(arg)


if __name__ == '__main__':
    pass
