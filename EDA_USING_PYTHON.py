import pandas as pd

df = pd.read_csv(r"C:\Users\Mayank Bisht\Documents\Data analyst Projects\EDA_Dataset_Messyone.csv",
                 low_memory=False)

df_clean = df.copy()

# ---------------------------------------------------------------------------------------------------

# DATA CLEANING

# Cleaning Process for 'User_ID' column

print("Before cleaning:")
print(df_clean.shape)
print(df_clean['User_ID'].isnull().sum())
print(df_clean['User_ID'].dtype)

# Drop rows where 'User_ID' is null and convert the column to integer type

df_clean = df_clean.dropna(subset=['User_ID'])
df_clean['User_ID'] = df_clean['User_ID'].astype('int64')

print("\nAfter cleaning:")
print(df_clean.shape)
print(df_clean['User_ID'].isnull().sum())
print(df_clean['User_ID'].dtype)



# Cleaning Process for 'Country' column

# Check unique values and frequency

print("\nUnique values in 'Country' column:")
print(df_clean['Country'].value_counts())

# 
df_clean['Country'].unique()
df_clean['Country'].value_counts(dropna=False)

# Fill missing values with 'Unknown'
df_clean['Country'] = df_clean['Country'].fillna('Unknown')

# Convert to lowercase and remove extra spaces
df_clean['Country'] = df_clean['Country'].str.lower().str.strip()

# Merge inconsistent country names
df_clean['Country'] = df_clean['Country'].replace({
    'ind': 'india',
    'uk': 'uk',      # already fine, just for clarity
    'usa': 'usa'
})

print("\nAfter cleaning 'Country' column:")
print(df_clean['Country'].value_counts())


# Cleaning Process for 'Device_Type' column

print("\nUnique values in 'Device_Type' column:")
print(df_clean['Device_Type'].unique())
print("\nValue counts in 'Device_Type' column:")
print(df_clean['Device_Type'].value_counts(dropna=False))

# Fill missing with 'Unknown'
df_clean['Device_Type'] = df_clean['Device_Type'].fillna('Unknown')

# Standardize text by converting to lowercase and stripping extra spaces
df_clean['Device_Type'] = df_clean['Device_Type'].str.lower().str.strip()

print("\nAfter cleaning 'Device_Type' column:")
print(df_clean['Device_Type'].value_counts())


# Cleaning Process for 'Traffic_Source' column

print("\nUnique values in 'Traffic_Source' column:")
print(df_clean['Traffic_Source'].unique())
print("\nValue counts in 'Traffic_Source' column:")
print(df_clean['Traffic_Source'].value_counts(dropna=False))

# Handle missing values by filling with 'Unknown'
df_clean['Traffic_Source'] = df_clean['Traffic_Source'].fillna('Unknown')

# Standardize text by converting to lowercase and stripping extra spaces
df_clean['Traffic_Source'] = df_clean['Traffic_Source'].str.lower().str.strip()

print("\nAfter cleaning 'Traffic_Source' column:")
print(df_clean['Traffic_Source'].value_counts())


# Cleaning process for 'Time_Spent_Minutes column

print("\nBefore cleaning 'Time_Spent_Minutes' column:")
print(df_clean['Time_Spent_Minutes'].describe())
print("\nUnique values in 'Time_Spent_Minutes' column:")
print(df_clean['Time_Spent_Minutes'].unique())

# Fill missing values with median (robust to outliers)
df_clean['Time_Spent_Minutes'] = df_clean['Time_Spent_Minutes'].fillna(
    df_clean['Time_Spent_Minutes'].median()
)

