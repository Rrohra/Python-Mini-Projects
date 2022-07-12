from  flask import Flask, render_template

app =Flask(__name__) #creates an instance of flask

@app.route('/home/') #the address of the app
def home(): #the funtion that the page will have
    return render_template("home.html")  #the contentof the function of the page

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/')
def layout():
    return render_template("layout.html")

if __name__ =="__main__": #if the name is main that means that the code of this file is exceuted
    app.run(debug =True)  #run the app