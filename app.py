from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flash messages

# Sample data
portfolio_items = [
    {
        'id': 1,
        'title': 'Project One',
        'description': 'A responsive website for a local business',
        'image': 'images/project1.jpg'
    },
    {
        'id': 2,
        'title': 'Project Two',
        'description': 'Mobile application for health tracking',
        'image': 'images/project2.jpg'
    },
    {
        'id': 3,
        'title': 'Project Three',
        'description': 'E-commerce solution with payment integration',
        'image': 'images/project3.jpg'
    }
]

team_members = [
    {
        'name': 'John Doe',
        'position': 'CEO & Founder',
        'bio': 'Expert in strategic planning and business development.',
        'image': 'images/team1.jpg'
    },
    {
        'name': 'Jane Smith',
        'position': 'Lead Designer',
        'bio': 'Creative professional with 10+ years of UI/UX experience.',
        'image': 'images/team2.jpg'
    },
    {
        'name': 'Mike Johnson',
        'position': 'Lead Developer',
        'bio': 'Full-stack developer specializing in modern web technologies.',
        'image': 'images/team3.jpg'
    }
]

@app.route('/')
def home():
    return render_template('index.html', portfolio_items=portfolio_items[:3])

@app.route('/about')
def about():
    return render_template('about.html', team_members=team_members)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', portfolio_items=portfolio_items)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # In a real application, you would process the form data here
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Just simulate form processing
        flash('Thanks for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)