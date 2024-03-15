from flask import Flask,render_template,request,redirect,url_for
import sqlite3
con=sqlite3.connect("data.db",check_same_thread=False)
cur=con.cursor()
con.execute("create table if not exists new(name varchar(30),email varchar(30),password varchar(30))")

app=Flask(__name__)

#VIEW

@app.route("/view")
def index():
    con=sqlite3.connect("data.db",check_same_thread=False)
    cur=con.cursor()
    cur.execute("select * from new")

    data=cur.fetchall()
    return render_template("index.html",data=data)



@app.route("/register",methods=["POST","GET"])
def register():
    if request.method=="POST":
        name=request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        conform_password=request.form["conform_password"]
        if password==conform_password:
            cur.execute("insert into new(name,email,password)values(?,?,?)",(name,email,password))
            con.commit()
            #return "done!!!!!!!!!"
            return redirect("register")
        return "Enter the correct password"


    return render_template("register.html")


#UPDATE

@app.route("/update",methods=["POST","GET"])
def update():
    if request.method=="POST":
       
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]

        conn=sqlite3.connect("data.db")
        cursor=conn.cursor()
        cursor.execute("update new set name=?,email=? where password=?",(name,email,password))
        conn.commit()

        return redirect(url_for("index"))
    return render_template("update.html")

#DELETE

@app.route("/delete",methods=["POST","GET"])
def delete():
    if request.method=="POST":
        name=request.form["name"]
        
        con=sqlite3.connect("data.db")
        cur=con.cursor()

        cur.execute("delete from new where name=?",(name,))
        con.commit()
        return redirect(url_for("index"))
    return render_template("delete.html")
   

if __name__=="__main__":
    app.run(debug=True) 