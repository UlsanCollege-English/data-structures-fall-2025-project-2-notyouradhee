# Trie Autocomplete System — Project 2

## What is this project?
This project is like a smart dictionary that helps you quickly find words that start with certain letters. It uses a special tree called a "trie" to store words and their popularity (frequency). You can add, remove, check, and get suggestions for words using simple commands. Everything works fast, even with a huge list of words!

## How does it work?
- **Trie Tree:** Imagine each word is made of letters, and each letter is a branch in a tree. If two words start the same way, they share the same branches for those letters. This saves space and makes searching super quick.
- **Frequency:** Each word remembers how popular it is. When you ask for suggestions, the most popular words come first.
- **Alphabet Order:** If two words are equally popular, the one that comes first in the alphabet is shown first.
- **Lowercase Only:** All words are changed to lowercase so "Apple" and "apple" are treated the same. This keeps things simple.
- **Space Saving:** The tree only keeps branches it needs. If you remove a word and no other word uses those branches, they disappear.
- **Fast Suggestions:** When you type a few letters, the program quickly finds all words that start that way and shows you the best matches.

## What can you do with it?
- Add new words with their popularity
- Remove words you don't want
- Check if a word is in the dictionary
- Get suggestions for words that start with certain letters
- Save your words to a file or load them from a file
- See stats about your dictionary

## What files are organized in this project?
```
.git/
.github/
  workflows/
    classroom.yml
    python.yml
.gitignore
.pytest_cache/
  .gitignore
  CACHEDIR.TAG
  README.md
  v/
.venv/
data/
  .gitkeep
  words.csv
output.csv
pytest.ini
README.md
requirements-dev.txt
scripts/
  make_wordlist.py
src/
  app.py
  io_utils.py
  trie.py
  __init__.py
  __pycache__/
tests/
  test_cli_protocol.py
  test_snapshot_format.py
  test_trie_basic.py
  __pycache__/
  resources/
    small_words.csv
  student/
    test_extreme_edge_cases.py
    test_additional_edge_cases.py
    __pycache__/
```

## How do you use the program? (Step-by-step)
1. Open a terminal in this folder.
2. Run the program:
   ```
   python src/app.py
   ```
3. Type commands when asked. Here are some examples:
   - `load data/words.csv` — Load the big word list
   - `insert apple 10.5` — Add the word "apple" with popularity 10.5
   - `contains apple` — Check if "apple" is in your dictionary
   - `complete app 5` — Get up to 5 suggestions for words starting with "app"
   - `remove apple` — Remove "apple" from your dictionary
   - `save output.csv` — Save your current words to a file
   - `stats` — See how many words, how tall the tree is, and how many branches there are
   - `quit` — Exit the program

## What does the word file look like? (CSV format)
A word file is a list of words and how popular they are. It looks like this:
```
word,frequency
apple,10.5
banana,7.2
```
- The first line is the header (optional).
- Each line after is a word and its frequency, separated by a comma.

## What does the stats command show?
When you type `stats`, you see something like:
```
words=50000 height=12 nodes=60000
```
- **words**: How many words are in your dictionary
- **height**: The longest branch in the tree (the longest word)
- **nodes**: How many branches (nodes) are in the tree

## How do you get the big word list?
You need a file called `data/words.csv` with 50,000 words. To make it:
1. Install the helper tool:
   ```
   pip install wordfreq
   ```
2. Run the script in `scripts/make_wordlist.py` to create the file.

## How do you test if it works?
Type this in the terminal:
```
pytest -v
```
This will check if everything is working, including special cases and tricky situations.

## Developer setup (install dev tools and run tests)
If you're contributing or want the development tools (formatters, linters, coverage), follow these steps in PowerShell.

1. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
```

2. Install development dependencies:

```powershell
pip install -r requirements-dev.txt
```

3. Run tests with coverage:

```powershell
pytest --cov=src -q
```

4. Run linters/formatters (optional):

```powershell
black .
flake8 src tests
mypy src
```

If PowerShell refuses to run `Activate.ps1`, allow running for the session then activate:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
. .venv\Scripts\Activate.ps1
```

## Troubleshooting (If things go wrong)
- If you get errors about missing files, make sure you have `data/words.csv`.
- If your word file is not working, check that it looks like the example above.
- If suggestions look strange, remember that the program always uses lowercase and sorts by popularity, then alphabet.
- If you see extra spaces or prompts, check your code to match the expected output exactly.

## Notes for curious minds
- The program always changes words to lowercase, so "Dog" and "dog" are the same.
- If you try to add an empty word (""), it won't be stored.
- When you ask for suggestions, the most popular words come first, and if there's a tie, the word that comes first in the alphabet wins.
- The tree is smart and only keeps what it needs, so it doesn't waste memory.

