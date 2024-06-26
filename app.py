from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru , India',
        'salary':'Rs. 10,000,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi , India',
        'salary':'Rs. 15,000,000'
    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location':'Remote',
        'salary':'Rs. 12,000,000'
    },
    {
        'id':4,
        'title':'Backend Engineer',
        'location':'Texas, USA',
        'salary':'Rs. 12,000,000'
    }
    ]

@app.route('/')
def index():
    return render_template('home.html',jobs=JOBS )
@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)