Q1 = df_clean['Time_Spent_Minutes'].quantile(0.25)
Q3 = df_clean['Time_Spent_Minutes'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_clean = df_clean[
    (df_clean['Time_Spent_Minutes'] >= lower_bound) &
    (df_clean['Time_Spent_Minutes'] <= upper_bound)
]

print("\nAfter cleaning 'Time_Spent_Minutes' column:")
print(df_clean['Time_Spent_Minutes'].describe())
print("\nUnique values in 'Time_Spent_Minutes' column after cleaning:")
print(df_clean['Time_Spent_Minutes'].unique())


# Cleaning process for 'Page_Views' column

print("\nBefore cleaning 'Pages_Viewed' column:")
print(df_clean['Pages_Viewed'].describe())
print("\nUnique values in 'Pages_Viewed' column:")
print(df_clean['Pages_Viewed'].unique())

# Fill missing with median
df_clean['Pages_Viewed'] = df_clean['Pages_Viewed'].fillna(
    df_clean['Pages_Viewed'].median()
)

print("\nAfter cleaning 'Pages_Viewed' column:")
print(df_clean['Pages_Viewed'].describe())
print("\nUnique values in 'Pages_Viewed' column after cleaning:")
print(df_clean['Pages_Viewed'].unique())



# Cleaning process for 'Added_to_Cart' column

print("\nBefore cleaning 'Added_to_Cart' column:")
print(df_clean['Added_to_Cart'].describe())
print("\nUnique values in 'Added_to_Cart' column:")
print(df_clean['Added_to_Cart'].unique())

# Fill missing values with most frequent value (mode)
df_clean['Added_to_Cart'] = df_clean['Added_to_Cart'].fillna(
    df_clean['Added_to_Cart'].mode()[0]
)

# Convert to integer type
df_clean['Added_to_Cart'] = df_clean['Added_to_Cart'].astype('int64')

print("\nAfter cleaning 'Added_to_Cart' column:")
print(df_clean['Added_to_Cart'].describe())
print("\nUnique values in 'Added_to_Cart' column after cleaning:")
print(df_clean['Added_to_Cart'].unique())



# Cleaning column 'Purchased'

print("\nBefore cleaning 'Purchased' column:")
print(df_clean['Purchased'].describe())
print("\nUnique values in 'Purchased' column:")
print(df_clean['Purchased'].unique())

print("\nValue counts in 'Purchased' column before cleaning:")
print(df_clean['Purchased'].value_counts(dropna=False))
print("\nNumber of missing values in 'Purchased' column:")
print(df_clean['Purchased'].isnull().sum())

print("\nRows where 'Added_to_Cart' is 0 and 'Purchased' is 1:")
print(df_clean[(df_clean['Added_to_Cart'] == 0) & (df_clean['Purchased'] == 1)])

# Handling missing values in 'Purchased' column by using mode (most frequent value)

df_clean['Purchased'] = df_clean['Purchased'].fillna(
    df_clean['Purchased'].mode()[0]
)

# Convert 'Purchased' to integer type
df_clean['Purchased'] = df_clean['Purchased'].astype(int)

# fixing logical inconsistency: if 'Added_to_Cart' is 0, then 'Purchased' cannot be 1. Set 'Purchased' to 0 in those cases.
df_clean.loc[
    (df_clean['Added_to_Cart'] == 0) & (df_clean['Purchased'] == 1),
    'Purchased'
] = 0

print("\nAfter cleaning 'Purchased' column:")
print(df_clean['Purchased'].describe())
print("\nUnique values in 'Purchased' column after cleaning:")
print(df_clean['Purchased'].unique())



# Cleaning column 'Price'

print("\nBefore cleaning 'Price' column:")
print(df_clean['Price'].describe())
print("\nUnique values in 'Price' column:")
print(df_clean['Price'].unique())
print("\nNumber of missing values in 'Price' column:")
print(df_clean['Price'].isnull().sum())

# Fill missing values with median
df_clean['Price'] = df_clean['Price'].fillna(
    df_clean['Price'].median()
)

Q1 = df_clean['Price'].quantile(0.25)
Q3 = df_clean['Price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_clean = df_clean[
    (df_clean['Price'] >= lower_bound) &
    (df_clean['Price'] <= upper_bound)
]

print("\nAfter cleaning 'Price' column:")
print(df_clean['Price'].describe())
print("\nUnique values in 'Price' column after cleaning:")
print(df_clean['Price'].unique())
print("\nNumber of missing values in 'Price' column after cleaning:")
print(df_clean['Price'].isnull().sum())

df_clean.info()

# --------------------------------------------------------------------------------------------- 


# EXPLORATORY DATA ANALYSIS (EDA)

#1. Overall statistics 

print("\nOverall statistics for numerical columns:")
print(df_clean.describe())

#2. Country Distribution

print("\nCountry distribution:")
print(df_clean['Country'].value_counts())

#3. Device Type Distribution

print("\nDevice Type distribution:")
print(df_clean['Device_Type'].value_counts())

#4. Traffic Source Distribution

print("\nTraffic Source distribution:")
print(df_clean['Traffic_Source'].value_counts())

#5. Time Spent Analysis

print("\nTime Spent (Minutes) analysis:")
print(df_clean['Time_Spent_Minutes'].value_counts())

#6. Pages Viewed Analysis

print("\nPages Viewed analysis:")
print(df_clean['Pages_Viewed'].value_counts())

#7. Cart v Purchase rate

print("\nCart vs Purchase Rate:")
print(df_clean[['Added_to_Cart', 'Purchased']].mean())

               
#8. Conversion Insight

print("\nCart vs Purchase rate:")
print(df_clean.groupby('Added_to_Cart')['Purchased'].mean())


#9. Price Distribution

print("\nPrice distribution:")
print(df_clean['Price'].describe())

#10. Revenue By Country

print("\nRevenue by Country:")
print(df_clean.groupby('Country')['Price'].sum().sort_values(ascending=False))

#11. Revenue By device type

print("\nRevenue by Device Type:")
print(df_clean.groupby('Device_Type')['Price'].sum().sort_values(ascending=False))

# -----------------------------------------------------------------------------------------------------


# DATA VISUALIZATION USING MATPLOTLIB

#1. Which countries bring the most users?

import matplotlib.pyplot as plt

df_clean['Country'].value_counts().plot(kind='bar')
plt.title("Users by Country")
plt.show()

#2. Device Usage distribution

df_clean['Device_Type'].value_counts().plot(kind='bar')
plt.title("Device Type Distribution")
plt.show()

#3. Traffic Soure Performance

df_clean['Traffic_Source'].value_counts().plot(kind='bar')
plt.title("Traffic Source Distribution")
plt.show()

#4. Time Spent Distribution

df_clean['Time_Spent_Minutes'].plot(kind='hist', bins=30)
plt.title("Time Spent Distribution")
plt.show()

#5. Pages Viewed Distribution

df_clean['Pages_Viewed'].plot(kind='hist', bins=30)
plt.title("Pages Viewed Distribution")
plt.show()

#6. Cart vs Purchase Rate

df_clean.groupby('Added_to_Cart')['Purchased'].mean().plot(kind='bar')
plt.title("Purchase Rate by Cart Status")
plt.show()

#7. Revenue By Country

df_clean.groupby('Country')['Price'].sum().sort_values(ascending=False).plot(kind='bar')
plt.title("Revenue by Country")
plt.show()

#8. Revenue By Device Type

df_clean.groupby('Device_Type')['Price'].sum().sort_values(ascending=False).plot(kind='bar')
plt.title("Revenue by Device Type")
plt.show()
