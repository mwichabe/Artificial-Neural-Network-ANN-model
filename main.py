import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# load the data
data = pd.read_csv("248.csv")

# Drop unnecessary columns (if any)
data = data.drop(["index", "最后一个基本个案"], axis=1)
# Split features (input) and target (output)
X = data.drop("totalseconds", axis=1)
y = data["totalseconds"]
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Building the ANN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    tf.keras.layers.Dense(units=32, activation='relu'),
    tf.keras.layers.Dense(units=1)  # Output layer
])
model.compile(optimizer='adam', loss='mean_squared_error')
# Training the model
model.fit(X_train_scaled, y_train, epochs=100, batch_size=32, verbose=1)
# Evaluate the model
loss = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Mean Squared Error on Test Set: {loss:.2f}")


