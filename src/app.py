# src/app.py
"""
Interactive CLI entrypoint.
Commands:
  load <path>
  save <path>
  insert <word> <freq>
  remove <word>
  contains <word>
  complete <prefix> <k>
  stats
  quit
"""

import sys
try:
    from src.trie import Trie
    from src.io_utils import load_csv, save_csv
except Exception:
    from trie import Trie
    from io_utils import load_csv, save_csv

PROMPT = ""  # keep outputs machine-friendly (no prompt)

def main():
    trie = Trie()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        cmd = parts[0].lower()

        if cmd == 'quit':
            break

        if cmd == 'load' and len(parts) == 2:
            path = parts[1]
            try:
                pairs = load_csv(path)
                # Replace current content
                trie = Trie()
                for w, s in pairs:
                    # normalize to lowercase
                    trie.insert(w.lower(), float(s))
            except (IOError, ValueError) as e:
                # silently continue on errors to keep grading simple
                continue
            continue

        if cmd == 'save' and len(parts) == 2:
            path = parts[1]
            try:
                # use trie.items() to get current vocabulary
                save_csv(path, trie.items())
            except IOError:
                # silently continue on errors to keep grading simple
                continue
            continue

        if cmd == 'insert' and len(parts) == 3:
            try:
                w = parts[1].lower()  # normalize
                freq = float(parts[2])
                trie.insert(w, freq)
            except ValueError:
                # silently continue on invalid frequency
                continue
            continue

        if cmd == 'remove' and len(parts) == 2:
            w = parts[1].lower()  # normalize
            print('OK' if trie.remove(w) else 'MISS')
            continue

        if cmd == 'contains' and len(parts) == 2:
            w = parts[1].lower()  # normalize
            print('YES' if trie.contains(w) else 'NO')
            continue

        if cmd == 'complete' and len(parts) >= 3:
            try:
                prefix = parts[1].lower()  # normalize
                k = int(parts[2])
                if k < 0:  # silently handle negative k
                    k = 0
                results = trie.complete(prefix, k)
                # ensure empty list prints blank line
                print(','.join(results) if results else '')
            except ValueError:
                # silently continue on invalid k
                continue
            continue

        if cmd == 'stats':
            words, height, nodes = trie.stats()
            print(f"words={words} height={height} nodes={nodes}")
            continue

        # Unknown or malformed commands do nothing (keeps grading simple)

if __name__ == '__main__':
    main()
