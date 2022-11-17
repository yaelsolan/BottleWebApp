from bottle import route, run, template, get, post, request
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
def ():
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
	
run(host="localhost", port=8080, debug=True, reloader=True)
