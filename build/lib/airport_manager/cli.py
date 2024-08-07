import click
from rich.panel import Panel
from rich.console import Console
from animations.welcome_animation import welcome_animation
from animations.banner import display_banner
from airport_manager.config import set_token
from airport_manager.database.routes import check_token_validity
from airport_manager.main_menu import main_menu
from airport_manager.database.main_menu import database_menu
from airport_manager.flight_tracker_v1.main_menu import flight_tracker_v1_menu
from airport_manager.fa24.main_menu import fa24_menu
from airport_manager.utils import clear_console

console = Console()

def validate_token():
    while True:
        token = console.input("[bold yellow]Please enter your API token: [/bold yellow]", password=True)
        response = check_token_validity(token)
        if response and response.get("status") == "success":
            set_token(token)
            console.print(Panel("Token validated successfully!", style="bold green"))
            break
        else:
            console.print(Panel(f"Token validation failed", style="bold red"))

@click.group()
def cli():
    clear_console()
    welcome_animation()
    clear_console()
    display_banner()
    validate_token()

cli.add_command(main_menu)
cli.add_command(database_menu)
cli.add_command(flight_tracker_v1_menu)
cli.add_command(fa24_menu)

if __name__ == "__main__":
    cli()
