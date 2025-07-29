from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for flash messages

# -------------------
# Route: Home Page
# -------------------
@app.route('/')
def home():
    return render_template('index.html')

# -------------------
# Route: About Page
# -------------------
@app.route('/about')
def about():
    return render_template('about.html')

# -------------------
# Route: Services Page
# -------------------
@app.route('/services')
def services():
    return render_template('services.html')

# -------------------
# Route: Contact Page (GET)
# -------------------
@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

# -------------------
# Route: Contact Form Submission (POST)
# -------------------
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    # Simulated processing (e.g., send email or store in DB)
    print("Contact Form Submission Received")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")

    flash("Thank you! Your message has been sent.", "success")
    return redirect(url_for('contact'))

# -------------------
# Route: Destinations Page (if needed)
# -------------------
@app.route('/destinations')
def destinations():
    return render_template('destinations.html')  # Make sure you create this page too

# -------------------
# Run the App
# -------------------
if __name__ == '__main__':
    app.run(debug=True)
