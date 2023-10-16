from sys                import argv
from            .server import start_server
#
#if __name__ == '__main__':
#    if len(sys.argv) < 3: raise ValueError("Command is required")
#
#    port    = int(sys.argv[1])
#    command = sys.argv[2:]
#    start_server(port, command=command)

if __name__ == '__main__':
  if len(argv) < 3: raise ValueError("Command is required")

  port = int(argv[1])
  args =     argv[2:]

  # Check if --no-stdin flag is specified
  if args[0].startswith("--no-stdin="): stdin_flag = args.pop(0)[11:]
  else:                                 stdin_flag = None

  # Find the index of -- argument (if present)
  if "--" in args:
    cmd_index = args.index("--")
    cmd_args  = args[cmd_index+1:]
    args      = args[:cmd_index]
  else: cmd_index = None

  # Separate the command from the arguments
  command      = args[0]
  command_args = args[1:]

  if stdin_flag and stdin_flag.startswith("--"):
    # Construct the modified command with the host flag
    modified_command_args = []
    for arg in command_args:
      modified_command_args.append(arg.replace("--", f"{stdin_flag}="))

    modified_command = [command] + modified_command_args
    start_server(port, command=modified_command)
  else:
    # Run the original command with stdin support
    if cmd_index is not None: command_args.extend(cmd_args)
    start_server(port, command=[command] + command_args)

