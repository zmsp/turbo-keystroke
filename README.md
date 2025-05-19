
# Keyboard Keystroke

A lightweight Python script to simulate fast key presses using `pyautogui`.

Supports:
- Key combos (e.g. `shift+s`, `ctrl+alt+d`)
- Character sequences (e.g. `abcd`, `hello`)
- Custom duration, start delay, and interval between presses

## Requirements

- Python 3.7+
- macOS, Linux, or Windows
- Install dependencies:

```bash
pip install pyautogui
````

> On macOS, enable Terminal in System Settings → Privacy & Security → Accessibility.

## Usage

```bash
python spam_keys.py --duration 2 --keys shift+s
python spam_keys.py --duration 1 --keys abcd --start-delay 3 --delay-between 0.01
```

### Arguments

| Name              | Description                                    |
| ----------------- | ---------------------------------------------- |
| `--duration`      | Time to run (minutes, required)                |
| `--keys`          | Key combo (`shift+s`) or sequence (`abcd`)     |
| `--start-delay`   | Delay before start (seconds, default: 5)       |
| `--delay-between` | Time between presses (seconds, default: 0.005) |

## License

MIT – see [LICENSE](./LICENSE).
