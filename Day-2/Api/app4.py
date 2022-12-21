from flask import Flask, redirect, url_for, request
app = Flask(__name__)
 
 
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
 
 
@app.route('/login', methods=['POST', 'GET'])
def blabla():
    if request.method == 'POST':
        # open file:///home/kedar/work/flask_env/app4.html
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        #http://localhost:5000/login?name=username
        user = request.args.get('name')
        return redirect(url_for('success', name=user))
 
 
if __name__ == '__main__':
    print("for POST redirect demo, open file:///home/kedar/work/flask_env/app4.html")
    print("For GET demo open - http://localhost:5000/login?name=username")
    app.run(debug=True)
