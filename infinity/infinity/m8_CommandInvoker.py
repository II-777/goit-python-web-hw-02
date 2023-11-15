from m5_Commands import Help, \
    Exit, \
    Clear, \
    AddRecord, \
    UpdateRecord, \
    DeleteRecord, \
    SearchRecord, \
    ShowAllRecords, \
    Note


class CommandInvoker:
    '''Invokes commands from the Commands module'''

    def __init__(self):
        self.commands = {
            'help': Help(),                            # General command
            'exit': Exit(),                            # General command
            'clear': Clear(),                          # General command
            'add record': AddRecord(),                 # AddressBook command
            'update record': UpdateRecord(),           # AddressBook command
            'delete record': DeleteRecord(),           # AddressBook command
            'search record': SearchRecord(),           # AddressBook command
            'show all': ShowAllRecords(),              # AddressBook command
            'note': Note(),                            # Notebook command
        }

    def execute(self, bot, parsed_data, *args, **kwargs):
        if parsed_data.get('command') in self.commands:
            self.commands[parsed_data.get('command')].execute(
                bot, parsed_data, *args, **kwargs)


if __name__ == '__main__':
    pass
