# Lake Tahoe Family Puzzle Tracker 🧩

A web app to track my family's progress through a series of Lake Tahoe-themed puzzles. Each level is unlocked by entering the correct code. Hints are available for each puzzle. Designed with a Tahoe-inspired look.

## Features
- Simple username login (no password)
- 10 puzzles/levels (customizable)
- Enter code to unlock next puzzle
- Show hint button for each puzzle
- Tahoe/forest/lake themed background

## Setup
1. Clone this repo
2. Install dependencies (requires Python 3.8+):
   ```sh
   pip3 install uv
   uv pip install -r requirements.txt  # or use uv add streamlit if not present
   ```
3. Run the app:
   ```sh
   source .venv/bin/activate && streamlit run main.py
   ```

## Usage
- Open the app in your browser (usually http://localhost:8501)
- Enter your name to start
- Enter the code for the current puzzle to unlock the next
- Click "Show Hint" if you need help
- Progress is tracked per session (not persistent)

## Customization
- Edit `main.py` to set real codes and hints for each puzzle in the `LEVELS` list.
- To add more puzzles, add more entries to the `LEVELS` list.

## License
MIT
