import argparse
import sys

from start_game import start_game
from stop_game import stop_game
from create_machine import create_machine

def main():
    parser = argparse.ArgumentParser(prog="hack", description="Hack game management script")
    subparsers = parser.add_subparsers(dest="command")


    start_parser = subparsers.add_parser("start", help="Start a new game")
    start_parser.add_argument("num_players", type=int, choices=[2, 3], help="Number of players (2 or 3)")

    subparsers.add_parser("stop", help="Stop the game and clean up resources")

    create_parser = subparsers.add_parser("create", help="Create a player machine")
    create_parser.add_argument("player_name", type=str, help="Name of the player machine to create")

    args = parser.parse_args()

    if args.command == "start":
        start_game(args.num_players)
    elif args.command == "stop":
        stop_game()
    elif args.command == "create":
        create_machine(args.player_name)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()