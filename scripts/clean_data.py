import os
from dotenv import load_dotenv
import pandas as pd
import urllib.parse
from sqlalchemy import create_engine

# Load environment variables from .env
load_dotenv()

# Read your DB credentials from .env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# URL-encode sensitive values
DB_USER_ENC = urllib.parse.quote_plus(DB_USER)
DB_PASSWORD_ENC = urllib.parse.quote_plus(DB_PASSWORD)
DB_HOST_ENC = urllib.parse.quote_plus(DB_HOST)
DB_NAME_ENC = urllib.parse.quote_plus(DB_NAME)

# Construct safe SQLAlchemy URL
DATABASE_URL = f"postgresql+psycopg2://{DB_USER_ENC}:{DB_PASSWORD_ENC}@{DB_HOST_ENC}:{DB_PORT}/{DB_NAME_ENC}"
engine = create_engine(DATABASE_URL)

# Load and clean dataset
print("Loading raw dataset...")
df = pd.read_csv("data/raw/listings.csv.gz", compression='gzip')
print(df.columns)
# Cleaning steps (same as before)
df.fillna({
    'name': 'No name provided',
    'host_name': 'Unknown',
    'reviews_per_month': 0
}, inplace=True)

for col in ['neighbourhood_group_cleansed', 'neighbourhood_cleansed', 'host_name']:
    if col in df.columns:
        df[col] = df[col].str.strip().str.lower()
    else:
        print(f"Column '{col}' not found, skipping.")
df.drop_duplicates(inplace=True)



# Save cleaned CSV
df.to_csv("data/cleaned/listings_cleaned.csv", index=False)
print("Cleaned CSV saved to data/cleaned/")

# Save to SQL
df.to_sql("airbnb_listings", engine, if_exists="replace", index=False)
print("Data saved to PostgreSQL successfully!")
