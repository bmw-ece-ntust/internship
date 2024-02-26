import pandas as pd
class DataProcess:
    def __init__(self, filename):
        self.data = pd.read_csv(filename,sep=';')

    def preprocess(self):
        non_tag_cols=['rssi_D1_1F_AP01','rssi_D1_1F_AP02','rssi_D1_1F_AP03','rssi_D1_1F_AP04','rssi_D1_1F_AP05']
        melted = self.data.melt(id_vars=[col for col in self.data.columns if col not in non_tag_cols],\
            var_name="AP_Name",value_name="rssi")
        melted = melted.dropna(subset=["rssi"])
        # Reset the index of the DataFrame
        melted.reset_index(drop=True, inplace=True)
        self.data = melted
        
    def to_list(self):
        return self.data.values.tolist()
    
    def to_dict(self):
        return self.data.to_dict('records')
    
    def to_dataframe(self):
        df = self.data
        return df