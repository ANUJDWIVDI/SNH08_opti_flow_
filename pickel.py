import pandas as pd
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
import matplotlib.pyplot as plt
import pickle

# Connect to MongoDB
uri = "mongodb+srv://anujd0009:okneha123@cluster0.og6bmfv.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['workload_data']
workload_data = db['workload_data']

# Define the schema
schema = {
    'update_time': float,
    'given_time_limit': float,
    'labor_force_availability': int,
    'workload': float,
    'task_complexity': float,
    'historical_workload_data': float,
    'seasonal_trends': float,
    'workload_priority': int,
    'time_of_day_week': int,
    'lead_time': float,
    'market_demand': float,
    'resource_constraints': float
}

# Fetch data from MongoDB
data = list(workload_data.find())
df = pd.DataFrame(data)

# Regression Models
regression_features = ['update_time', 'given_time_limit', 'workload', 'task_complexity', 'historical_workload_data']
regression_target = 'lead_time'

X_reg = df[regression_features]
y_reg = df[regression_target]

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Linear Regression
reg_model_lr = LinearRegression()
reg_model_lr.fit(X_train_reg, y_train_reg)
reg_predictions_lr = reg_model_lr.predict(X_test_reg)
reg_mse_lr = mean_squared_error(y_test_reg, reg_predictions_lr)
print(f'Linear Regression Mean Squared Error: {reg_mse_lr}')

# Decision Tree Regressor
reg_model_dt = DecisionTreeRegressor()
reg_model_dt.fit(X_train_reg, y_train_reg)
reg_predictions_dt = reg_model_dt.predict(X_test_reg)
reg_mse_dt = mean_squared_error(y_test_reg, reg_predictions_dt)
print(f'Decision Tree Regression Mean Squared Error: {reg_mse_dt}')

# Random Forest Regressor
reg_model_rf = RandomForestRegressor()
reg_model_rf.fit(X_train_reg, y_train_reg)
reg_predictions_rf = reg_model_rf.predict(X_test_reg)
reg_mse_rf = mean_squared_error(y_test_reg, reg_predictions_rf)
print(f'Random Forest Regression Mean Squared Error: {reg_mse_rf}')

# Save the regression models to files
with open('regression_model_lr.pkl', 'wb') as reg_model_file:
    pickle.dump(reg_model_lr, reg_model_file)
with open('regression_model_dt.pkl', 'wb') as reg_model_file:
    pickle.dump(reg_model_dt, reg_model_file)
with open('regression_model_rf.pkl', 'wb') as reg_model_file:
    pickle.dump(reg_model_rf, reg_model_file)

# Classification Models
classification_features = ['labor_force_availability', 'workload', 'workload_priority', 'resource_constraints']
classification_target = 'time_of_day_week'

X_cls = df[classification_features]
y_cls = df[classification_target]

X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)

# Random Forest Classifier
cls_model_rf = RandomForestClassifier()
cls_model_rf.fit(X_train_cls, y_train_cls)
cls_predictions_rf = cls_model_rf.predict(X_test_cls)
cls_accuracy_rf = accuracy_score(y_test_cls, cls_predictions_rf)
print(f'Random Forest Classification Accuracy: {cls_accuracy_rf}')

# Save the classification model to a file
with open('classification_model_rf.pkl', 'wb') as cls_model_file:
    pickle.dump(cls_model_rf, cls_model_file)

# Plotting Regression Results
plt.scatter(X_test_reg['update_time'], y_test_reg, color='black', label='Actual')
plt.scatter(X_test_reg['update_time'], reg_predictions_lr, color='blue', label='Linear Regression')
plt.scatter(X_test_reg['update_time'], reg_predictions_dt, color='green', label='Decision Tree Regression')
plt.scatter(X_test_reg['update_time'], reg_predictions_rf, color='red', label='Random Forest Regression')
plt.xlabel('Update Time')
plt.ylabel('Lead Time')
plt.legend()
plt.title('Regression Results')
plt.show()
