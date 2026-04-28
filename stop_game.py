#stop_game.py
import subprocess

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {cmd}\nError: {e}")

def stop_game():
    print("Stopping and removing all containers...")
    for name in ["player1", "player2", "player3", "hack-server"]:
        run(f"docker rm -f {name} || true")
    run("docker network rm hacknet || true")
    print("Game stopped successfully.")