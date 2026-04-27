import sys
import subprocess

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit("Command failed: {cmd}\nError: {e}")

def container_exists(name):
    result = subprocess.run(f"docker ps -a --filter name={name} --format '{{{{.Names}}}}'", shell=True, capture_output=True, text=True)
    return name in result.stdout.strip().split('\n')

def create_machine(name):
    print(f"Creating machine {name}...")
    
    if container_exists(name):
        run(f" docker rm -f {name}")
    run(f"docker run -dit --name {name} --network hacknet {name}")

    print(f"Machine {name} created successfully.")

