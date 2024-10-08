import pandas as pd

# Load the CSV file
df = pd.read_csv("BMS_DIFFERENTIAL_2024-10-01.csv")

# Example: Keep rows where 'ID' is in the list of selected IDs
selected_ids = ['123404']  # List of IDs to keep
filtered_df = df[df['EMP_SER_NUM'].isin(selected_ids)]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv("BMS_DIFFERENTIAL_2024-10-01_c.csv", index=False)
