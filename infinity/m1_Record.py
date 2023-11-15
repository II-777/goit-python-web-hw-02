class Field:
    '''Field baseclass.'''

    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    def value(self):
        self._value = None


class Name(Field):
    '''Represent Name field.'''

    def __init__(self, name):
        super().__init__(name)


class Birthday(Field):
    '''Represent Birthday field.'''

    def __init__(self, birthday):
        super().__init__(birthday)


class Phone(Field):
    '''Represent Phone field.'''

    def __init__(self, phone):
        super().__init__(phone)

    def __str__(self):
        return f"{self.phone}"


class Email(Field):
    '''Represent Email field.'''

    def __init__(self, email):
        super().__init__(email)

    def __str__(self):
        return f"{self.email}"


class Tag(Field):
    '''Represent Tag field.'''

    def __init__(self, tag):
        super().__init__(tag)

    def __str__(self):
        return f"{self.tag}"


class Record:
    '''Represent Record in the AddressBook.'''

    def __init__(self, name,
                 birthday=None,
                 phones=None,
                 emails=None,
                 tags=None):

        self.name = Name(name)
        self.birthday = Birthday(birthday) if birthday is not None else None
        self.phones = [Phone(phone) for phone in (phones or [])]
        self.emails = [Email(email) for email in (emails or [])]
        self.tags = [Tag(tag) for tag in (tags or [])]

        if name is None:
            print('[-] Name cannot be \'None\'')

    def __repr__(self):
        return ({f"{self.name.value}; {self.birthday.value if self.birthday else None}; "
                f"{', '.join([phone.value for phone in self.phones]) if self.phones else None}; "
                 f"{', '.join([email.value for email in self.emails]) if self.emails else None}; "
                 f"{', '.join([tag.value for tag in self.tags]) if self.tags else None};"})

    def __str__(self):
        return (f"n: {self.name.value}; b: {self.birthday.value if self.birthday else None}; "
                f"p: {', '.join([phone.value for phone in self.phones]) if self.phones else None}; "
                f"e: {', '.join([email.value for email in self.emails]) if self.emails else None}; "
                f"t: {', '.join([tag.value for tag in self.tags]) if self.tags else None}; ")

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_email(self, email):
        self.emails.append(Email(email))

    def add_tag(self, tag):
        self.tags.append(Tag(tag))

    @property
    def show_name(self):
        return self.name.value

    @property
    def show_birthday(self):
        if self.birthday:
            return self.birthday.value
        else:
            return None

    @property
    def show_phones(self):
        if self.phones:
            return [f"{phone.value}" for phone in self.phones]
        else:
            return None

    @property
    def show_emails(self):
        if self.emails:
            return [f"{email.value}" for email in self.emails]
        else:
            return None

    @property
    def show_tags(self):
        if self.tags:
            return [f"{tag.value}" for tag in self.tags]
        else:
            return None

    @show_name.setter
    def update_name(self, new_name):
        if new_name == '' or new_name is None:
            print('[-] Name can\'t be None. Try again.')
        else:
            self.name = Name(new_name)

    @show_birthday.setter
    def update_birthday(self, new_birthday):
        self.birthday = Birthday(new_birthday)

    @show_phones.setter
    def update_phones(self, new_phones):
        self.phones = [Phone(phone) for phone in (new_phones or [])]

    @show_emails.setter
    def update_emails(self, new_emails):
        self.emails = [Email(email) for email in (new_emails or [])]

    @show_tags.setter
    def update_tags(self, new_tags):
        self.tags = [Tag(tag) for tag in (new_tags or [])]

    @show_birthday.deleter
    def del_birthday(self):
        self.birthday = None

    @show_phones.deleter
    def del_phones(self):
        self.phones = None

    @show_emails.deleter
    def del_emails(self):
        self.emails = None

    @show_tags.deleter
    def del_tags(self):
        self.tags = None


if __name__ == "__main__":
    pass
