# Aim : To implement a price monitoring system using Beautiful Soup for data extraction, 
# Pandas for analysis, SQLite for database storage, and a dashboard for visualization.

# Practical Workflow

    # HTML Product Pages
            ↓
    # Beautiful Soup
            ↓
    # Extract Product + Price
            ↓
    # Pandas
            ↓
    # Analyze Prices
            ↓
    # SQLite Database
            ↓
    # Dashboard
            ↓
    # Business Decision


#================================================================#
# Price Monitoring System
# Beautiful Soup + Pandas + SQLite + Dashboard
# Install Required Libraries - pip install beautifulsoup4 pandas matplotlib
#=================================================================#

from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


# ==========================================
# STEP 1: EXTRACT DATA USING BEAUTIFUL SOUP
# ==========================================

with open("competitor.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

products = soup.find_all("div", class_="product")

product_data = []

for product in products:

    name = product.find("h2").text.strip()

    price = product.find(
        "p", class_="price"
    ).text.strip()

    availability = product.find(
        "p", class_="availability"
    ).text.strip()

    product_data.append({
        "Product": name,
        "Price": float(price),
        "Availability": availability
    })


# ==========================================
# STEP 2: CREATE PANDAS DATAFRAME
# ==========================================

df = pd.DataFrame(product_data)

print("\n--- Extracted Product Data ---")
print(df)


# ==========================================
# STEP 3: ANALYZE PRICES USING PANDAS
# ==========================================

print("\n--- Price Analysis ---")

print("Average Price:",
      df["Price"].mean())

print("Highest Price:",
      df["Price"].max())

print("Lowest Price:",
      df["Price"].min())


# Find cheapest product
cheapest = df.loc[df["Price"].idxmin()]

print("\nCheapest Product:")
print(cheapest["Product"])
print("Price:", cheapest["Price"])


# Products currently available
print("\nProducts In Stock:")

print(
    df[df["Availability"] == "In Stock"]
)


# ==========================================
# STEP 4: STORE DATA IN SQLITE DATABASE
# ==========================================

connection = sqlite3.connect("price_monitor.db")

df.to_sql(
    "products",
    connection,
    if_exists="replace",
    index=False
)

print("\nData successfully stored in database.")


# ==========================================
# STEP 5: READ DATA FROM DATABASE
# ==========================================

database_data = pd.read_sql(
    "SELECT * FROM products",
    connection
)

print("\n--- Data Retrieved from Database ---")
print(database_data)

connection.close()


# ==========================================
# STEP 6: CREATE DASHBOARD / VISUALIZATION
# ==========================================

plt.figure(figsize=(8, 5))

plt.bar(
    df["Product"],
    df["Price"]
)

plt.xlabel("Product")
plt.ylabel("Price (₹)")
plt.title("Competitor Product Price Monitoring")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()
plt.show()


# ==========================================
# STEP 7: BUSINESS DECISION
# ==========================================

print("\n--- Business Decision ---")

average_price = df["Price"].mean()

if average_price > 55000:
    print(
        "Competitor average price is high."
    )
    print(
        "Business can consider competitive pricing."
    )
else:
    print(
        "Competitor average price is relatively low."
    )
    print(
        "Business should review its pricing strategy."
    )

