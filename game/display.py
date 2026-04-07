from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.rule import Rule
import time

console = Console()

# Color scheme
STORY_COLOR = "cyan"
TASK_COLOR = "yellow"
SUCCESS_COLOR = "green"
ERROR_COLOR = "red"
HINT_COLOR = "magenta"
PROMPT_COLOR = "white"
DIM_COLOR = "dim white"
TITLE_COLOR = "bold cyan"


def slow_print(text, color=STORY_COLOR, delay=0.018):
    """Print text character by character for dramatic effect."""
    styled = Text()
    for char in text:
        styled.append(char, style=color)
        console.print(styled, end="\r", highlight=False)
        time.sleep(delay)
    console.print()


def print_story(text):
    """Print narrative story text."""
    console.print()
    for line in text.strip().split("\n"):
        if line.strip():
            console.print(f"  {line}", style=STORY_COLOR)
        else:
            console.print()
    console.print()


def print_task(text):
    """Print a challenge task description."""
    console.print(Panel(
        text.strip(),
        title="[bold yellow]TASK[/bold yellow]",
        border_style="yellow",
        padding=(1, 2)
    ))


def print_options(options):
    """Print multiple choice options."""
    console.print()
    for key, value in options.items():
        console.print(f"  [{key}]  {value}", style=PROMPT_COLOR)
    console.print()


def print_success(text):
    """Print a success message."""
    console.print()
    console.print(Rule(style="green"))
    for line in text.strip().split("\n"):
        if line.strip():
            console.print(f"  {line}", style=SUCCESS_COLOR)
        else:
            console.print()
    console.print(Rule(style="green"))
    console.print()


def print_error(text):
    """Print an error or wrong answer message."""
    console.print(f"\n  ✗ {text}", style=ERROR_COLOR)
    console.print()


def print_hint(text, number):
    """Print a hint."""
    console.print(
        Panel(
            text.strip(),
            title=f"[magenta]HINT {number}[/magenta]",
            border_style="magenta",
            padding=(0, 2)
        )
    )


def print_title():
    """Print the game title screen."""
    console.clear()
    console.print()
    console.print(Rule(style="cyan"))
    console.print()
    console.print("  THE LAST SIGNAL", style="bold cyan", justify="center")
    console.print()
    console.print("  a Python learning game", style="dim cyan", justify="center")
    console.print()
    console.print(Rule(style="cyan"))
    console.print()


def print_chapter_header(number, title):
    """Print a chapter header."""
    console.print()
    console.print(Rule(style="dim cyan"))
    console.print(
        f"  CHAPTER {number}: {title.upper()}",
        style="bold cyan"
    )
    console.print(Rule(style="dim cyan"))
    console.print()


def print_divider():
    """Print a simple divider."""
    console.print(Rule(style="dim"))


def print_code_prompt():
    """Print the code input prompt."""
    console.print(
        "\n  Enter your Python code below.",
        style=DIM_COLOR
    )
    console.print(
        '  Type "hint" for a hint. Type "done" on a new line when finished.\n',
        style=DIM_COLOR
    )


def print_system(text):
    """Print a system message."""
    console.print(f"  > {text}", style=DIM_COLOR)


def get_input(prompt="  > "):
    """Get input from the player."""
    return console.input(f"[white]{prompt}[/white]").strip()


def press_enter():
    """Wait for the player to press enter."""
    console.input("\n  [dim][ press enter to continue ][/dim]")
    console.print()


def print_save_notice(chapter, challenge):
    """Print a small save notification."""
    console.print(
        f"  [dim]progress saved — chapter {chapter}[/dim]"
    )
    console.print()
