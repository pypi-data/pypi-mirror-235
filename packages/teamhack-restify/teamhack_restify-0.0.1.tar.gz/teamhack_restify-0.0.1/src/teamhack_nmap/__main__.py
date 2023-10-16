from sys                import argv
from            .server import start_server

if __name__ == '__main__':
    if len(sys.argv) < 2: raise ValueError("Command is required")

    command = sys.argv[1:]
    start_server(command=command)

