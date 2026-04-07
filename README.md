# The Last Signal

A terminal-based Python learning game. You're a survivor-detective in a collapsed civilization. You've found an old terminal broadcasting encrypted messages. Python is the only tool that can decrypt them.

Every challenge is a survival action — not a lesson.

---

## Status

> 🚧 In development — V1 (terminal version) in progress

---

## What It Is

A story-driven mystery game that teaches Python from scratch. No math puzzles. Challenges use real logic: names, messages, lists of survivors, radio signals.

You learn by doing. The story only moves forward when your code works.

---

## Curriculum

| Chapter | Story Beat | Python Concept |
|---------|-----------|----------------|
| 1 | You power on the terminal. A fragmented message appears. | Variables, `print()`, storing text |
| 2 | You find a survivor log with missing entries. | Strings, string methods, `input()` |
| 3 | A supply cache is locked — you need to check who's authorized. | Lists, indexing, membership |
| 4 | You intercept a repeating signal meant for multiple survivors. | Loops, iterating over lists |
| 5 | The terminal asks you to build a decoder from scratch. | Functions, parameters, return values |

---

## How It Works

- **Chapters 1–2:** Multiple choice only — no typing required
- **Chapter 3:** Hybrid — multiple choice + simple typed Python
- **Chapters 4–5:** You write real Python that gets executed and validated
- **Wrong answers** give a story-flavored hint, not the solution
- **Type `hint`** anytime for a progressive hint (up to 3 per challenge)
- **Progress is saved** between sessions — pick up where you left off

---

## Tech Stack

| Layer | Tool |
|-------|------|
| Language | Python |
| Terminal colors | `rich` |
| Save system | JSON (local) |
| Code execution | `exec()` with stdout capture + validation |

---

## Project Structure

```
/
├── main.py               # Entry point
├── requirements.txt      # Dependencies (rich)
├── game/
│   ├── __init__.py
│   ├── display.py        # Color output via rich
│   ├── save.py           # Save/load progress
│   ├── engine.py         # Game loop, input handling, answer validation
│   └── chapters.py       # All story content and challenges
└── saves/                # Local save files (gitignored)
```

---

## Running the Game

```bash
pip install -r requirements.txt
python main.py
```

Requires Python 3.8+

---

## Roadmap

### V1 — Terminal (current)
- [x] Project design and curriculum
- [ ] Core engine and save system
- [ ] Chapter 1–5 content
- [ ] Answer validation and hint system
- [ ] Playtesting and polish

### V2 — Browser
- [ ] Backend for safe Python execution (Railway or Cloudflare Workers)
- [ ] Web frontend with story panels and progress UI
- [ ] Chapter select and color themes
- [ ] Port after V1 is stable and fun

---

## About

Built as a personal Python learning tool. Designed for someone starting from zero — the game teaches the language through the story, not the other way around.
