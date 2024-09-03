from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOB = [
    {
        'id' : 1,
        'title' : 'Web Developer',
        'location' : 'bengaluru, India',
        'salary' : 'Rs.100000'
    },
    {
        'id' : 2,
        'title' : 'Data Analyst',
        'location' : 'Mumbai, India',
        'salary' : 'Rs.120000'
    },
    {
        'id' : 3,
        'title' : 'Cloud Engineer',
        'location' : 'Texas, USA',
        'salary' : 'Rs.150000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOB)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOB)

if __name__ == "__main__":
    app.run()