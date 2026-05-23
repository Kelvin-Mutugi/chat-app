from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None  # Start with no name by default
    
    if request.method == 'POST':
        # Get the name from the form input fields
        name = request.form.get('user_name')
        
    # Send the name variable back to the HTML template
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
