from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/report', methods=['POST'])
def receive_report():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400
    
    # Save test report as test-report.json locally
    with open('test-report.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print("Test report successfully received and saved to test-report.json!")
    return jsonify({"status": "success", "saved": True}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)