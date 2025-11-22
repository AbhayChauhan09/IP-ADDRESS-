from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_ip_info(ip):
    try:
        # Free IP lookup API
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        return response.json()
    except:
        return {"error": "Could not fetch IP info"}

@app.route("/")
def track_ip():
    # Get user IP (works on all hosting platforms)
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    info = get_ip_info(ip)

    return jsonify({
        "your_ip": ip,
        "location_info": info
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
