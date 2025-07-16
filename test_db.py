from sqlalchemy import create_engine

url = "mysql+pymysql://root:Husain%402004@localhost:3306/gutenberg"

try:
    engine = create_engine(url)
    conn = engine.connect()
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
