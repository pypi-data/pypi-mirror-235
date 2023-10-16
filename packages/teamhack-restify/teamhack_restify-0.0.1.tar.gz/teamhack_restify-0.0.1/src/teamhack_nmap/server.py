from flask      import Flask, request
from subprocess import check_output

def create_app(command):
  app = Flask(__name__)

  @app.route('/upload', methods=['PUT'])
  def upload():
    data = request.get_data()
    print(f'data: {data}')
    return check_output(command, input=data)

  return app

def start_server(host="0.0.0.0", port=55432, command=None, *args, **kwargs):
  if command is None: raise ValueError("Command parameter is required")

  app = create_app(command=command, **kwargs)
  app.run(debug=True, host=host, port=port, *args)

