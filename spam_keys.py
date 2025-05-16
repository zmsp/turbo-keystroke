#!/usr/bin/env python3

import pyautogui
import time
import argparse

# Configure PyAutoGUI for maximum speed
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

def spam_combo_keys(duration_minutes, combo_str, start_delay, delay_between):
    """Spam a key combination like shift+s for a given duration."""
    keys = combo_str.lower().split('+')
    print(f"Spamming combo: {' + '.join(keys)} for {duration_minutes} minutes...")
    time.sleep(start_delay)

    end_time = time.time() + duration_minutes * 60
    while time.time() < end_time:
        for key in keys:
            pyautogui.keyDown(key)
        time.sleep(0.01)
        for key in reversed(keys):
            pyautogui.keyUp(key)
        time.sleep(delay_between)

def spam_sequence_chars(duration_minutes, sequence_str, start_delay, delay_between):
    """Spam a character sequence like abcd repeatedly for a given duration."""
    chars = list(sequence_str)
    print(f"Spamming sequence: {sequence_str} for {duration_minutes} minutes...")
    time.sleep(start_delay)

    end_time = time.time() + duration_minutes * 60
    while time.time() < end_time:
        for char in chars:
            pyautogui.press(char)
            time.sleep(delay_between)

def main():
    parser = argparse.ArgumentParser(
        description="Spam key combinations or character sequences using PyAutoGUI."
    )
    parser.add_argument(
        "--duration", type=float, required=True,
        help="Duration to run in minutes."
    )
    parser.add_argument(
        "--keys", required=True,
        help="Key combo (e.g. shift+s) or character sequence (e.g. abcd)."
    )
    parser.add_argument(
        "--start-delay", type=float, default=5.0,
        help="Start delay in seconds (default: 5)."
    )
    parser.add_argument(
        "--delay-between", type=float, default=0.005,
        help="Delay between presses in seconds (default: 0.005)."
    )

    args = parser.parse_args()

    if '+' in args.keys:
        spam_combo_keys(args.duration, args.keys, args.start_delay, args.delay_between)
    else:
        spam_sequence_chars(args.duration, args.keys, args.start_delay, args.delay_between)

if __name__ == "__main__":
    main()
