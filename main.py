from game.display import print_title, print_story, get_input, console, press_enter
from game.save import has_save, load_save, delete_save
from game.engine import run_game


def main():
    print_title()

    if has_save():
        save = load_save()
        chapter = save.get("chapter", 1)
        console.print(
            f"  [dim]Save found — Chapter {chapter}[/dim]\n"
        )
        console.print("  [A]  Continue")
        console.print("  [B]  New Game\n")
        choice = get_input("  > ").strip().upper()
        if choice == "B":
            confirm = get_input(
                "  This will erase your progress. Are you sure? (yes/no): "
            ).strip().lower()
            if confirm == "yes":
                delete_save()
                console.print("\n  [dim]Progress cleared.[/dim]")
                press_enter()
    else:
        print_story("""
Welcome, operator.

This terminal has been waiting a long time.

You are about to use Python — a real programming language —
to survive, investigate, and piece together what happened
to the world.

Every challenge you solve is real code. Everything you learn here
works outside this terminal too.

No math. No memorizing. Just logic, story, and survival.

Let's begin.
""")
        press_enter()

    run_game()


if __name__ == "__main__":
    main()
