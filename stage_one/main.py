from flask import Flask, json, request
import datetime
import pytz  # Import the pytz library

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home_page():
    # Define the West African Time (WAT) timezone
    wat_timezone = pytz.timezone('Africa/Lagos')

    # Get the current time in WAT
    current_time = datetime.datetime.now(wat_timezone)

    # Get the current day in WAT
    current_day = current_time.strftime("%A")

    # Get the slack_name and track query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    data_set = {
        "slack_name": slack_name if slack_name else "Abdulrasheed Apampa",
        "current_day": current_day,
        "utc_time": current_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": track if track else "backend",
        "github_file_url": "https://github.com/AbdulrasheedApampa/HNGx-Internship/blob/main/stage_one/main.py",
        "github_repo_url": "https://github.com/AbdulrasheedApampa/HNGx-Internship",
        "status_code": 200
    }

    # Convert the dictionary to JSON format with each item on a separate line
    json_data = json.dumps(data_set, indent=4)

    # Replace commas with commas and line breaks
    json_data = json_data.replace(', ', ',\n')

    # Return the modified JSON data as a response
    return json_data

if __name__ == '__main__':
    app.run(port=7777)
