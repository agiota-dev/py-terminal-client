from rich.console import Console
from rich.panel import Panel

console = Console()

def print_note(index: int, content: str):
    panel = Panel(content, title=f"Note #{index}", expand=True, border_style="green")
    console.print(panel)
