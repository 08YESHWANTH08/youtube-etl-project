from extractor.fetch_youtube_data import fetch_trending_videos
from transformer.clean_data import clean_data
from loader.load_to_mysql import load_to_mysql
import subprocess
import threading
import time

def run_etl_process():
    # Step 1: Fetch trending videos from YouTube API
    print("Step 1: Fetching trending videos...")
    api_key = "AIzaSyCAdhbUWOstmvyF_3JsmDoryS8GWPV0OBA"  # Set your YouTube API key here
    videos = fetch_trending_videos(api_key)

    # Step 2: Clean the raw video data
    print("Step 2: Cleaning data...")
    cleaned_data = clean_data(videos)

    # Step 3: Load data into MySQL
    print("Step 3: Loading data to MySQL...")
    if not cleaned_data.empty:
        load_to_mysql(cleaned_data.to_dict(orient='records'))
        print("Data loaded successfully into MySQL.")
    else:
        print("No data to load.")

def run_dashboard():
    # Wait for a few seconds to make sure ETL finishes (optional)
    time.sleep(2)
    # Start the Streamlit app
    subprocess.call(["streamlit", "run", "dashboard/app.py"])

if __name__ == "__main__":
    run_etl_process()

    # After ETL, run the dashboard
    run_dashboard()
