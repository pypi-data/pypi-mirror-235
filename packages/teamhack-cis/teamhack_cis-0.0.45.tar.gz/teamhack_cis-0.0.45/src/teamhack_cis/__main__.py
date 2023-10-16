from argparse        import ArgumentParser
from         .server import start_server

def parse_args():
  parser = ArgumentParser(description='Start the server')
  parser.add_argument('-H', '--host', type=str, default='0.0.0.0',
                      help='The host to bind to')
  parser.add_argument('-p', '--port', type=int, default=2223,
                      help='The port to listen on')
  return parser.parse_args()

if __name__ == '__main__':
  args = parse_args()
  start_server(host=args.host, port=args.port)

