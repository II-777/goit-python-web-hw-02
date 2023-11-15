from abc import ABC, abstractmethod
from m1_Record import Record
from m3_NoteBook import note_book
import os


class Command(ABC):
    @abstractmethod
    def execute(self, bot, *args, **kwargs):
        pass


class Help(Command):
    '''
    Show help message
    '''

    def execute(self, bot, *args, **kwargs):
        print('[+] Available commands: ')
        for cmd_name, cmd in bot.command_invoker.commands.items():
            docstring = cmd.__doc__
            print(f"\033[32;49m{cmd_name}\033[0m {docstring}")


class Exit(Command):
    '''
    Exit from application
    '''

    def execute(self, bot, *args, **kwargs):
        bot.address_book.save_to_csv(bot.csv_file)
        print('[+] Exiting...')
        exit(0)


class Clear(Command):
    '''
    Clear the screen
    '''

    def execute(self, bot, *args, **kwargs):
        os.system('cls' if os.name == 'nt' else 'clear')


class ShowAllRecords(Command):
    '''
    Show all records in the AddressBook
    '''

    def execute(self, bot, *args, **kwargs):
        try:
            bot.ui.show_contacts(bot)
        except Exception as e:
            print(f"[-] {e}. Using a fallback user interace.")
            bot.address_book.show_all_records()


class AddRecord(Command):
    '''
    Add a record to the AddressBook:

    <name>     - 'A-Za-z' string;
    <birthday> - YYYY-MM-DD date;
    <phone>    - 11-digit number;
    <email>    - contains '@' string;
    <tag>      - starts with '#' string;

    Ex.: add record 'John Doe' 2000-01-01 +1(333)777-3377 +1(333)777-3388 john@gmail.com test@test.com #work #test
    '''

    def execute(self, bot, parsed_data):
        if parsed_data['name']:
            if parsed_data['name'] in bot.address_book.data:
                print('[-] Record not added: Name already exists.')
            else:
                record = Record(parsed_data['name'],
                                parsed_data['birthday'],
                                parsed_data['phones'],
                                parsed_data['emails'],
                                parsed_data['tags'])
                try:
                    bot.address_book.add_record(record)
                    print('[+] Record added:', record)
                except Exception as e:
                    print(f'[-] Record not added: {e}')
        else:
            print('[-] Name can\'t be None. Try again.')


class UpdateRecord(Command):
    '''
    Update existing record

    Ex.: update record 'John Doe' 'Jane Doe' 2000-01-01 jane@gmail.com
    '''

    def _update_record_key(self, bot, old_key, new_key, record):
        bot.address_book.data[new_key] = record
        record.name.value = new_key
        del bot.address_book.data[old_key]

    def _update_record_fields(self, record, parsed_data):
        if 'new_name' in parsed_data and parsed_data['new_name']:
            record.update_name = parsed_data['new_name']
        if 'birthday' in parsed_data and parsed_data['birthday']:
            record.update_birthday = parsed_data['birthday']
        if 'phones' in parsed_data and parsed_data['phones']:
            record.update_phones = parsed_data['phones']
        if 'emails' in parsed_data and parsed_data['emails']:
            record.update_emails = parsed_data['emails']
        if 'tags' in parsed_data and parsed_data['tags']:
            record.update_tags = parsed_data['tags']

    def execute(self, bot, parsed_data):
        name = parsed_data.get('name')
        record = bot.address_book.data.get(name)

        try:
            if record:
                new_name = parsed_data.get('new_name')

                if new_name in bot.address_book.data:
                    print(f"[-] Name {new_name} already exists. Try again.")
                    return
                else:
                    if new_name and new_name != name:
                        self._update_record_key(bot, name, new_name, record)

                self._update_record_fields(record, parsed_data)
                print('[+] Record Updated: ', record)
                return
            else:
                print('[-] Record not found.')
        except Exception as e:
            print(f'[-] Update failed: {e}')


class DeleteRecord(Command):
    '''
    Delete a record from the AddressBook

    Ex.: delete record 'Jane Doe'
    '''

    def execute(self, bot, parsed_data):
        bot.address_book.delete_record(parsed_data.get('name'))
        print('[+] Record deleted: ', parsed_data.get('name'))


class SearchRecord(Command):
    '''
    Search records case insensitively across all fields.
    '''

    def execute(self, bot, parsed_data):
        query = parsed_data['search_query']
        bot.address_book.search_record(query)


class Note(Command):
    '''
    Enable notetaking mode
    '''

    def execute(self, bot, parsed_data):
        note_book()


if __name__ == "__main__":
    pass
