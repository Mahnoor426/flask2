from flask import Flask, redirect, url_for, request
app = Flask(__name__)
 
 
@app.route('/success/<name>') # it tells which url should be called with associated function
def success(name):
    return 'welcome %s' % name
 
 #A GET message is send, and the server returns data
 #The data received by the POST method is not cached by the server.
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm'] # Because the server receives data through the POST method, the value of the “nm” parameter obtained from the form data is obtained by this line
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
 
 
if __name__ == '__main__':
    app.run(debug=True)