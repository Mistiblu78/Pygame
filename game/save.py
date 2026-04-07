import json
import os

SAVE_DIR = "saves"
SAVE_FILE = os.path.join(SAVE_DIR, "progress.json")

DEFAULT_SAVE = {
    "chapter": 1,
    "challenge_index": 0,
    "completed_chapters": [],
    "story_flags": {}
}


def ensure_save_dir():
    """Make sure the saves directory exists."""
    os.makedirs(SAVE_DIR, exist_ok=True)


def load_save():
    """Load saved progress. Returns default if no save exists."""
    ensure_save_dir()
    if not os.path.exists(SAVE_FILE):
        return DEFAULT_SAVE.copy()
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            # Fill in any missing keys from defaults
            for key, value in DEFAULT_SAVE.items():
                if key not in data:
                    data[key] = value
            return data
    except (json.JSONDecodeError, IOError):
        return DEFAULT_SAVE.copy()


def save_progress(chapter, challenge_index, completed_chapters=None, story_flags=None):
    """Save current progress to disk."""
    ensure_save_dir()
    data = {
        "chapter": chapter,
        "challenge_index": challenge_index,
        "completed_chapters": completed_chapters or [],
        "story_flags": story_flags or {}
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=2)


def has_save():
    """Check if a save file exists."""
    return os.path.exists(SAVE_FILE)


def delete_save():
    """Delete saved progress (new game)."""
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
