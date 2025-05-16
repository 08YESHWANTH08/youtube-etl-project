import streamlit as st
import pandas as pd
import mysql.connector

def app():
    st.title("YouTube Trending Videos (India)")

    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ye$hw@nth8",
            database="youtube_trending"
        )

        query = "SELECT * FROM videos ORDER BY views DESC LIMIT 20"
        df = pd.read_sql(query, conn)

        st.dataframe(df[['title', 'channel_title', 'views', 'likes']], use_container_width=True)

        # Create bar charts for views and likes
        st.bar_chart(df.set_index('title')[['views']].head(10))
        st.bar_chart(df.set_index('title')[['likes']].head(10))

    except mysql.connector.Error as err:
        st.error(f"Error connecting to MySQL: {err}")
    finally:
        if conn.is_connected():
            conn.close()

if __name__ == "__main__":
    app()