## What you will learn (short and simple)
This project is a great, hands-on way to learn a few important ideas:
- How a trie (prefix tree) stores many words efficiently.
- Why some words are faster to find than others (because of shared letters).
- How frequencies (popularity scores) are used to show the best suggestions first.
- How to read and write simple CSV files to save and load data.

These ideas are explained simply in the code and the tests — try changing a few words and see how suggestions change.

## Install Python (quick, beginner-friendly)
If you don't already have Python, here are easy steps to get it.

- Windows: go to https://www.python.org/downloads/windows and download the latest stable installer. Run it and make sure you check "Add Python to PATH" during installation.
- macOS: use the macOS installer at https://www.python.org/downloads/macos or install with Homebrew: `brew install python`.
- Linux: use your package manager, for example on Ubuntu/Debian:

```powershell
sudo apt update; sudo apt install python3 python3-venv python3-pip -y
```

After installing, verify Python is available by running in a terminal:

```powershell
python --version
# or on some systems
python3 --version
```

If you see a Python version (for example `Python 3.11.x`), you're ready to run this project.

If you need help, the official Python downloads page (https://www.python.org/downloads/) has step-by-step installers.

## How to contribute (for students and beginners)
Want to help improve the project? Here's a tiny guide:

1. Fork the repository on GitHub and clone your fork locally.
2. Create a new branch for your change: `git checkout -b fix-or-feature`.
3. Make small, focused changes and run tests locally:

```powershell
python -m pytest -q
```

4. Commit your changes with a clear message and push the branch.
5. Open a Pull Request (PR) on GitHub describing what you changed and why.

Tips:
- Keep changes small and focused so they are easy to review.
- Run tests before creating the PR to ensure you didn't break anything.
- If you're unsure about style or design, open an Issue first to discuss it.

## Complexity Notes

-   **`insert(word, freq)`**: `O(L)`
    -   **Time**: We iterate through each of the `L` characters in the word, performing a constant-time dictionary lookup/insertion at each node.
    -   **Space**: In the worst case (inserting a new word with no shared prefix), we create `L` new `TrieNode` objects.

-   **`remove(word)`**: `O(L)`
    -   **Time**: We first traverse `L` nodes to find the word. We then traverse back up the `L` nodes (at most) to prune empty branches. The total time is `O(L)`.

-   **`contains(word)`**: `O(L)`
    -   **Time**: We traverse at most `L` nodes, one for each character. Each step is a constant-time dictionary lookup.

-   **`complete(prefix, k)`**: `O(M + N log N)`
    -   **Time**:
        1.  `O(M)`: First, we traverse `M` nodes to find the prefix (where `M` is the length of the prefix).
        2.  `O(N)`: From that prefix node, we must perform a DFS to find all `N` candidate words beneath it.
        3.  `O(N log N)`: We then sort the entire list of `N` candidates.
        4.  `O(k)`: Finally, we take the top `k` results.
    -   The dominant step is the sort, making the total time `O(M + N log N)`.
    *(Note: This meets the spec's "acceptable" complexity. A min-heap optimization would achieve O(M + N log k), but your current correct implementation is fine.)*

-   **`stats()`**: `O(T)`
    -   **Time**: Finding the word and node count is `O(1)` (since we track it). However, calculating the height requires a full DFS of the entire trie, visiting all `T` nodes in the worst case.

## Edge-Case Handling

-   **Empty prefix (`complete "" k`)**: Handled correctly. The search starts from the root node and returns the top `k` most frequent words in the entire trie.
-   **Prefix not present**: Handled. The initial traversal for the prefix fails, and `complete` correctly returns an empty list `[]`.
-   **Ties in frequency**: Handled. The `complete` method's sort key `(-x[1], x[0])` correctly uses frequency (descending) as the primary key and lexicographical order (ascending) as the tie-breaker.
-   **Non-alphabetics**: Handled by normalization. All inputs to `insert`, `remove`, `contains`, and `complete` are first converted to lowercase. The current implementation only inserts `[a-z]` characters.
-   **Case sensitivity**: Handled. All inputs are normalized to lowercase, making the trie case-insensitive.
-   **Insert existing word**: Handled. `insert` traverses to the existing word's node and simply updates its `freq` value.
-   **Remove non-existent word**: Handled. `remove` returns `False` if the word path doesn't exist or if the final node's `is_word` flag is already `False`.
-   **Large `k`**: Handled. If `k` is larger than the number of available suggestions, the slice `[:k]` simply returns all found candidates, correctly sorted.
-   **Load/save round-trip**: Handled. `save` iterates all words and saves them. `load` clears the trie and re-inserts all words, ensuring fidelity.


## Who made this?
- notyouradhee
- Assigned By : Prof. Benajamin William Slater


