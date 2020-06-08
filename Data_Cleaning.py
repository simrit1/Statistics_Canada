import pandas as pd

df = pd.read_csv('Copy of Electric_Vehicle_Population_Data.csv')

train = df[df['Base MSRP']!=0]
test = df[df['Base MSRP']==0]

X_train = train[['Model Year', 'Make', 'Model', 'Electric Vehicle Type', 'Clean Alternative Fuel Vehicle (CAFV) Eligibility', 'Electric Range']]
X_test = test[['Model Year', 'Make', 'Model', 'Electric Vehicle Type', 'Clean Alternative Fuel Vehicle (CAFV) Eligibility', 'Electric Range']]

y_train = train[['Base MSRP']]

from sklearn.preprocessing import LabelEncoder
