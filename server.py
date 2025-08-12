from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def serve_form():
    return send_from_directory('.', 'Screening.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    answers = [request.form.get(f'q{i}') for i in range(1, 11)]
    
    with open('results.txt', 'a') as f:
        f.write(f"Candidate: {name}\n")
        for i, ans in enumerate(answers, 1):
            f.write(f"Q{i}: {ans}\n")
        f.write("\n")
    
    return "Thank you! Your responses have been recorded."

if __name__ == '__main__':
    app.run()
