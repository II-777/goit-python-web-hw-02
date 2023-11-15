from collections import UserDict
from m1_Record import Record, Birthday
import csv
import os


class AddressBook(UserDict):
    '''Stores records in a dictionary'''

    def add_record(self, record):
        if record.name.value == '' or None:
            print('[-] Name can\'t be None. Try again.')
        else:
            self.data[record.name.value] = record

    def show_record(self, name):
        if name in self.data:
            return repr(self.data[name])
        else:
            return None

    def delete_record(self, name):
        try:
            if name in self.data:
                del self.data[name]
        except Exception as e:
            print(f'[-] Record {name} not found in the AddressBook: {e}.')

    def show_all_records(self):
        if not self.data:
            print("[-] No records found in the address book.")
        else:
            for i, (name, record) in enumerate(self.items(), start=1):
                print(f'{i}. {record.__str__()}')

    def search_record(self, value):
        found = []
        lower_value = value.lower()
        for name, record in self.data.items():
            if lower_value in name.lower():
                found.append((name, record))
            elif record.birthday and record.birthday.value and lower_value in record.birthday.value.lower():
                found.append((name, record))
            else:
                for phone in record.phones:
                    if lower_value in phone.value.lower():
                        found.append((name, record))
                        break
                for email in record.emails:
                    if lower_value in email.value.lower():
                        found.append((name, record))
                        break
                for tag in record.tags:
                    if lower_value in tag.value.lower():
                        found.append((name, record))

        if found:
            for i, (name, record) in enumerate(found, start=1):
                print(f'{i}. {record.__repr__()}')

        return found

    def check_csv_file(self, filename):
        if not os.path.exists(filename):
            print(f"[+] File {filename} not found. Creating an empty file.")
            with open(filename, "w"):
                pass

    def save_to_csv(self, filename):
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['Name', 'Birthday', 'Phones', 'Emails', 'Tags']
                writer = csv.DictWriter(
                    csvfile, fieldnames=fieldnames, delimiter=';')
                writer.writeheader()
                for record in self.data.values():
                    phones_list = [phone.value for phone in record.phones]
                    emails_list = [email.value for email in record.emails]
                    tags_list = [tag.value for tag in record.tags]

                    birthday_value = record.birthday.value if record.birthday else ""
                    writer.writerow(
                        {'Name': record.name.value,
                         'Birthday': birthday_value,
                         'Phones': phones_list,
                         'Emails': emails_list,
                         'Tags': tags_list})

            print(f'[+] Saved addressbook changes to {filename}')
        except Exception as e:
            print(f'[-] Failed to save addressbook changes to {file}: {e}')

    def load_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                name = row['Name']
                birthday = row['Birthday']
                phones_str = row['Phones']
                emails_str = row['Emails']
                tags_str = row['Tags']
                phones_list = eval(phones_str)
                emails_list = eval(emails_str)
                tags_list = eval(tags_str)
                record = Record(name)
                if birthday:
                    record.birthday = Birthday(birthday)
                for phone in phones_list:
                    record.add_phone(phone)
                for emails in emails_list:
                    record.add_email(emails)
                for tags in tags_list:
                    record.add_tag(tags)
                self.add_record(record)


if __name__ == "__main__":
    pass
