from bottle import route, run, template, request


@route('/home', method='POST')
def home():
    print "helloworld"
    data = request.body.read()
    print data
    

run(host='localhost', port=8080, debug=True)
