from bottle import Bottle, route, run, template, get, post, request, error, response, static_file, abort, redirect


app = Bottle()

@app.route('/')
def index():
	return "My first web app with bottle"
	
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name="your_name"):
	return template("Hello {{template_name}}", template_name=name)
	
@app.route('/wiki/Learn')
def wiki_Learn():
	return "Lets learn!"

@app.route('/follow/yooli')
def follow_yooli():
	return "Follow yooli"


@app.get('/login') #create new route; request
def login ():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@app.post('/login') 
def check_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
	
@app.error(404)
def error404(error):
    return 'Nothing here, sorry'	
    
@app.route('/iso')
def get_iso():
    response.charset = 'ISO-8859-15'
    return 'This will be sent with ISO-8859-15 encoding.'

@app.route('/latin9')
def get_latin():
    response.content_type = 'text/html; charset=latin9'
    return u'ISO-8859-15 is also known as latin9.'
	
@app.route('/images/<filename:re:.*\.jpeg>')
def send_image(filename):
    return static_file(filename, root='/home/yael/bottle', mimetype='yool.jpeg')

@app.route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='/home/yael/bottle')  
    
@app.route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='/home/yael/bottle', download=filename)
    
@app.route('/restricted')
def restricted():
    	abort(401, "Sorry, access denied.") 
    
    
@app.route('/forgeturl')
def wrong():
    redirect("/therighturl")
    
@app.route('/wiki/<page>')
def wiki(page):
    response.set_header('Set-Cookie', 'name=value')
    response.add_header('Set-Cookie', 'name2=value2')
    return 'Hello'
    
@app.route('/hello')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"  
        
@app.route('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        response.set_cookie("account", username, secret='some-secret-key')
        return template("<p>Welcome {{name}}! You are now logged in.</p>", name=username)
    else:
        return "<p>Login failed.</p>"

@app.route('/restricted')
def restricted_area():
    username = request.get_cookie("account", secret='some-secret-key')
    if username:
        return template("Hello {{name}}. Welcome back.", name=username)
    else:
        return "You are not logged in. Access denied."
        
@app.route('/counter')
def counter():
    count = int( request.cookies.get('counter', '0') )
    count += 1
    response.set_cookie('counter', str(count))
    return 'You visited this page %d times' % count
    

if __name__ == '__main__':
    run(app=app,
        server='gunicorn',
        host="localhost",
        port=8080,
        debug=True,
        reloader=True)
