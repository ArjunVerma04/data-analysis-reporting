import sqlite3
import pandas as pd

def create_database():
    conn = sqlite3.connect("business.db")
    df = pd.read_csv("data/business_data.csv")
    df.to_sql("business", conn, if_exists="replace", index=False)
    conn.close()

def get_connection():
    return sqlite3.connect("business.db")