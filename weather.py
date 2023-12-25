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
        "locations": "Herndon,VA,20170",
        "aggregateHours": 24,
        "unitGroup": "us",
        "shortColumnNames": False,
        "contentType": "csv",
        "key": os.getenv("VISUAL_CROSSING_API_KEY")
    }

    # Send the request
    response = requests.get(endpoint, params=params)

    # Convert the response to a pandas DataFrame
    data = pd.read_csv(pd.compat.StringIO(response.text))

    # Create the graph
    plt.figure(figsize=(10, 6))
    plt.plot(data['time'], data['temperature_2m'])
    plt.title('Temperature over Time')
    plt.xlabel('Time')
    plt.ylabel('Temperature (2m)')

    # Save the graph as an image
    plt.savefig('graph.png')

# Schedule the function to run every hour (or any other desired interval)
schedule.every(1).hours.do(fetch_and_plot)

while True:
    schedule.run_pending()
    time.sleep(1)
