# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
import os
import psycopg2

app = Flask(__name__)
CORS(app)

DB_URL = os.environ.get('DATABASE_URL')  # ejemplo: postgresql://usuario:pass@db:5432/citasdb

def get_citas():
    with psycopg2.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, paciente, fecha, motivo FROM citas ORDER BY id;")
            rows = cur.fetchall()
            return [{"id":r[0],"paciente":r[1],"fecha":r[2].isoformat(),"motivo":r[3]} for r in rows]

@app.route('/api/citas', methods=['GET'])
def citas():
    return jsonify(get_citas())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
