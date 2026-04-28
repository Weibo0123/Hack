#staart_game.py
import sys
import subprocess
from create_machine import create_machine

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(f"Command failed: {cmd}\nError: {e}")

def start_game(num_players):
    try:
        num_players = int(num_players)
        if num_players < 2 or num_players > 3:
            raise ValueError("Number of players must be between 2 and 3.")

        print("Creating Docker network 'hacknet'...")
        run("docker network create hacknet")

        print("Building player images...")
        for i in range(1, num_players + 1):
            run(f"docker build -t player{i} -f Dockerfile.player{i} .")
        run("docker build -t hack-server -f server/Dockerfile server")

        print("Starting server container...")
        run("docker rm -f hack-server || true")
        run("docker run -dit --name hack-server --network hacknet -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock hack-server")
        print("Creating player machines...")
        for i in range(1, num_players + 1):
            create_machine(f"player{i}")

        print("Game started successfully!")
        # TODO: add instructions for players to submit flags

        for i in range(1, num_players + 1):
            print(f"Player{i} can connect to their machine using: docker exec -it player{i} bash")

    except ValueError as e:
        sys.exit(str(e))