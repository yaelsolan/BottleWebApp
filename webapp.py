from bottle import route, run, template, get, post, request, error, response, static_file
@route('/')
def index():
	return "My first web app with bottle"
	
@route('/hello')
@route('/hello/<name>')
def hello(name="your_name"):
	return template("Hello {{template_name}}", template_name=name)
	
@route('/wiki/Learn')
def wiki_Learn():
	return "Lets learn!"

@route('/follow/yooli')
def follow_yooli():
	return "Follow yooli"


@get('/login') #create new route; request
def login ():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') 
def check_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
	
@error(404)
def error404(error):
    return 'Nothing here, sorry'	
    
@route('/iso')
def get_iso():
    response.charset = 'ISO-8859-15'
    return u'This will be sent with ISO-8859-15 encoding.'

@route('/latin9')
def get_latin():
    response.content_type = 'text/html; charset=latin9'
    return u'ISO-8859-15 is also known as latin9.'
	
@route('/images/<filename:re:.*\.jpeg>')
def send_image(filename):
    return static_file(filename, root='/home/yael/bottle', mimetype='yool.jpeg')

@route('/static/<yool:/home/yael/bottle>')
def send_static(yool):
    return static_file(filename, root='/home/yael/bottle')
	
run(host="localhost", port=8080, debug=True, reloader=True)
