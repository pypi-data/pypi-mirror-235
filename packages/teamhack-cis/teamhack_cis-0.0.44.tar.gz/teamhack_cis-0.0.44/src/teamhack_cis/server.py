from docker     import errors, from_env
from flask      import Flask, request
from subprocess import check_output
from traceback  import print_tb

def cis_daemon(dc, url, recursive=True, branch=None, image='innovanon/build'):
  print(f'cis_daemon(url={url}, recursive={recursive}, branch={branch}, image={image})', flush=True)
  # TODO entrypoint /usr/local/bin/cis
  # TODO command    {url} {branch} {recursive}
  # TODO volumes
  #cont = dc.containers.create(image, command='/bin/sh')

  brn = f'--branch {branch}' if branch    else ""
  rec =  '--recursive'       if recursive else ""
  cmd = f'{url} {brn} {rec}'
  print(f'brn: {brn}', flush=True)
  print(f'rec: {rec}', flush=True)
  print(f'cmd: {cmd}', flush=True)

  # Create a Docker container within the container
  cont = dc.containers.create(image, command=cmd)
  print('container created', flush=True)

  cont.remove()
  print('container removed', flush=True)

  #try:
  #
  #  # Run git clone command within the container
  #  #rec_cmd =  '--recursive'       if rec    else ""
  #  #brn_cmd = f'--branch={branch}' if branch else ""
  #  #git_cmd = f'git clone {rec_cmd} {brn_cmd} {url} repo'
  #  #cis_cmd = f'if [ -f .cis/run ] ; then .cis/run ; else cis ; fi'
  #  #all_cmd = f'{git_cmd} && cd repo && {cis_cmd}'
  #  #print(f'cmd: {all_cmd}', flush=True)
  #
  #  output = cont.exec_run(all_cmd)
  #  status = output.exit_code
  #  print(f'output: {output}, status: {status}', flush=True)
  #  status = 200 if status == 0 else 204
  #
  #  return output.output.decode('utf-8'), status
  #except errors.APIError as e:
  #  # Handle Docker API errors
  #  print_tb(e.__traceback__)
  #  print(e.explanation)
  #  #return str(e), 500
  #  return "%s\n\n%s\n\n" % (str(e.__traceback__),str(e.explanation)), 500
  #except Exception as e:
  #  # Handle other excpetions (e.g., command execution errors)
  #  print_tb(e.__traceback__)
  #  #return str(e), 400
  #  return str(e.__traceback__), 400
  #
  #finally: cont.remove()

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

