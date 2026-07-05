import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("Nike_Sales_Uncleaned.csv")

print("Original Shape:", df.shape)

# -----------------------------
# Remove Duplicate Rows
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Handle Missing Values
# -----------------------------

# Fill missing Size with "Unknown"
df["Size"] = df["Size"].fillna("Unknown")

# Fill numerical columns with median
df["Units_Sold"] = df["Units_Sold"].fillna(df["Units_Sold"].median())
df["MRP"] = df["MRP"].fillna(df["MRP"].median())
df["Discount_Applied"] = df["Discount_Applied"].fillna(df["Discount_Applied"].median())

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Fill missing dates with the most common date
df["Order_Date"] = df["Order_Date"].fillna(df["Order_Date"].mode()[0])

# -----------------------------
# Remove Extra Spaces
# -----------------------------
text_columns = [
    "Gender_Category",
    "Product_Line",
    "Product_Name",
    "Sales_Channel",
    "Region"
]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# -----------------------------
# Standardize Text
# -----------------------------
df["Gender_Category"] = df["Gender_Category"].str.title()
df["Product_Line"] = df["Product_Line"].str.title()
df["Product_Name"] = df["Product_Name"].str.title()
df["Sales_Channel"] = df["Sales_Channel"].str.title()
df["Region"] = df["Region"].str.title()

# -----------------------------
# Convert Numeric Columns
# -----------------------------
numeric_columns = [
    "Units_Sold",
    "MRP",
    "Discount_Applied",
    "Revenue",
    "Profit"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# Remove Remaining Missing Values
# -----------------------------
df = df.dropna()

# -----------------------------
# Reset Index
# -----------------------------
df = df.reset_index(drop=True)
# -----------------------------
# Format Date
# -----------------------------
df["Order_Date"] = df["Order_Date"].dt.strftime("%Y-%m-%d")

# -----------------------------
# Round Numeric Columns
# -----------------------------
numeric_columns = [
    "Units_Sold",
    "MRP",
    "Discount_Applied",
    "Revenue",
    "Profit"
]

df[numeric_columns] = df[numeric_columns].round(2)

# -----------------------------
# -----------------------------
# Sort Dataset by Order Date
# -----------------------------
df = df.sort_values(by="Order_Date")

# Reset index after sorting
df = df.reset_index(drop=True)

# -----------------------------
# Save Clean Dataset
# -----------------------------
df.to_csv("Nike_Sales_Cleaned.csv", index=False, encoding="utf-8")
print("Cleaning Completed Successfully!")
print("Final Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst 5 Rows:")
print(df.head())