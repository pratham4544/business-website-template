from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, 
            template_folder='templates',
            static_folder='assets')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def pages(path):
    if path.endswith('.html'):
        return render_template(path)
    # Serve static files
    return send_from_directory('templates', path)

if __name__ == '__main__':
    app.run(debug=True) 