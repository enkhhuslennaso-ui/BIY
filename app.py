from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Render-ийг 24/7 сэрүүн байлгахад ашиглах UptimeRobot ping endpoint
@app.route('/ping')
def ping():
    return jsonify({
        "status": "alive",
        "project": "Ayangat Tsagiin Tuuj - Team 3",
        "developer": "Enkhhuslen",
        "timestamp": datetime.datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
