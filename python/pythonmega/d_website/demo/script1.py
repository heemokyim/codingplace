# What is flask?
# = website framework

# pip install flask

from flask import Flask, render_template

app=Flask(__name__)

# routing = mapping proper function for each endpoint
@app.route('/')
def home():
    # when routed here, server responses with home.html
    # Then where is apache? (something that manages static, etc)
    # == Maybe inside of flask object

    # folder should be named 'templates'
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    # debug=True same with nodemon
    app.run(debug=True,port=3000)

elif __name__=='app':
    print('when another script imports this one')
