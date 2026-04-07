CHAPTERS = [
    {
        "id": 1,
        "title": "Power On",
        "intro": """
The world ended eighteen months ago. Not with bombs — with silence.
Every network, every server, every connected device just... stopped.

You've been surviving in the ruins of what used to be a city.
Today you found something in the basement of an old university building:
a terminal. Still powered by a solar array on the roof.

You brush the dust off the keyboard. A cursor blinks.

The screen reads:

    SIGNAL DETECTED — ORIGIN UNKNOWN
    DECRYPTION REQUIRED
    AWAITING OPERATOR...

Your hands are shaking. You haven't seen a working screen in months.
You sit down. You type.
""",
        "challenges": [
            {
                "id": "1-1",
                "type": "multiple_choice",
                "story": """
The terminal prompts you for an operator name.
You need to store your name so the system can identify you.

In Python, storing information looks like this:

    name = "your name here"

That's called a VARIABLE. You're giving a piece of information a label
so you can use it later.
""",
                "task": "What is a variable in Python?",
                "options": {
                    "A": "A number that changes on its own",
                    "B": "A label that stores a piece of information",
                    "C": "A type of error message",
                    "D": "A command that prints text"
                },
                "answer": "B",
                "hints": [
                    "Think about what the word 'variable' means — something that holds a value.",
                    "When you write name = 'Alex', you're giving the value 'Alex' the label 'name'.",
                    "It's B — a label that stores information."
                ],
                "success": """
Correct. The terminal accepts your logic.

You type your name. The cursor blinks three times.
Then: OPERATOR RECOGNIZED. ACCESS LEVEL: BASIC.

You're in. But the signal is still encrypted.
You'll need to go deeper.
"""
            },
            {
                "id": "1-2",
                "type": "multiple_choice",
                "story": """
The terminal asks you to confirm your callsign out loud —
to broadcast it so any other survivors listening can hear you.

In Python, you display information to the screen using print():

    name = "Phoenix"
    print(name)

This would show:  Phoenix
""",
                "task": "What does print() do?",
                "options": {
                    "A": "Saves your name to a file",
                    "B": "Deletes a variable",
                    "C": "Displays information on the screen",
                    "D": "Creates a new variable"
                },
                "answer": "C",
                "hints": [
                    "What happens when you call print() in a Python program?",
                    "The word 'print' is a clue — it outputs something visibly.",
                    "It's C — print() displays information on the screen."
                ],
                "success": """
Your callsign crackles through the terminal speaker.

Somewhere out there, someone might be listening.

The signal strength meter ticks upward. The encrypted message
is starting to resolve. One more step.
"""
            },
            {
                "id": "1-3",
                "type": "multiple_choice",
                "story": """
The terminal shows you a fragment of the encrypted signal:

    msg = "HELP - SECTOR 7 - SURVIVORS"
    print(msg)

You recognize the pattern. A variable storing a message,
then print() to display it.
""",
                "task": "What would the above code display on screen?",
                "options": {
                    "A": "msg",
                    "B": 'HELP - SECTOR 7 - SURVIVORS',
                    "C": '"msg"',
                    "D": "Nothing — it would cause an error"
                },
                "answer": "B",
                "hints": [
                    "print() displays the VALUE stored in the variable, not the variable name itself.",
                    "msg stores the text HELP - SECTOR 7 - SURVIVORS.",
                    "It's B — print(msg) shows whatever is stored inside msg."
                ],
                "success": """
SIGNAL FRAGMENT DECODED.

The message is real. There are survivors in Sector 7.
That's three kilometers east of your position.

The terminal hums. A new file appears on screen:
SURVIVOR_LOG.txt — last modified 47 days ago.

You open it. Half the entries are corrupted.
You'll need to know how to work with text to fix them.

> END OF CHAPTER 1
> CHAPTER 2 UNLOCKED: The Survivor Log
"""
            }
        ]
    },
    {
        "id": 2,
        "title": "The Survivor Log",
        "intro": """
SURVIVOR_LOG.txt

The file opens slowly. There are dozens of entries — names, locations,
supply counts. But the corruption is bad. Words are split. Names are
in the wrong case. Some entries are all uppercase, some are garbled.

You need to clean this data if you're going to find the Sector 7 survivors.

Fortunately, Python can manipulate text. Strings — that's what Python
calls pieces of text — have built-in tools for exactly this.
""",
        "challenges": [
            {
                "id": "2-1",
                "type": "multiple_choice",
                "story": """
The first entry reads:

    "mARCUS - sECTOR 7 - aLIVE"

The case is scrambled. You need to normalize it.
Python strings have a method called .lower() that converts
everything to lowercase:

    entry = "mARCUS - sECTOR 7 - aLIVE"
    print(entry.lower())

Would output:  marcus - sector 7 - alive
""",
                "task": "What does the .lower() method do to a string?",
                "options": {
                    "A": "Deletes the string",
                    "B": "Converts all characters to lowercase",
                    "C": "Converts all characters to uppercase",
                    "D": "Removes spaces from the string"
                },
                "answer": "B",
                "hints": [
                    "The method name is a clue — 'lower' means lowercase.",
                    "It affects every letter in the string.",
                    "It's B — .lower() converts all characters to lowercase."
                ],
                "success": """
The entry normalizes. You can read it now:

    marcus - sector 7 - alive

Marcus. He was alive 47 days ago.
You keep reading.
"""
            },
            {
                "id": "2-2",
                "type": "multiple_choice",
                "story": """
The next entry has a different problem:

    "   RELAY STATION OMEGA   "

There are spaces at the start and end — corrupted padding from
the original transmission. Python's .strip() method removes them:

    location = "   RELAY STATION OMEGA   "
    print(location.strip())

Would output:  RELAY STATION OMEGA
""",
                "task": "What does .strip() do?",
                "options": {
                    "A": "Removes all spaces inside the string",
                    "B": "Converts the string to a list",
                    "C": "Removes spaces from the beginning and end of a string",
                    "D": "Splits the string into two parts"
                },
                "answer": "C",
                "hints": [
                    "It doesn't touch spaces inside the text — only the edges.",
                    "Think of 'stripping' the outer layer off something.",
                    "It's C — .strip() removes leading and trailing spaces."
                ],
                "success": """
    RELAY STATION OMEGA

That's a location you recognize. An old emergency broadcast relay
about two kilometers north of Sector 7.

If survivors are there, that relay could reach other terminals.
You make a note.
"""
            },
            {
                "id": "2-3",
                "type": "multiple_choice",
                "story": """
One entry is partially readable:

    "STATUS: UNKNOWN. LAST SEEN: TUNNEL B."

You want to check if the word "TUNNEL" appears in that entry.
Python lets you search inside strings using the 'in' keyword:

    entry = "STATUS: UNKNOWN. LAST SEEN: TUNNEL B."
    print("TUNNEL" in entry)

This would output: True
""",
                "task": "What does 'in' do when used with a string?",
                "options": {
                    "A": "It adds text to the string",
                    "B": "It checks whether one string exists inside another",
                    "C": "It counts how many times a word appears",
                    "D": "It replaces a word in the string"
                },
                "answer": "B",
                "hints": [
                    "The result is True or False — it's checking something.",
                    "'TUNNEL' in entry — is TUNNEL found inside entry?",
                    "It's B — 'in' checks whether one string exists inside another."
                ],
                "success": """
True.

Tunnel B. You pull up the old city map on the terminal.
Tunnel B runs directly under Sector 7 — it was used as
an emergency shelter during the collapse.

They might still be there.

The terminal beeps. A new signal is coming in —
coordinates locked behind a supply cache access code.
The cache is in Tunnel B.

> END OF CHAPTER 2
> CHAPTER 3 UNLOCKED: The Supply Cache
"""
            }
        ]
    },
    {
        "id": 3,
        "title": "The Supply Cache",
        "intro": """
You make it to Tunnel B.

At the entrance: a keypad. Next to it, a weathered placard reads:

    AUTHORIZED PERSONNEL ONLY
    ACCESS GRANTED TO REGISTERED OPERATORS

Someone left a terminal nearby — still running, somehow.
On the screen: a Python script, half-written, meant to check
whether an operator is on the authorized list.

You're going to have to finish it.
""",
        "challenges": [
            {
                "id": "3-1",
                "type": "multiple_choice",
                "story": """
The authorized list is stored like this:

    authorized = ["Marcus", "Reyes", "Dr. Okafor", "Phoenix"]

That's called a LIST — a collection of items stored in order,
wrapped in square brackets, separated by commas.
""",
                "task": "Which of these correctly creates a list of survivor names?",
                "options": {
                    "A": 'survivors = ("Ana", "Cole", "Mira")',
                    "B": 'survivors = ["Ana", "Cole", "Mira"]',
                    "C": 'survivors = {"Ana", "Cole", "Mira"}',
                    "D": 'survivors = "Ana", "Cole", "Mira"'
                },
                "answer": "B",
                "hints": [
                    "Lists use a specific type of bracket.",
                    "Square brackets [ ] are what define a list in Python.",
                    "It's B — lists use square brackets [ ]."
                ],
                "success": """
You recognize the syntax. Square brackets. Comma-separated names.

You check the authorized list:
    ["Marcus", "Reyes", "Dr. Okafor", "Phoenix"]

Your callsign is in there. Phoenix. You keep going.
"""
            },
            {
                "id": "3-2",
                "type": "multiple_choice",
                "story": """
The script needs to pull the FIRST name from the list to
display it as a confirmation:

    authorized = ["Marcus", "Reyes", "Dr. Okafor", "Phoenix"]

In Python, you access items in a list by their position — called an INDEX.
Counting starts at ZERO:

    authorized[0]  → "Marcus"
    authorized[1]  → "Reyes"
    authorized[2]  → "Dr. Okafor"
""",
                "task": "What would authorized[2] return?",
                "options": {
                    "A": '"Reyes"',
                    "B": '"Marcus"',
                    "C": '"Dr. Okafor"',
                    "D": '"Phoenix"'
                },
                "answer": "C",
                "hints": [
                    "Remember: Python starts counting at 0, not 1.",
                    "Index 0 = Marcus, Index 1 = Reyes, Index 2 = ?",
                    "It's C — authorized[2] returns 'Dr. Okafor'."
                ],
                "success": """
Dr. Okafor. You remember that name from the survivor log.
She was a physician. If she made it to this cache...

You keep going. The script is almost complete.
"""
            },
            {
                "id": "3-3",
                "type": "hybrid",
                "story": """
The final check: is your callsign on the authorized list?

The half-written script shows:

    authorized = ["Marcus", "Reyes", "Dr. Okafor", "Phoenix"]
    callsign = "Phoenix"

You need to complete the check using 'in'.
""",
                "task": 'Type a Python print() statement that checks if callsign is in the authorized list.\nExpected output: True',
                "expected_output": "True",
                "setup_code": 'authorized = ["Marcus", "Reyes", "Dr. Okafor", "Phoenix"]\ncallsign = "Phoenix"',
                "hints": [
                    "You need print() to show the result.",
                    "Use the 'in' keyword: something in something_else",
                    "Try: print(callsign in authorized)"
                ],
                "success": """
True.

The keypad beeps. The door clicks open.

Inside the cache: food, medicine, batteries — and a radio.
A real radio, still in its case.

And sitting beside it: a handwritten note.

    "If you're reading this, the terminal worked.
     We're at the Relay Station. Come find us.
     — Dr. Okafor"

They're alive. And they've been waiting.

> END OF CHAPTER 3
> CHAPTER 4 UNLOCKED: The Relay Signal
"""
            }
        ]
    },
    {
        "id": 4,
        "title": "The Relay Signal",
        "intro": """
You reach Relay Station Omega just after dark.

Inside: four survivors. Marcus. Reyes. Dr. Okafor. A teenage kid
who introduces himself as Wren.

They've been trying to broadcast a signal — but the relay
needs to send the same message to multiple frequencies,
one after another. The script to do it is broken.

"It kept stopping after the first one," Reyes says.
"We need a loop."

You sit down at the relay terminal. You know what to do.
""",
        "challenges": [
            {
                "id": "4-1",
                "type": "multiple_choice",
                "story": """
To send a message to multiple frequencies, you need to
repeat an action — once for each frequency in the list.

Python's for loop does exactly this:

    frequencies = ["107.3", "91.5", "88.1"]

    for freq in frequencies:
        print(freq)

This would output:
    107.3
    91.5
    88.1

The loop goes through each item and runs the indented code for each one.
""",
                "task": "What does a for loop do?",
                "options": {
                    "A": "It runs code once and stops",
                    "B": "It repeats a block of code for each item in a collection",
                    "C": "It creates a new list",
                    "D": "It checks if two values are equal"
                },
                "answer": "B",
                "hints": [
                    "The key word is 'for each' — it runs once per item.",
                    "With 3 frequencies, the indented code runs 3 times.",
                    "It's B — a for loop repeats code for each item in a collection."
                ],
                "success": """
"That's it," Wren says, leaning over your shoulder.
"We just need to loop through the frequencies."

You nod. But knowing what a loop does is one thing.
Writing one is another.
"""
            },
            {
                "id": "4-2",
                "type": "code",
                "story": """
The relay is ready. You have a list of survivor names
and you need to broadcast a message to each one.

The setup:
    survivors = ["Marcus", "Reyes", "Dr. Okafor", "Wren"]

You need to print a message for each survivor.
""",
                "task": 'Write a for loop that prints "Calling: " followed by each name.\n\nExpected output:\n    Calling: Marcus\n    Calling: Reyes\n    Calling: Dr. Okafor\n    Calling: Wren',
                "expected_output": "Calling: Marcus\nCalling: Reyes\nCalling: Dr. Okafor\nCalling: Wren",
                "setup_code": 'survivors = ["Marcus", "Reyes", "Dr. Okafor", "Wren"]',
                "hints": [
                    "Start with: for name in survivors:",
                    "Inside the loop (indented), use print() to show the message.",
                    'Try:\nfor name in survivors:\n    print("Calling: " + name)'
                ],
                "success": """
The relay crackles to life.

    Calling: Marcus
    Calling: Reyes
    Calling: Dr. Okafor
    Calling: Wren

Each name echoes through the station speakers.

Then — silence. Then static. Then a voice.
A voice none of them recognize.

"...I hear you. This is Station Eleven.
 We've been dark for eight months.
 How many of you are there?"

Everyone in the room goes still.

Dr. Okafor grabs the mic. "Five. We have five."

A long pause.

"We have forty-three."

> END OF CHAPTER 4
> CHAPTER 5 UNLOCKED: The Decoder
"""
            }
        ]
    },
    {
        "id": 5,
        "title": "The Decoder",
        "intro": """
Station Eleven. Forty-three survivors, two hundred kilometers north.

But their transmissions are being intercepted. Someone — or something —
is jamming their signal when it carries plaintext. They've been
sending encoded messages, but you don't have the decoder.

"They sent us the algorithm," Marcus says, pulling up a file.
"We just need someone to build it."

The algorithm is simple: each word in a message gets a prefix
based on its position. Position 1 gets "ALPHA-", position 2 gets "BETA-",
and so on. But it needs to be a reusable function — something you can
call over and over as new messages come in.

You crack your knuckles. This is what Chapter 5 is about.
""",
        "challenges": [
            {
                "id": "5-1",
                "type": "multiple_choice",
                "story": """
A FUNCTION is a reusable block of code you define once and
can call as many times as you need.

    def greet(name):
        print("Hello, " + name)

    greet("Marcus")   →  Hello, Marcus
    greet("Wren")     →  Hello, Wren

- def starts the definition
- greet is the function name
- name is a PARAMETER — a variable the function receives
- The indented code is what runs each time you call it
""",
                "task": "What keyword do you use to define a function in Python?",
                "options": {
                    "A": "function",
                    "B": "define",
                    "C": "def",
                    "D": "create"
                },
                "answer": "C",
                "hints": [
                    "It's a short keyword — only 3 letters.",
                    "It's short for 'define'.",
                    "It's C — def."
                ],
                "success": """
def. Define. You can feel the pieces coming together.

A function is just a named set of instructions.
You define it once. You use it forever.

Time to build the decoder.
"""
            },
            {
                "id": "5-2",
                "type": "multiple_choice",
                "story": """
Functions can also RETURN a value — send something back
to whoever called them:

    def add_prefix(word):
        return "ALPHA-" + word

    result = add_prefix("Phoenix")
    print(result)   →  ALPHA-Phoenix

The return statement sends the result back out of the function.
""",
                "task": "What does the return statement do?",
                "options": {
                    "A": "It prints a value to the screen",
                    "B": "It ends the program",
                    "C": "It sends a value back to whoever called the function",
                    "D": "It creates a new variable"
                },
                "answer": "C",
                "hints": [
                    "It doesn't print — it sends back a value.",
                    "Think of a function like a vending machine — you put something in, you get something back.",
                    "It's C — return sends a value back to the caller."
                ],
                "success": """
Return. Send it back.

You understand now. A function takes something in,
does something with it, and hands something back.

The decoder will take a message, transform each word,
and return the encoded result.

Almost there.
"""
            },
            {
                "id": "5-3",
                "type": "code",
                "story": """
This is it. The final piece.

You need to write a function called decode_message that:
- Takes a list of words as a parameter
- Loops through the words
- Prints each word with "DECODED: " in front of it

The setup:
    message = ["SHELTER", "NORTH", "TUNNEL", "SAFE"]
""",
                "task": 'Write a function called decode_message that takes a list called words,\nand prints "DECODED: " + each word.\n\nThen call it with the message list.\n\nExpected output:\n    DECODED: SHELTER\n    DECODED: NORTH\n    DECODED: TUNNEL\n    DECODED: SAFE',
                "expected_output": "DECODED: SHELTER\nDECODED: NORTH\nDECODED: TUNNEL\nDECODED: SAFE",
                "setup_code": 'message = ["SHELTER", "NORTH", "TUNNEL", "SAFE"]',
                "hints": [
                    "Start with: def decode_message(words):",
                    "Inside the function, write a for loop over words.",
                    'Try:\ndef decode_message(words):\n    for word in words:\n        print("DECODED: " + word)\n\ndecode_message(message)'
                ],
                "success": """
    DECODED: SHELTER
    DECODED: NORTH
    DECODED: TUNNEL
    DECODED: SAFE

The room goes quiet.

Shelter. North. Tunnel. Safe.

Station Eleven isn't just surviving — they've found something.
A shelter. Underground. North of the city.
And they're saying it's safe.

Marcus grabs your arm. "That message was sent three weeks ago."

Dr. Okafor is already on the radio.
"Station Eleven, this is Relay Omega. We decoded your message.
 We're coming north. How do we find you?"

The static clears.

"Follow the signal," the voice says.
"We've been waiting for someone who could read it."

You look around the room. Five survivors, a working relay,
and a message that just changed everything.

The terminal hums.

    > TRANSMISSION COMPLETE
    > YOU HAVE REACHED THE END OF THE CURRENT SIGNAL
    > MORE CHAPTERS COMING...
    > STAY ALIVE OUT THERE.

> END OF CHAPTER 5
"""
            }
        ]
    }
]
