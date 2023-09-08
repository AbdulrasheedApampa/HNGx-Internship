from flask import Flask, json, request
import datetime
import pytz  # Import the pytz library

app = Flask(__name__)

@app.route("/api", methods=['GET'])
def home_page():
    # Define the West African Time (WAT) timezone
    wat_timezone = pytz.timezone('Africa/Lagos')

    # Get the current time in WAT
    current_time =  datetime.datetime.utcnow() 
    utc_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Get the current day in WAT
    current_day = current_time.strftime("%A")

    # Get the slack_name and track query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    data_set = {
        "slack_name": slack_name if slack_name else "Abdulrasheed Apampa",
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track if track else "backend",
        "github_file_url": "https://github.com/AbdulrasheedApampa/HNGx-Internship/blob/main/stage_one/main.py",
        "github_repo_url": "https://github.com/AbdulrasheedApampa/HNGx-Internship",
        "status_code": 200
    }
    
    return data_set

if __name__ == '__main__':
    app.run(debug=True)
