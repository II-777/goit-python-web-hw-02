import re


class SanitizeInput:
    '''Ensures same phone number and date formats across all records'''
    @staticmethod
    def sanitize_phone(phone):
        sanitized_phone = ''.join(filter(str.isdigit, phone))

        if len(sanitized_phone) != 11:
            raise ValueError("[-] Phone must be 11-digit long.")
        return sanitized_phone

    @staticmethod
    def sanitize_date(date):
        match = re.search(
            r'^(\d{4})\D*(0[1-9]|1[0-2])\D*(0[1-9]|[12]\d|3[01])', date)
        # extra check for the year format (to begin from either 19 or 20)
        # r'^(19\d{2}|20\d{2})\D*(0[1-9]|1[0-2])\D*(0[1-9]|[12]\d|3[01])', date)

        if match:
            year, month, day = match.groups()
            sanitized_date = f"{year}-{month}-{day}"
            return sanitized_date
        else:
            raise ValueError("[-] Date must be in YYYY-MM-DD format.")


if __name__ == '__main__':
    # DEMO:
    try:
        phone_number = input('Enter a phone number: ')
        sanitized_phone = SanitizeInput.sanitize_phone(phone_number)
        print(f"[+] Sanitized phone number: {sanitized_phone}")
    except ValueError as e:
        print(e)

    try:
        date = input('Enter a date: ')
        sanitized_date = SanitizeInput.sanitize_date(date)
        print(f"[+] Sanitized date: {sanitized_date}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    pass
