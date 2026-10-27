from flask import Flask, render_template_string, request, redirect, url_for, jsonify
import re

app = Flask(__name__)

# In-memory database for submissions
submissions = []

HTML_TEMPLATE = '''
<!doctype html>
<title>Assignment Submission Portal</title>
<div style="font-family: Arial; width: 500px; margin: auto; padding: 20px;">
  <h2>Assignment Submission Portal</h2>
  <form method="post">
    Name: <input type="text" name="name" required><br><br>
    Reg No: <input type="text" name="reg_no" required><br><br>
    Assignment Title: <input type="text" name="title" required><br><br>
    Submission URL: <input type="url" name="url" required><br><br>
    <input type="submit" value="Submit">
  </form>
  {% if error %}
    <p style="color: red;">{{ error }}</p>
  {% endif %}
  <h3>Submissions List</h3>
  <ul>
    {% for sub in submissions %}
      <li>{{ sub.name }} ({{ sub.reg_no }}) - {{ sub.title }}: <a href="{{ sub.url }}" target="_blank">{{ sub.url }}</a></li>
    {% endfor %}
  </ul>
</div>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        reg_no = request.form.get('reg_no')
        title = request.form.get('title')
        url = request.form.get('url')

        # Validation logic
        url_pattern = re.compile(r'^(https?://)?[\w-]+(\.[\w-]+)+[/#?]?.*$')
        
        if not reg_no:
            error = "Missing registration number"
        elif not url or not url_pattern.match(url):
            error = "Invalid submission URL"
        else:
            submissions.append({'name': name, 'reg_no': reg_no, 'title': title, 'url': url})
            return redirect(url_for('index'))

    return render_template_string(HTML_TEMPLATE, submissions=submissions, error=error)

@app.route('/api/submit', methods=['POST'])
def api_submit():
    data = request.json
    if not data or not data.get('reg_no'):
        return jsonify({"status": "rejected", "message": "Missing registration number"}), 400
    
    url = data.get('url', '')
    if not url.startswith('http://') and not url.startswith('https://'):
        return jsonify({"status": "rejected", "message": "Invalid submission URL"}), 400
        
    submissions.append(data)
    return jsonify({"status": "saved", "message": "The submission is saved and appears in the submission list."}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)