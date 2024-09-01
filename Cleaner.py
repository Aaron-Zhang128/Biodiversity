import pandas as pd

dataCO2 = pd.read_csv("/Users/aaronz/Desktop/Big Data/CleanedCO2.csv")

# regions = ["Africa", "Europe", "Asia", "North America", "South America", "Oceana", "World"]
regions = ["North America"]

# Create a boolean mask for the specified conditions
mask = (dataCO2["Year"] > 2007) &  (dataCO2["Year"] < 2019) &(dataCO2["Entity"].isin(regions))

# Apply the mask to filter the DataFrame
filtered_data = dataCO2[mask]

# Save the filtered data to a new CSV file
filtered_data.to_csv("Fortnite", index=False)

# Print information about the filtered data
print("Filtered data saved to Forge.csv")


import pandas as pd

# # df = pd.read("merged_file.csv")

# # for i in range()

# # Read the CSV files into dataframes
# df1 = pd.read_csv("World.csv")
# df2 = pd.read_csv("World2.csv")

# # Merge the two dataframes on "Entity" and "Year"
# merged_df = pd.merge(df1, df2, on=['Entity', 'Year'], how='outer')

# # Save the merged dataframe to a new CSV file
# merged_df.to_csv("finalWorld.csv", index=False)

# # Print the merged dataframe
# print(merged_df)







import pandas as pd

# Read your CSV file into a dataframe
data = pd.read_csv("northamerica.csv")

# Replace "your_column" with the actual column name for which you want to calculate the delta
column_name = "Annual CO₂ emissions "

# Calculate the delta and create a new column with the result
data['Delta_' + column_name] = data[column_name].diff()

# Save the updated dataframe to a new CSV file
data.to_csv("Lnorthamerica.csv", index=False)

# Print the updated dataframe
print(data)