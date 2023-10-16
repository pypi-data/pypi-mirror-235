from docker     import errors, from_env
from flask      import Flask, request
from subprocess import check_output
from traceback  import print_tb

def cis_daemon(dc, url, recursive=True, branch=None, image='innovanon/build'):
  print(f'cis_daemon(url={url}, recursive={recursive}, branch={branch}, image={image})', flush=True)

  brn = f'--branch {branch}' if branch else ""
  rec =  '--recursive' if recursive else ""
  cmd = f'{url} {brn} {rec}'
  print(f'brn: {brn}', flush=True)
  print(f'rec: {rec}', flush=True)
  print(f'cmd: {cmd}', flush=True)

  try:
    # Create a Docker container within the container
    # image has ENTRYPOINT ["/usr/local/bin/cis"]
    cont = dc.containers.create(image, command=cmd)
    print('container created', flush=True)

    # Start the container
    cont.start()
    print('container started', flush=True)

    # Wait for the container to complete its execution
    cont.wait()
    print('container execution completed', flush=True)

    # Get the container logs
    logs = cont.logs().decode('utf-8')
    print(f'container logs: {logs}', flush=True)

    # Remove the container
    cont.remove()
    print('container removed', flush=True)

    # return useful output and HTML status
    return logs, 200

  except errors.APIError as e:
    # HandlDocker API errors
    error_message = f'Docker APIError: {e.response.status_code} {e.response.reason}'
    print(error_message, flush=True)
    return error_message, 500

  except Exception as e:
    # Handle any other exceptions
    error_message = f'Error: {str(e)}'
    print(error_message, flush=True)
    return error_message, 500

def create_app(dc):
  app = Flask(__name__)

  def get_arg(request, arg, *args):
    if request.method       == 'GET':              return request.args      .get(arg, *args);
    if request.method       != 'POST':             raise  Exception('Invalid method')
    if request.content_type == 'application/json': return request.get_json().get(arg, *args)
    return                                                request.form      .get(arg, *args) or \
                                                        request.args      .get(arg, *args)

  @app.route('/git', methods=['GET', 'POST'])
  def upload():
    print('upload() 1', flush=True)
    try:
      url = get_arg(request, 'url')
      print(f'url: {url}', flush=True)
      rec = get_arg(request, 'recursive')
      print(f'rec: {rec}', flush=True)
      brn = get_arg(request, 'branch')
      print(f'brn: {brn}', flush=True)
      img = get_arg(request, 'image')
      print(f'img: {img}', flush=True)
    except Exception as e: return str(e), 204
    print('upload() 2', flush=True)
    return cis_daemon(dc, url, rec, brn, img)

  return app

def start_server(host="0.0.0.0", port=2223, *args, **kwargs):
  dc  = from_env()
  app = create_app(dc, **kwargs)
  app.run(debug=True, host=host, port=port, *args)

# https://www.easydevguide.com/posts/curl_upload_flask

