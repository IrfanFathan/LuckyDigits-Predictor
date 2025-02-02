# LuckyDigits-Predictor
A Machine Learning Model for Predicting the Most Probable Last Three Digits
### file structre 
```plaintext
LuckyDigits-Predictor/
│── 📂 backend/                 # Backend with Django or Flask
│   │── 📂 database/            # Database-related files
│   │   │── create_db.py        # Creates the SQLite database
│   │   │── insert_data.py      # Inserts scraped data into the database
│   │   │── fetch_data.py       # Fetches past records for ML training
│   │── 📂 api/                 # API for predictions
│   │   │── main.py             # Flask/Django API to get predictions
│── 📂 ml_model/                # Machine Learning model
│   │── train_model.py          # Trains the ML model
│   │── predict.py              # Predicts the next three digits
│   │── model.pkl               # Saved trained model
│── 📂 scraper/                 # Web scraping scripts
│   │── scrape_data.py          # Scrapes lottery data from websites
│── 📂 frontend/                # Frontend (optional, if needed)
│   │── app.py                  # Simple Flask-based UI (or React, Flutter)
│── 📂 data/                    # Stores datasets
│   │── lottery_data.csv         # Dataset for training
│── requirements.txt            # Python dependencies
│── README.md                   # Project documentation
```
