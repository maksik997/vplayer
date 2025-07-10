#!/usr/bin/env python3

import os.path
import sys
from argparse import ArgumentParser
from time import sleep

from player import Player
from visualizer import Cava

def parse_args():
    parser = ArgumentParser(
        description="VPlayer - audio player with playlist and fancy visualization."
    )
    parser.add_argument(
        "files",
        metavar="file",
        nargs="+",
        help="path to audio files to play"
    )
    return parser.parse_args()

def validate_files(files):
    valid = []
    for file in files:
        if not os.path.isfile(file):
            print(f"Error: file not found - {file}", file=sys.stderr)
        else:
            valid.append(file)
    if not valid:
        print("No valid audio files found.", file=sys.stderr)
        sys.exit(1)
    return tuple(valid)

def main():
    args = parse_args()
    playlist = validate_files(args.files)

    player = Player(playlist)
    player.start()
    cava = Cava()

    try:
        while player.is_running():
            sleep(1)
    except KeyboardInterrupt:
        cava.stop()
        print("\nStopping player...")
        player.stop()

if __name__ == "__main__":
    main()
