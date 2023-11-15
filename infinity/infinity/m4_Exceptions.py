class NameException(Exception):
    pass


class BirthdayException(Exception):
    pass


class PhoneException(Exception):
    pass


class EmailException(Exception):
    pass


class TagException(Exception):
    pass


class SearchQueryException(Exception):
    pass


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NameException:
            return "[-] Invalid name."
        except BirthdayException:
            return "[-] Invalid date."
        except PhoneException:
            return "[-] Invalid phone."
        except EmailException:
            return "[-] Invalid email address."
        except TagException:
            return "[-] Invalid tag."
        except SearchQueryException:
            return "[-] Invalid search query."
        except IndexError:
            return "[-] Not found."
        except KeyError:
            return "[-] Invalid input. Please use 'help' for assistance."
        except TypeError:
            return "[-] Invalid input. Please use 'help' for assistance."
        except ValueError:
            return "[-] Invalid input. Please use 'help' for assistance."
    return wrapper


if __name__ == '__main__':
    pass
