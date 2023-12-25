import requests
import pandas as pd
import matplotlib.pyplot as plt
import schedule
import time
import os

def fetch_and_plot():
    # Define the endpoint
    endpoint = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast"

    # Define the parameters
    params = {
        "locations": "Singapore",
        "aggregateHours": 24,
        "unitGroup": "us",
        "shortColumnNames": False,
        "contentType": "json",
        "key": os.getenv("VISUAL_CROSSING_API_KEY")
    }

    # Send the request
    response = requests.get(endpoint, params=params)

    # Convert the response to a JSON object
    data_json = response.json()

    # Convert the 'Daily' section of the JSON object to a pandas DataFrame
    data = pd.DataFrame(data_json['Daily'])

    # Create the graph
    plt.figure(figsize=(10, 6))
    plt.plot(pd.to_datetime(data['datetime']), data['temp'])
    plt.title('Temperature over Time')
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    # Save the graph as an image
    plt.savefig('graph.png')

# Schedule the function to run every hour (or any other desired interval)
schedule.every(1).hours.do(fetch_and_plot)

while True:
    schedule.run_pending()
    time.sleep(1)
