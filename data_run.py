from datetime import datetime, timedelta
import random
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Replace <password> with your actual MongoDB Atlas password
uri = "mongodb+srv://anujd0009:okneha123@cluster0.og6bmfv.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the 'workload_data' database
db = client['workload_data']
workload_data = db['workload_data']

# Define the schema or fields for your documents
# Note: MongoDB is schema-less, so this step is optional, but it can be helpful for documentation.
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
    'performance_metrics': float,
    'market_demand': float,
    'resource_constraints': float
}

# Insert the schema into the collection (optional step)
workload_data.insert_one(schema)

# Function to generate random datetime within a range
def random_date(start_date, end_date):
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )

# Number of data points
num_data_points = 100

# Base date for last_period_date
base_date = datetime.strptime("2023-11-05", "%Y-%m-%d")

# Generate data for updating time, given time limit, labor force availability, workload, and additional features
data = []

for _ in range(num_data_points):
    update_time = random.uniform(1, 60)  # Random updating time between 1 and 60 minutes
    given_time_limit = random.uniform(30, 180)  # Random time limit between 30 and 180 minutes
    labor_force_availability = random.randint(5, 20)  # Random labor force between 5 and 20 workers
    workload = random.uniform(1, 100)  # Random workload between 1 and 100
    task_complexity = random.uniform(1, 10)  # Random task complexity between 1 and 10
    historical_workload_data = random.uniform(1, 100)  # Random historical workload data between 1 and 100
    seasonal_trends = random.uniform(1, 10)  # Random seasonal trends between 1 and 10
    workload_priority = random.randint(1, 3)  # Random workload priority (1, 2, or 3)
    time_of_day_week = random.randint(1, 7)  # Random time of day/week (1 to 7)
    lead_time = random.uniform(1, 30)  # Random lead time between 1 and 30 days
    performance_metrics = random.uniform(1, 10)  # Random performance metrics between 1 and 10
    market_demand = random.uniform(1, 10)  # Random market demand between 1 and 10
    resource_constraints = random.uniform(1, 10)  # Random resource constraints between 1 and 10

    data.append({
        'update_time': update_time,
        'given_time_limit': given_time_limit,
        'labor_force_availability': labor_force_availability,
        'workload': workload,
        'task_complexity': task_complexity,
        'historical_workload_data': historical_workload_data,
        'seasonal_trends': seasonal_trends,
        'workload_priority': workload_priority,
        'time_of_day_week': time_of_day_week,
        'lead_time': lead_time,
        'performance_metrics': performance_metrics,
        'market_demand': market_demand,
        'resource_constraints': resource_constraints
    })

# Insert the data into the collection
result = workload_data.insert_many(data)

print(f"Inserted {len(result.inserted_ids)} documents")
