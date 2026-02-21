from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("large_sales_data.csv")
current_index = 0

@app.get("/stream")
def stream_data():
    global current_index
    
    if current_index >= len(df):
        current_index = 0
        
    record = df.iloc[current_index].to_dict()
    current_index += 1
    
    return record