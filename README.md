# Python Chess

A terminal-based chess game written in Python 3, supporting local play against a simple AI or another player via network. This project is a Python port of the author's C++ chess program.

![Screenshot](https://github.com/matthewJamesAbbott/Python-Chess/blob/main/pythonChess.png)

---

## Features

- **Playable against a computer AI or another human**
- **Text-based terminal interface**
- **Supports standalone, server, and client modes for network play**
- **Basic move and board validation**
- **Simple AI: makes moves via decision trees and piece evaluation**
- **Unicode chess pieces shown in the terminal for a visually clear board**

---

## Getting Started

### Prerequisites

- Python **3.10 or above**
- Works in any terminal (Linux, macOS, or Windows with Unicode support)

### Installation

Clone the repository:
```bash
git clone https://github.com/matthewJamesAbbott/Python-Chess.git
cd Python-Chess
```

### Running

**Standalone (vs computer or two on the same device):**
```bash
python3 main.py
```

**Server mode (wait for remote player):**
```bash
python3 main.py -s
```

**Client mode (connect to a server):**
```bash
python3 main.py -c [SERVER_IP_ADDRESS]
```

**Help:**
```bash
python3 main.py --help
```

---

## Controls

- Follow terminal prompts:  
  Enter the row and column for the piece to move (row: 1–8, column: a–h) and the move destination.
- Use `9` at any prompt to exit immediately.
- The board and pieces print in Unicode for clarity in compatible terminals.

---

## Project Structure

- **`main.py`** - Program entrypoint & command-line parser; sets up mode (standalone, client, server).
- **`Game.py`** - Main game logic, move validation, board printing, AI moves, and user move handling.
- **`Engine.py`** - Contains AI class: builds a move tree, selects moves for computer player.
- **`MoveCalculator.py`** - Calculates all legal moves for a piece and provides move lists and validation.
- **`Board.py`** - Simple 8x8 chessboard implementation, with setters/getters for positions.

---

## AI & Implementation Notes

- The AI uses a decision tree of possible moves, with a basic material-evaluation strategy (captures prioritized, fallback if move puts AI in check).
- Designed to mimic the logic from the original C++ version.

---

## Limitations

- Terminal only (no GUI).
- Protocol/network play is basic and uses port 9008, both endpoints must be able to connect.
- No save/load or persistence of games.
- Not a competitive chess AI (suitable for casual play/learning).

---

## License & Authorship

> This code is **not licensed for redistribution or commercial use**;  
> it is published here for learning and personal exploration.
>
> **Created by Matthew James Abbott.**  
> Do not reuse or redistribute without explicit permission.  
> Contact via GitHub for any permission requests.

---

**Enjoy Python Chess!**
