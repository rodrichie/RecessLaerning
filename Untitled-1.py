# %%
import pandas as pd
df = pd.DataFrame()
print(df)

# %%
data = {
    'Name': ['John', 'Alice', 'Bob', 'Emily', 'Michael'],
    'Age': [25, 30, 35, 28, 32],
    'Country': ['USA', 'Canada', 'UK', 'USA', 'Australia'],
    'Salary': [50000, 60000, 70000, 55000, 65000]
}

df1 = pd.DataFrame(data)
print(df1)

# %%
#accessing individual items
names = data["Name"]
age= data["Age"]
country = data["Country"]
salary= data["Salary"]

print(names,age,country,salary)

# %%
# Create data using pd.Series
names = pd.Series(['John', 'Alice', 'Bob', 'Emily', 'Michael'])
ages = pd.Series([25, 30, 35, 28, 32])
countries = pd.Series(['USA', 'Canada', 'UK', 'USA', 'Australia'])
salaries = pd.Series([50000, 60000, 70000, 55000, 65000])

# Create a dictionary of series
data = {
    'Name': names,
    'Age': ages,
    'Country': countries,
    'Salary': salaries
}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the dataset
print(df)


# %%
import pandas as pd

# Create a pandas DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Emily', 'Michael'],
    'Age': [25, 30, 35, 28, 32],
    'Country': ['USA', 'Canada', 'UK', 'USA', 'Australia'],
    'Salary': [50000, 60000, 70000, 55000, 65000]
}
df = pd.DataFrame(data)

# Convert DataFrame columns into Series using pd.Series()
names = pd.Series(df['Name'])
ages = pd.Series(df['Age'])
countries = pd.Series(df['Country'])
salaries = pd.Series(df['Salary'])

# Print the individual Series
print("Names:")
print(names)
print()

print("Ages:")
print(ages)
print()

print("Countries:")
print(countries)
print()

print("Salaries:")
print(salaries)


# %%
import pandas as pd

# Create a dictionary of days and dates
data = {
    'Monday': '2023-07-03',
    'Tuesday': '2023-07-04',
    'Wednesday': '2023-07-05',
    'Thursday': '2023-07-06',
    'Friday': '2023-07-07'
}

# Create a Pandas Series from the dictionary
series = pd.Series(data)

# Print the Pandas Series
print(series)




# %%
#selecting indexed days
selected_days = series[['Monday','Tuesday']]
print("Selected Days (Indexing):")
print(selected_days)

# %%
import seaborn as sns


# %%
import matplotlib.pyplot as pl


