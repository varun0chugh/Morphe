from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getenv('USER') or os.getenv('USERNAME')

    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 19800)) # 19800 seconds offset for IST

    top_output = subprocess.check_output(['top', '-bn1']).decode('utf-8')

    
    return f"""
    <html>
    <head><title>htop output</title></head>
    <body>
        <h2>Name: {name}</h2>
        <h3>User: {username}</h3>
        <h3>Server Time (IST): {server_time}</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
