import argparse

from utils import remove_empty_folders
from config import RUN_FOLDER

from rearrange import rearrange
from download import download
from move_to_lib import move
from lyrics import get_lyrics


def main():
    actions = ["download", "move", "rearrange", "lyrics", "remove-empty"]
    qualities = ["FLAC", "MP3_320", "MP3_128"]

    parser = argparse.ArgumentParser(description="Music utils app")

    parser.add_argument("action", choices=actions,
                        help="action you'd like to preform")

    action = parser.parse_known_args()[0].action

    parser.add_argument(
        "--link", "-l", help="link to download (with download action)", required=action == "download")
    parser.add_argument(
        "--quality", "-q", help="download quality (with download action)", choices=qualities)
    parser.add_argument(
        "--rearrange", "-r", help="should rearrange after downloading or not (with download action)", action=argparse.BooleanOptionalAction, default=True)

    parser.add_argument(
        "--song", "-s", help="link to download (with lyrics action)", required=action == "lyrics")
    parser.add_argument(
        "--artist", "-a", help="link to download (with lyrics action)")

    parser.add_argument(
        "--verbose", "-v", action=argparse.BooleanOptionalAction, default=True,
        help="make the action verbose")

    args = parser.parse_args()
    verbose = args.verbose

    if action == "move":
        move()

    elif action == "rearrange":
        rearrange(verbose=verbose)

    elif action == "lyrics":
        song = args.song
        artist = args.artist

        lyrics = get_lyrics(song, artist, verbose=verbose)
        print(lyrics)

    elif action == "download":
        link = args.link
        quality = args.quality or "MP3_320"
        should_rearrange = args.rearrange
        download(link, verbose=verbose, quality=quality,
                 should_rearrange=should_rearrange)

    elif action == "remove-empty":
        remove_empty_folders(RUN_FOLDER)


if __name__ == "__main__":
    main()
