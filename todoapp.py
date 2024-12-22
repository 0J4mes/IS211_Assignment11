from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Global list to store To-Do items
todo_list = []

# Helper function for email validation
def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

@app.route('/')
def index():
    """Displays the To-Do list and the form to add a new item."""
    return render_template('index.html', todo_list=todo_list)

@app.route('/submit', methods=['POST'])
def submit():
    """Handles submission of a new To-Do item."""
    task = request.form.get('task', '').strip()
    email = request.form.get('email', '').strip()
    priority = request.form.get('priority', '').strip()

    # Validate inputs
    if not task or not email or not priority:
        return redirect(url_for('index'))  # Missing data
    if not is_valid_email(email):
        return redirect(url_for('index'))  # Invalid email
    if priority not in ['Low', 'Medium', 'High']:
        return redirect(url_for('index'))  # Invalid priority

    # Add the new item to the list
    todo_list.append({'task': task, 'email': email, 'priority': priority})
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear():
    """Clears all To-Do items."""
    todo_list.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
