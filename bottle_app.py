
from bottle import static_file, route, run
def static_file_callback(filename):
    return static_file(filename, root='static')
route('/static/<filename>', 'GET', static_file_callback)
run()

