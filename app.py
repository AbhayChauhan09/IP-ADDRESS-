from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def show_ip():
    # Works on Render, PythonAnywhere, Replit, Localhost
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    return f"""
    <h1>Your IP Address:</h1>
    <h2>{user_ip}</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

