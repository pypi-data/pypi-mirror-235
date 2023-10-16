from flask      import Flask, request
from tempfile   import NamedTemporaryFile
from subprocess import check_output
from json       import loads, JSONDecodeError
from xmltodict  import unparse

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

def convert_json(output):
  try: data = loads  (output)
  except JSONDecodeError as e: raise Exception('Output is not valid JSON: %s\n\n%s' % (str(e), output,))
  try xml  = unparse(data)
  except Exception as e: raise Exception('Output is not valid XML: %s\n\n%s' % (str(e), data,))
  return xml

def convert_output(output, convert=None):
  if convert == 'json': return convert_json(output)
  raise Exception("Not yet implemented: see TODO")

def run_command(command, convert=None, **kwargs):
  output = check_output(command, **kwargs)
  if convert is None: return output
  return convert_output(output)

def wrap_input(command, data, iflag=None, convert=None):
  if iflag is None: return run_command(command, convert=convert, input=data)
  output = ""
  for line in data.splitlines():
    cmd     = command + [iflag, line]
    output += run_command(cmd, convert=convert)
  return output

def wrap_output(command, data, iflag=None, oflag=None, convert=None):
  if oflag is None: return wrap_input(command, data, iflag, convert), None

  with temp as NamedTemporaryFile():
    cmd    = command + [oflag, temp.name]
    extra  = wrap_input(cmd, data, iflag, convert)
    temp.seek(0)
    output = temp.read()
    return output, extra

def create_app(command, convert=None, iflag=None, oflag=None):
  app = Flask(__name__)

  @app.route('/upload', methods=['PUT'])
  def upload():
    data = request.get_data()
    print(f'data: {data}')

    output, extra = wrap_output(command, data, iflag, oflag, convert)
    print(f'output: {output}')
    if extra: print(f'extra: {extra}')
    return output

  return app

def start_server(command, port, host="0.0.0.0", convert=None, iflag=None, oflag=None, *args, **kwargs):
  app = create_app(command=command, convert=convert, iflag=iflag, oflag=oflag, **kwargs)
  app.run(debug=True, host=host, port=port, *args)

