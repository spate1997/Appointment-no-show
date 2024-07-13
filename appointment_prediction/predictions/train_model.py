import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load your dataset
data = pd.read_csv('path_to_dataset.csv')

# Preprocess your data
# Example: data preprocessing steps (cleaning, encoding, etc.)
data['ScheduledDay'] = pd.to_datetime(data['ScheduledDay'])
data['AppointmentDay'] = pd.to_datetime(data['AppointmentDay'])
data['DaysBetween'] = (data['AppointmentDay'] - data['ScheduledDay']).dt.days
data['Gender'] = data['Gender'].map({'F': 0, 'M': 1})

# Select features and target
features = data[['Gender', 'Age', 'DaysBetween']]
target = data['No-show'].map({'No': 0, 'Yes': 1})

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

# Save the model
joblib.dump(model, 'appointment_model.pkl')
