import io
import sys
from game.display import (
    print_story, print_task, print_options, print_success,
    print_error, print_hint, print_chapter_header, press_enter,
    print_code_prompt, print_system, get_input, print_save_notice,
    print_divider, console
)
from game.save import load_save, save_progress
from game.chapters import CHAPTERS


def run_player_code(code, setup_code=""):
    """
    Safely execute player's Python code.
    Returns (success, output, error_message)
    """
    full_code = setup_code + "\n" + code if setup_code else code

    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    try:
        exec(full_code, {})
        output = buffer.getvalue().strip()
        return True, output, None
    except SyntaxError as e:
        return False, "", f"Syntax error: {e.msg} (line {e.lineno})"
    except Exception as e:
        return False, "", f"{type(e).__name__}: {e}"
    finally:
        sys.stdout = old_stdout


def collect_multiline_code():
    """Collect multi-line code input from the player."""
    lines = []
    print_code_prompt()
    while True:
        line = console.input("  [dim white]... [/dim white]")
        if line.strip().lower() == "done":
            break
        if line.strip().lower() == "hint":
            return None  # Signal that hint was requested
        lines.append(line)
    return "\n".join(lines)


def run_multiple_choice(challenge, hint_count, save_state):
    """Handle a multiple choice challenge. Returns True when solved."""
    print_story(challenge["story"])
    print_task(challenge["task"])
    print_options(challenge["options"])

    attempts = 0
    while True:
        answer = get_input("  Your answer: ").strip().upper()

        if answer == "HINT":
            if hint_count[0] < len(challenge["hints"]):
                print_hint(challenge["hints"][hint_count[0]], hint_count[0] + 1)
                hint_count[0] += 1
            else:
                print_system("No more hints available.")
            print_options(challenge["options"])
            continue

        # Accept single letter or full answer text
        correct = challenge["answer"].upper()
        correct_text = challenge["options"][correct].upper()

        if answer == correct or answer == correct_text:
            print_success(challenge["success"])
            press_enter()
            return True
        else:
            attempts += 1
            print_error("That's not right. The signal flickers. Try again.")
            if attempts == 1 and hint_count[0] == 0:
                print_system('Type "hint" if you need a clue.')
            print_options(challenge["options"])


def run_code_challenge(challenge, hint_count, save_state):
    """Handle a code input challenge. Returns True when solved."""
    print_story(challenge["story"])
    print_task(challenge["task"])

    attempts = 0
    while True:
        code = collect_multiline_code()

        if code is None:
            # Player typed "hint" during code entry
            if hint_count[0] < len(challenge["hints"]):
                print_hint(challenge["hints"][hint_count[0]], hint_count[0] + 1)
                hint_count[0] += 1
            else:
                print_system("No more hints available.")
            continue

        if not code.strip():
            print_error("No code entered. Try again.")
            continue

        success, output, error = run_player_code(
            code,
            challenge.get("setup_code", "")
        )

        if not success:
            attempts += 1
            print_error(f"Your code hit an error: {error}")
            print_system("Check your syntax and try again.")
            if attempts == 1:
                print_system('Type "hint" on the first line for a clue.')
            continue

        expected = challenge["expected_output"].strip()
        if output == expected:
            print_success(challenge["success"])
            press_enter()
            return True
        else:
            attempts += 1
            print_error("The output doesn't match what the terminal expects.")
            console.print(f"  Expected: [dim]{expected}[/dim]")
            console.print(f"  Got:      [dim]{output if output else '(nothing)'}[/dim]")
            console.print()
            print_system('Type "hint" on the first line for a clue.')


def run_hybrid_challenge(challenge, hint_count, save_state):
    """Handle a hybrid challenge (code input only, like code challenges)."""
    return run_code_challenge(challenge, hint_count, save_state)


def run_chapter(chapter_data, start_challenge=0, save_state=None):
    """Run a full chapter. Returns updated save state."""
    if save_state is None:
        save_state = {}

    print_chapter_header(chapter_data["id"], chapter_data["title"])
    print_story(chapter_data["intro"])
    press_enter()

    challenges = chapter_data["challenges"]

    for i, challenge in enumerate(challenges):
        if i < start_challenge:
            continue

        hint_count = [0]
        challenge_type = challenge.get("type", "multiple_choice")

        # Save before each challenge
        save_progress(
            chapter=chapter_data["id"],
            challenge_index=i,
            completed_chapters=save_state.get("completed_chapters", []),
            story_flags=save_state.get("story_flags", {})
        )
        print_save_notice(chapter_data["id"], i + 1)

        print_divider()
        console.print(
            f"  [dim]Challenge {i + 1} of {len(challenges)}[/dim]"
        )
        console.print()

        if challenge_type == "multiple_choice":
            run_multiple_choice(challenge, hint_count, save_state)
        elif challenge_type == "code":
            run_code_challenge(challenge, hint_count, save_state)
        elif challenge_type == "hybrid":
            run_hybrid_challenge(challenge, hint_count, save_state)

    # Chapter complete
    completed = save_state.get("completed_chapters", [])
    if chapter_data["id"] not in completed:
        completed.append(chapter_data["id"])
    save_state["completed_chapters"] = completed

    save_progress(
        chapter=chapter_data["id"] + 1,
        challenge_index=0,
        completed_chapters=completed,
        story_flags=save_state.get("story_flags", {})
    )

    return save_state


def run_game():
    """Main game loop."""
    save_state = load_save()
    current_chapter = save_state.get("chapter", 1)
    current_challenge = save_state.get("challenge_index", 0)

    # Find where to start
    chapter_index = current_chapter - 1

    if chapter_index >= len(CHAPTERS):
        console.print(
            "\n  [cyan]You've completed all available chapters.[/cyan]"
        )
        console.print(
            "  [dim]More chapters coming soon...[/dim]\n"
        )
        return

    # Run chapters from where we left off
    for i in range(chapter_index, len(CHAPTERS)):
        chapter = CHAPTERS[i]
        start = current_challenge if i == chapter_index else 0
        save_state = run_chapter(chapter, start_challenge=start, save_state=save_state)
        current_challenge = 0  # Reset for subsequent chapters

    console.print("\n  [bold cyan]You've reached the end of the current signal.[/bold cyan]")
    console.print("  [dim]Stay alive out there.[/dim]\n")
