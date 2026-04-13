import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import json

# Load dataset (FIXED LINE)
df = pd.read_csv("data/winequality.csv", sep=';')

# Features & target
X = df.drop("quality", axis=1)
y = df["quality"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("R2:", r2)

# Save model
joblib.dump(model, "model.pkl")

# Save metrics
metrics = {"mse": mse, "r2": r2}
with open("metrics.json", "w") as f:
    json.dump(metrics, f)
print("Auto trigger working")