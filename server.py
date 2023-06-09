from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def index():
    return render_template('index.html',x=8,y=8, color_one='red', color_two='black')

@app.route('/<int:x>')
def checkerboard_x(x):
    return render_template('index.html', x=x, y=8, color_one='red', color_two='black')

@app.route('/<int:x>/<int:y>')
def checkerboard_x_y(x, y):
    return render_template('index.html',x=x, y=y, color_one='red', color_two='black')

@app.route('/<int:x>/<int:y>/<string:color1>')
def checkerboard_x_y_color1(x, y, color1):
    return render_template('index.html', x=x, y=y, color_one=color1, color_two='black')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def checkerboard_x_y_color1_color2(x, y, color1, color2):
    return render_template('index.html', x=x, y=y, color_one=color1, color_two=color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
