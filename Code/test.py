import pandas as pd

# Load the data files
ues_data_path = 'ues-2024-07-16-083100-qfnriic8.csv'
cells_data_path = 'cells-2024-07-16-083043-teg2vaqy.csv'

ues_data = pd.read_csv(ues_data_path)
cells_data = pd.read_csv(cells_data_path)

# Display the first few rows of each dataset
ues_data.head(), cells_data.head()