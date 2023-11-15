from abc import ABC, abstractmethod
from rich import box
from rich.console import Console
from rich.table import Table


class UserInterface(ABC):
    @abstractmethod
    def show_contacts(self, contacts):
        pass

    @abstractmethod
    def show_notes(self, notes):
        pass

    @abstractmethod
    def show_commands(self, commands):
        pass


class ConsoleUserInterface(UserInterface):
    def show_contacts(self, bot):
        table = Table(box=box.SIMPLE_HEAD)

        # Define table columns with styles and justify settings
        table.add_column("Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("Birthday", justify="left", style="magenta")
        table.add_column("Phones", justify="left", style="cyan")
        table.add_column("Emails", justify="left", style="magenta")
        table.add_column("Tags", justify="left", style="cyan")

        # Define alternating row styles
        table.row_styles = ["", "dim"]

        # Populate the table with the user data
        for name, record in bot.address_book.data.items():  # Change here
            table.add_row(
                record.name.value if record.name.value else "",
                record.birthday.value if record.birthday else "",
                ", ".join(phone.value for phone in record.phones),
                ", ".join(email.value for email in record.emails),
                ", ".join(tag.value for tag in record.tags)
            )

        console = Console()
        console.print(table)

    def show_notes(self, notes):
        pass

    def show_commands(self, commands):
        pass


if __name__ == "__main__":
    pass
