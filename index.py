

import csv

with open("C:/Users/marri/Downloads/SuperMarket Analysis.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


#importing the pandas library to read the CSV file and perform data analysis
import pandas as pd

df = pd.read_csv("C:/Users/marri/Downloads/SuperMarket Analysis.csv")

print(df)


import pandas as pd

df = pd.read_csv("C:/Users/marri/Downloads/SuperMarket Analysis.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

# Checking for null values and duplicates in the dataset

print(df.isnull().sum())

#checking for duplicates in the dataset
print(df.duplicated().sum())

# Dropping duplicates from the dataset
print(df.drop_duplicates(inplace=True))

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print(df.columns)



df["product_line"] = df["product_line"].str.strip()
df["product_line"] = df["product_line"].str.title()



print("Duplicates before cleaning:")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Duplicates after cleaning:")
print(df.duplicated().sum())



print("\n--- DATA TYPES BEFORE CLEANING ---")
print(df.dtypes)


# Convert numeric columns
numeric_columns = [
    "unit_price",
    "quantity",
    "tax_5%",
    "sales",
    "cogs",
    "gross_margin_percentage",
    "gross_income",
    "rating"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


print("\n--- DATA TYPES AFTER CLEANING ---")
print(df.dtypes)



print(df)


df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

print("\n--- DATA TYPES AFTER CLEANING ---")
print(df.dtypes)


#Clean ALL important text columns

text_columns = [
    "branch",
    "city",
    "customer_type",
    "gender",
    "product_line",
    "payment"
]

for column in text_columns:
    df[column] = df[column].str.strip()

#checking for null values and duplicates in the dataset after cleaning

print(df)


# Checking for invalid quantity values (less than or equal to 0)
print("\n--- INVALID QUANTITY ---")
print(df[df["quantity"] <= 0])

# Checking for invalid unit_price values (less than or equal to 0)
print("\n--- RATING RANGE ---")
print(df["rating"].min())
print(df["rating"].max())


# Checking for invalid rating values (less than 0 or greater than 10)
print(df[
    (df["rating"] < 0) |
    (df["rating"] > 10)
])


#Check unique categorical values
print("\n--- BRANCH VALUES ---")
print(df["branch"].unique())

print("\n--- CITY VALUES ---")
print(df["city"].unique())

print("\n--- CUSTOMER TYPES ---")
print(df["customer_type"].unique())

print("\n--- GENDER VALUES ---")
print(df["gender"].unique())

print("\n--- PRODUCT LINES ---")
print(df["product_line"].unique())

print("\n--- PAYMENT METHODS ---")
print(df["payment"].unique())


#Create a calculated column

df["calculated_cogs"] = (
    df["unit_price"] * df["quantity"]
)


print(df["calculated_cogs"])


print("\n--- CALCULATED COGS ---")
print(
    df[
        ["unit_price", "quantity", "calculated_cogs"]
    ].head()
)


#Validate your calculation
df["cogs_difference"] = (
    df["calculated_cogs"] - df["cogs"]
).abs()


print("\n--- COGS VALIDATION ---")
print(df[
    [
        "cogs",
        "calculated_cogs",
        "cogs_difference"
    ]
].head())


df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["day_name"] = df["date"].dt.day_name()


print(
    df[
        ["date", "year", "month", "day", "day_name"]
    ].head()
)


#Analyze the cleaned data

#total sales
print("\n--- TOTAL SALES ---")
print(df["sales"].sum())

#average sales
print("\n--- AVERAGE SALES ---")
print(df["sales"].mean())

#average rating
print("\n--- AVERAGE RATING ---")
print(df["rating"].mean())


#Sales by product line

sales_by_product = (
    df.groupby("product_line")["sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n--- SALES BY PRODUCT LINE ---")
print(sales_by_product)


#Sales by city

sales_by_city = (
    df.groupby("city")["sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n--- SALES BY CITY ---")
print(sales_by_city)


#Sales by payment method

sales_by_payment = (
    df.groupby("payment")["sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n--- SALES BY PAYMENT METHOD ---")
print(sales_by_payment)


#Average rating by product line
rating_by_product = (
    df.groupby("product_line")["rating"]
      .mean()
      .sort_values(ascending=False)
)

print("\n--- AVERAGE RATING BY PRODUCT ---")
print(rating_by_product)

#Average rating by city
print("\n========== FINAL VALIDATION ==========")

print("Rows:", len(df))

print("Columns:", len(df.columns))

print(
    "Missing values:",
    df.isnull().sum().sum()
)

print(
    "Duplicates:",
    df.duplicated().sum()
)

print(
    "Duplicate Invoice IDs:",
    df["invoice_id"].duplicated().sum()
)

print("======================================")



#Save the cleaned dataset

output_file = (
    "C:/Users/marri/Downloads/"
    "SuperMarket_Cleaned.csv"
)

df.to_csv(
    output_file,
    index=False
)

print("\nCleaned CSV saved successfully!")
print(output_file)


