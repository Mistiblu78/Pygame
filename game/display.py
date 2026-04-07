from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.rule import Rule
import time
import random

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

# ASCII art for chapter headers
CHAPTER_ART = {
    1: [
        "  +--------------------------+",
        "  |  TERMINAL ONLINE        |",
        "  |  SIGNAL DETECTED...     |",
        "  |  DECRYPTION REQUIRED    |",
        "  +--------------------------+",
    ],
    2: [
        "  +--------------------------+",
        "  |  SURVIVOR_LOG.txt       |",
        "  |  LAST MODIFIED: 47 DAYS |",
        "  |  CORRUPTION DETECTED    |",
        "  +--------------------------+",
    ],
    3: [
        "  +---------------------------+",
        "  |  SUPPLY CACHE - TUNNEL B |",
        "  |  ACCESS: RESTRICTED      |",
        "  |  AUTHORIZATION REQUIRED  |",
        "  +---------------------------+",
    ],
    4: [
        "  +--------------------------+",
        "  |  RELAY STATION OMEGA    |",
        "  |  BROADCAST RANGE: 200KM |",
        "  |  SIGNAL: ACTIVE         |",
        "  +--------------------------+",
    ],
    5: [
        "  +--------------------------+",
        "  |  INCOMING TRANSMISSION  |",
        "  |  ORIGIN: STATION ELEVEN |",
        "  |  DECODING IN PROGRESS.. |",
        "  +--------------------------+",
    ],
}

TITLE_ART = [
    "  _____ _   _ _____   _      _    ____ _____   ____ ___ ____ _   _    _    _     ",
    " |_   _| | | | ____| | |    / \\  / ___|_   _| / ___|_ _/ ___| \\ | |  / \\  | |   ",
    "   | | | |_| |  _|   | |   / _ \\ \\___ \\ | |   \\___ \\| | |  _|  \\| | / _ \\ | |   ",
    "   | | |  _  | |___  | |__/ ___ \\ ___) || |    ___) | | |_| | |\\  |/ ___ \\| |___",
    "   |_| |_| |_|_____| |____/_/   \\_\\____/ |_|   |____/___\\____|_| \\_/_/   \\_\\_____|",
]


def glitch_line(text, color="cyan"):
    """Print a single line with a glitch effect then resolve cleanly."""
    glitch_chars = ["#", "%", "@", "!", "?", "*", "/", "\\"]
    random.seed(99)

    garbled = ""
    for char in text:
        if char not in (" ", "|", "+", "-") and random.random() < 0.45:
            garbled += random.choice(glitch_chars)
        else:
            garbled += char

    console.print(garbled, style=f"dim {color}")
    time.sleep(0.07)
    console.print(text, style=f"bold {color}", end="\r")
    time.sleep(0.05)
    console.print(text, style=f"bold {color}")


def slow_print(text, color=STORY_COLOR, delay=0.018):
    """Print text character by character."""
    for line in text.strip().split("\n"):
        rendered = "  "
        for char in line:
            rendered += char
            console.print(rendered, end="\r", style=color, highlight=False)
            time.sleep(delay)
        console.print(f"  {line}", style=color)
    console.print()


def print_story(text, slow=False):
    """Print narrative story text."""
    console.print()
    lines = text.strip().split("\n")
    for line in lines:
        if line.strip():
            if slow:
                slow_print(line, delay=0.014)
            else:
                console.print(f"  {line}", style=STORY_COLOR)
        else:
            console.print()
    console.print()


def print_task(text):
    """Print a challenge task description."""
    console.print(Panel(
        text.strip(),
        title="[bold yellow]> TASK[/bold yellow]",
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
    """Print a success message with a flash effect."""
    console.print()
    time.sleep(0.3)

    # Flash the confirmation line
    for style in ["bold green", "dim green", "bold green"]:
        console.print("  >>> SIGNAL CONFIRMED <<<", style=style, end="\r")
        time.sleep(0.12)
    console.print("  >>> SIGNAL CONFIRMED <<<", style="bold green")
    console.print()
    console.print(Rule(style="green"))
    console.print()

    for line in text.strip().split("\n"):
        if line.strip():
            console.print(f"  {line}", style=SUCCESS_COLOR)
            time.sleep(0.03)
        else:
            console.print()

    console.print()
    console.print(Rule(style="green"))
    console.print()


def print_error(text):
    """Print an error with a red flash."""
    console.print()
    time.sleep(0.2)
    console.print("  !!! SIGNAL REJECTED !!!", style="bold red", end="\r")
    time.sleep(0.15)
    console.print("  !!! SIGNAL REJECTED !!!", style="bold red")
    console.print(f"  {text}", style=ERROR_COLOR)
    console.print()


def print_hint(text, number):
    """Print a hint."""
    console.print()
    console.print(Panel(
        text.strip(),
        title=f"[magenta]> HINT {number}/3[/magenta]",
        border_style="magenta",
        padding=(0, 2)
    ))
    console.print()


def print_title():
    """Print the game title with a boot sequence."""
    console.clear()
    console.print()

    boot_lines = [
        ("POWER ON...", 0.35),
        ("SOLAR ARRAY: CONNECTED", 0.2),
        ("BATTERY RESERVE: 43%", 0.15),
        ("NETWORK STATUS: OFFLINE", 0.15),
        ("LOCAL STORAGE: INTACT", 0.15),
        ("SIGNAL SCANNER: ACTIVE", 0.2),
        ("ANOMALY DETECTED ON FREQUENCY 88.1...", 0.4),
        ("LOADING DECRYPTION MODULES...", 0.5),
    ]

    for line, delay in boot_lines:
        console.print(f"  > {line}", style="dim cyan")
        time.sleep(delay)

    time.sleep(0.5)
    console.clear()
    console.print()

    for line in TITLE_ART:
        console.print(line, style="bold cyan")
        time.sleep(0.06)

    console.print()
    console.print(Rule(style="dim cyan"))
    console.print("  a Python learning game", style="dim cyan", justify="center")
    console.print(Rule(style="dim cyan"))
    console.print()


def print_chapter_header(number, title):
    """Print a chapter header with ASCII box and glitch effect."""
    console.print()
    time.sleep(0.3)
    console.clear()
    console.print()

    console.print(f"  > LOADING CHAPTER {number}...", style="dim cyan")
    time.sleep(0.4)
    console.print(f"  > DECRYPTING...", style="dim cyan")
    time.sleep(0.35)
    console.print()

    if number in CHAPTER_ART:
        for line in CHAPTER_ART[number]:
            console.print(line, style="cyan")
            time.sleep(0.05)

    console.print()
    glitch_line(f"  CHAPTER {number}: {title.upper()}")
    console.print()
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
    console.print()
    console.input("  [dim][ press enter to continue ][/dim]")
    console.print()


def print_save_notice(chapter, challenge):
    """Print a small save notification."""
    console.print(
        f"  [dim]> progress saved -- chapter {chapter}[/dim]"
    )
    console.print()


def print_transmission(text):
    """Print incoming radio transmission character by character."""
    console.print()
    console.print("  [dim cyan]> INCOMING TRANSMISSION...[/dim cyan]")
    time.sleep(0.6)

    for line in text.strip().split("\n"):
        if line.strip():
            rendered = "  "
            for char in line:
                rendered += char
                console.print(rendered, style="cyan", end="\r", highlight=False)
                time.sleep(0.03)
            console.print(f"  {line}", style="cyan")
        else:
            console.print()
    console.print()
