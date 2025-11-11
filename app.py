from flask import Flask, jsonify

app=Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message":"FindMe- Missing Persons Reporting API",
        "description":"Community-driven platform for reporting and tracking missing persons",
        "endpoints":{
            "health":"/api/health",
            "missing_persons":"/api/missing",
            "specific_person":"/api/missing/<id>"
        }
    })

@app.route('/api/health')
def health_check():
    return jsonify({
        "status":"healthy",
        "database":"not connected yet",
        "message":"API is running"
    })

if __name__=='__main__':
    app.run(debug=True, port=5000)