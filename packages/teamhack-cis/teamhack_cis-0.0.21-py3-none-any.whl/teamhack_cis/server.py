#from tempfile import NamedTemporaryFile
from flask      import Flask, request
from subprocess import check_output

from docker     import errors, from_env

def cis_daemon(dc, url, rec, branch, image):
  # Create a Docker container within the container
  # TODO command
  # TODO volumes
  cont = dc.containers.create(image, command='/bin/sh')
  try:
    # Run git clone command within the container
    rec_cmd =  '--recursive'       if rec    else ""
    brn_cmd = f'--branch={branch}' if branch else ""
    git_cmd = f'git clone {rec_cmd} {brn_cmd} {url} repo'
    cis_cmd = f'if [ -f .cis/run ] ; then .cis/run ; else cis ; fi'
    all_cmd = f'{git_cmd} && cd repo && {cis_cmd}'

    output = cont.exec_run(all_cmd)
    status = output.exit_code
    status = 200 if status == 0 else 204

    return output.output.decode('utf-8'), status
  except errors.APIError as e:
    # Handle Docker API errors
    return str(e), 500
  except Exception as e:
    # Handle other excpetions (e.g., command execution errors)
    return str(e), 400

  finally: cont.remove()

def get_arg(request, arg, *args):
  if request.method       == 'GET':              return request.args      .get(arg, *args);
  if request.method       != 'POST':             raise  Exception('Invalid method')
  if request.content_type == 'application/json': return request.get_json().get(arg, *args)
  return                                                request.form      .get(arg, *args) or \
                                                        request.args      .get(arg, *args)

def create_app(dc):
  app = Flask(__name__)

  @app.route('/git', methods=['GET', 'POST'])
  def upload():
    try:
      url =      get_arg(request, 'url')
      print(f'url: {url}')
      rec = bool(get_arg(request, 'recursive', True))
      print(f'rec: {rec}')
      brn =      get_arg(request, 'branch',    None)
      print(f'brn: {brn}')
      img =      get_arg(request, 'image'     'InnovAnon-Inc/build')
      print(f'img: {img}')
    except Exception as e: return str(e), 204
    return cis_daemon(dc, url, rec, brn, img)

  return app

def start_server(host="0.0.0.0", port=2223, *args, **kwargs):
  dc  = from_env()
  app = create_app(dc, **kwargs)
  app.run(debug=True, host=host, port=port, *args)

# https://www.easydevguide.com/posts/curl_upload_flask

