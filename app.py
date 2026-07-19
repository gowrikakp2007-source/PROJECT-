from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>AI-Based Crop Health Monitoring System</h1><p>Deployment Successful!</p>"

if __name__ == "__main__":
    app.run(debug=True)