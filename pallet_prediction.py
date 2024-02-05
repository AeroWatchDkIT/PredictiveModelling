import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Generate sample data
np.random.seed(42)
num_samples = 1000

data = {
    'Weight': np.random.choice(['heavy', 'light'], size=num_samples),
    'Aisle': np.random.choice(['1', '2', '3', '4'], size=num_samples),
    'Row': np.random.choice(['1', '2', '3'], size=num_samples),
    'Column': np.random.choice(['1', '2', '3'], size=num_samples),
    'Distance_from_Entry': np.random.randint(10, 100, size=num_samples),
    'Time_of_Day': np.random.choice(['morning', 'afternoon', 'night'], size=num_samples),
    'Day_of_Week': np.random.choice(['weekday', 'weekend'], size=num_samples),
    'Congestion': np.random.choice(['low', 'medium', 'high'], size=num_samples),
    'Previous_Retrieval_Time': np.random.randint(10, 30, size=num_samples),
    'Temperature': np.random.choice(['normal', 'cold', 'hot'], size=num_samples),
    'Automation_Level': np.random.choice(['low', 'medium', 'high'], size=num_samples),
}

