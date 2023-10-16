from flask      import Flask, request
from subprocess import check_output

#def create_app(command):
#  app = Flask(__name__)
#
#  @app.route('/upload', methods=['PUT'])
#  def upload():
#    data = request.get_data()
#    print(f'data: {data}')
#    return check_output(command, input=data)
#
#  return app
#
#def start_server(port, host="0.0.0.0", command=None, *args, **kwargs):
#  if command is None: raise ValueError("Command parameter is required")
#
#  app = create_app(command=command, **kwargs)
#  app.run(debug=True, host=host, port=port, *args)

def create_app(command):
    app = Flask(__name__)

    @app.route('/upload', methods=['PUT'])
    def upload():
        data = request.get_data()
        print(f'data: {data}')

        if command[0] == "--no-stdin":
            # Remove the "--no-stdin" flag from the command arguments
            command_args = command[1:]

            # Get the host flag name from the command
            host_flag = command_args.pop(0)[2:]

            # Iterate over the host list and invoke the command for each host
            results = []
            for host in data.decode().splitlines():
                # Append the host flag and host to the command arguments
                modified_command = [command[0]] + command_args + [f"{host_flag}={host}"]

                # Run the modified command and collect the output
                output = check_output(modified_command)
                results.append(output.decode())

            return "\n".join(results)
        else:
            # Run the original command with stdin support
            return check_output(command, input=data)

    return app

def start_server(port, host="0.0.0.0", command=None, *args, **kwargs):
    if command is None: raise ValueError("Command parameter is required")

    app = create_app(command=command, **kwargs)
    app.run(debug=True, host=host, port=port, *args)

