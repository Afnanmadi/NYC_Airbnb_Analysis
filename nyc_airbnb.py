
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
file_path = "C:\\Users\\user\\PycharmProjects\\PythonProject\\Assignments\\AssignmentsData5\\Finle Project\\AB_NYC_2019 (1).csv"
df = pd.read_csv(file_path)

# Data Cleaning
# Handling missing values
df = df.assign(
    name=df['name'].fillna("Unknown"),
    host_name=df['host_name'].fillna("Unknown"),
    reviews_per_month=df['reviews_per_month'].fillna(0),
    last_review=pd.to_datetime(df['last_review'])
)

# Removing outliers using IQR
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

columns_to_clean = ['price', 'minimum_nights', 'reviews_per_month']
df_cleaned = df.copy()
for col in columns_to_clean:
    df_cleaned = remove_outliers(df_cleaned, col)

# Exploratory Data Analysis
# Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(df_cleaned[['number_of_reviews', 'price', 'availability_365', 'reviews_per_month']].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Scatter Plots
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df_cleaned['number_of_reviews'], y=df_cleaned['price'], alpha=0.5)
plt.title('Number of Reviews vs Price')
plt.xlabel('Number of Reviews')
plt.ylabel('Price')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df_cleaned['number_of_reviews'], y=df_cleaned['availability_365'], alpha=0.5)
plt.title('Number of Reviews vs Availability')
plt.xlabel('Number of Reviews')
plt.ylabel('Availability (days/year)')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x=df_cleaned['room_type'], y=df_cleaned['number_of_reviews'])
plt.title("Number of Reviews by Room Type")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x=df_cleaned['neighbourhood_group'], y=df_cleaned['number_of_reviews'])
plt.title("Number of Reviews by Neighborhood Group")
plt.xticks(rotation=45)
plt.show()

# Machine Learning Model
# Selecting features and target variable
features = ['price', 'availability_365', 'reviews_per_month', 'calculated_host_listings_count']
X = df_cleaned[features]
y = df_cleaned['number_of_reviews']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print model evaluation metrics
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")
