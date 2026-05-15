python
import pandas as pd
import plotly.express as px

# Load CSV dataset
data = pd.read_csv("License_Category.csv")

# Data Preprocessing
data['License Type'] = data['License Type'].str.strip()
data['Category'] = data['Category'].str.strip()

# Basic Visualization: Bar Chart by License Type
fig = px.bar(data, x='License Type', y='Number of Licenses', color='Category',
             title="Distribution of Licenses in the Energy Sector",
             labels={'License Type': 'Type of License', 'Number of Licenses': 'Count'})

# Show the plot
fig.show()

# Advanced Analysis: Filter Licenses based on Type
def filter_licenses(license_type):
    filtered_data = data[data['License Type'] == license_type]
    return filtered_data

# Example usage
selected_licenses = filter_licenses("Electricity Generation")
print(selected_licenses)

# Save filtered data to a new CSV
selected_licenses.to_csv("Filtered_Licenses.csv", index=False)
