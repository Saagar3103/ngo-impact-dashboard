import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ngo_id TEXT,
            month TEXT,
            people_helped INTEGER,
            events INTEGER,
            funds INTEGER
        )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return "Server is running successfully 🚀"

@app.route('/report', methods=['POST'])
def add_report():
    data = request.json

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO reports (ngo_id, month, people_helped, events, funds)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        data['ngo_id'],
        data['month'],
        data['people_helped'],
        data['events'],
        data['funds']
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Report added successfully"})

@app.route('/dashboard', methods=['GET'])
def get_dashboard():
    month = request.args.get('month')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT ngo_id, people_helped, events, funds
        FROM reports
        WHERE month=?
    ''', (month,))

    rows = cursor.fetchall()
    conn.close()

    ngos = set()
    total_people = 0
    total_events = 0
    total_funds = 0

    for row in rows:
        ngos.add(row[0])
        total_people += row[1]
        total_events += row[2]
        total_funds += row[3]

    return jsonify({
        "total_ngos": len(ngos),
        "total_people": total_people,
        "total_events": total_events,
        "total_funds": total_funds
    })

if __name__ == '__main__':
    app.run(debug=True)