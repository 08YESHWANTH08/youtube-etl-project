
# 📊 YouTube Trending Videos ETL Pipeline Project

This project is a complete end-to-end **ETL (Extract, Transform, Load) pipeline** built using Python that collects trending YouTube video data, cleans and processes it, and stores it into a MySQL database. It also includes a Streamlit-powered dashboard to visualize the trending data interactively.

---

## 🚀 Features

- 📥 Extracts trending video data using the **YouTube Data API**
- 🧹 Transforms and cleans raw data using **Pandas**
- 🗃️ Loads data into **MySQL database**
- 📊 Interactive dashboard built with **Streamlit**
- 🔒 Configuration handled securely using **python-dotenv**

---

## 🛠️ Technologies Used

- Python
- YouTube Data API (v3)
- Pandas
- MySQL
- MySQL Connector (mysql-connector-python)
- Streamlit
- python-dotenv
- requests

---

## 🧱 Project Structure

- `main.py` - Runs the full ETL pipeline
- `extractor/fetch_youtube_data.py` - Extracts data from YouTube API
- `transformer/clean_data.py` - Cleans and transforms the extracted data
- `loader/load_to_mysql.py` - Loads the processed data into MySQL
- `dashboard/app.py` - Streamlit dashboard to visualize data
- `utils/config.py` - Stores reusable constants/config
- `.env` - Stores API keys and DB credentials

---

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/08YESHWANTH08/youtube-etl-project.git
cd youtube-etl-project
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # For Windows
# source venv/bin/activate   # For Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file with the following contents:

```
YOUTUBE_API_KEY=your_youtube_api_key
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=your_db_name
```

### 5. Run the ETL Pipeline

```bash
python main.py
```

### 6. Launch the Dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📷 Sample Dashboard Screenshot

![utube-etl1](https://github.com/user-attachments/assets/17ab3b3f-21af-4ddb-90b6-d6ae51873f15)

![utube-etl2](https://github.com/user-attachments/assets/60942e0f-3637-494d-8bee-26eb0939c6ab)

## 📚 What I Learned

- How to integrate external APIs like YouTube Data API
- Writing modular and reusable Python code
- Using pandas to clean and transform data
- Connecting and interacting with MySQL using Python
- Building real-time dashboards with Streamlit
- Structuring a production-ready ETL project

---

## 📌 License

This project is open source and free to use under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Yeshwanth**  
[LinkedIn](https://www.linkedin.com/in/yeshwanth-arulkumar-696444355/) | [GitHub](https://github.com/08YESHWANTH08)
