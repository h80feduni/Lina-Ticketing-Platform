from flask import Flask, render_template

app = Flask(__name__)

# Route for Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for Dashboard page
@app.route('/dashboard')
def dashboard():
    return rendered_template('dashboard.html')

if __name__ == '__main__':
   app.run(debug=True)
   
