from bottle import error, run
@error(404)
def error404(error):
    return 'Nothing here, sorry'
    
run(host="localhost", port=8080, debug=True, reloader=True)
