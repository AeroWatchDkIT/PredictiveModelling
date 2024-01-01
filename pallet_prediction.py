import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
# Generating sample data for pallet retrieval
np.random.seed(42)
num_samples = 1000
data = {
    'Warehouse_Zone': np.random.choice(['A', 'B', 'C', 'D'], size=num_samples),
    'Timestamp': pd.date_range('2022-01-01', periods=num_samples, freq='H'),
    'Distance_meters': np.random.randint(20, 100, size=num_samples),
    'Items_on_Pallet': np.random.randint(5, 25, size=num_samples),
    'Retrieval_Time_minutes': np.random.randint(10, 30, size=num_samples)
}