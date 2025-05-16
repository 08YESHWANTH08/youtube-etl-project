import mysql.connector
from datetime import datetime

def load_to_mysql(data):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ye$hw@nth8",  # Update with your MySQL password
            database="youtube_trending"  # Update with your database name
        )
        cursor = connection.cursor()

        # Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS videos (
                video_id VARCHAR(255) PRIMARY KEY,
                title TEXT,
                description TEXT,
                published_at DATETIME,
                channel_id VARCHAR(255),
                channel_title VARCHAR(255),
                views BIGINT,
                likes BIGINT,
                dislikes BIGINT
            )
        """)

        # Insert data into the table
        for video in data:
            # Ensure 'published_at' is formatted as a datetime object
            published_at = datetime.strptime(video['published_at'], "%Y-%m-%dT%H:%M:%SZ")  # Convert ISO 8601 to MySQL DATETIME format

            cursor.execute("""
                INSERT INTO videos (video_id, title, description, published_at, channel_id, channel_title, views, likes, dislikes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    title=VALUES(title),
                    description=VALUES(description),
                    published_at=VALUES(published_at),
                    channel_id=VALUES(channel_id),
                    channel_title=VALUES(channel_title),
                    views=VALUES(views),
                    likes=VALUES(likes),
                    dislikes=VALUES(dislikes)
            """, (
                video["video_id"], video["title"], video["description"], published_at,
                video["channel_id"], video["channel_title"], video["views"], video["likes"], video["dislikes"]
            ))

        # Commit and close the connection
        connection.commit()
        print("Data loaded successfully into MySQL.")
    except mysql.connector.Error as err:
        print(f"Error loading data to MySQL: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
