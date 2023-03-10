from flask import Flask, render_template,request,flash,redirect,url_for
import sqlite3

app = Flask(__name__)
app.secret_key="123"

con=sqlite3.connect("database.db")
con.execute("CREATE TABLE IF NOT EXISTS data(pid INTEGER PRIMARY KEY ,name TEXT,address TEXT,contact INTEGER,mail TEXT)")
con.close()


connection = sqlite3.connect("user_data.db") 
cursor = connection.cursor()
 
cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, password INTEGER)") 
cursor.execute("INSERT INTO users VALUES ('gayathri', '12345')")
cursor.execute("INSERT INTO users VALUES ('ramya', '67890')")
cursor.execute("INSERT INTO users VALUES ('pujitha', '13579')")

connection.commit() 
 
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        print(name, password)

        #query
        query = "SELECT name, password FROM users where name = '"+name+"' and password = '"+password+"'" 
        cursor.execute(query)

        results = cursor.fetchall()

        if len(results) == 0:
            print("Sorry incorrect")
        else:
            return render_template('index.html')    #place the sqlite

    return render_template('home.html') 

@app.route('/add_record')
def add_record():
    return render_template('add_record.html')

@app.route("/addData",methods=["POST","GET"])
def addData():
    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            contact=request.form['contact']
            mail=request.form['mail']
            con=sqlite3.connect("database.db")
            cur=con.cursor()
            cur.execute("INSERT INTO data(name,address,contact,mail)values(?,?,?,?)",(name,address,contact,mail))
            con.commit()
            flash("Record Added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return render_template('index.html')
            con.close()

@app.route('/view_record')
def view_record():
    con=sqlite3.connect("database.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM data")
    data=cur.fetchall()
    con.close()
    return render_template("view_record.html",data=data)

@app.route('/update_record/<string:id>',methods=["POST","GET"])
def update_record(id):
    con=sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM data where pid=?",(id))
    data = cur.fetchone()
    con.close()

    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            contact=request.form['contact']
            mail=request.form['mail']
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            cur.execute("UPDATE data SET name=?,address=?,contact=?,mail=? where pid=?",(name,address,contact,mail,id))
            con.commit()
            flash("Update Successfully","success")
        except:
            flash("Error in Update Operation","danger")
        finally:
            return render_template('index.html')
            con.close()
    return render_template('update_record.html',data=data)


@app.route('/delete_record/<string:id>')
def delete_record(id):
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return render_template('index.html')
        con.close()

if __name__ == '__main__':
    app.run(debug=True)
