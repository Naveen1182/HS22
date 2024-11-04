import pandas as pd
import json

def indexData(p_collection_name, p_exclude_column):
    data = pd.read_csv("employee_data.csv")
    data = data.drop(columns=[p_exclude_column])
    json_data = data.to_dict(orient="records")
    
    url = f"http://localhost:8989/solr/{p_collection_name}/update?commit=true"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(json_data), headers=headers)
    
    if response.status_code == 200:
        print(f"Data indexed into '{p_collection_name}' excluding column '{p_exclude_column}'.")
    else:
        print("Error indexing data:", response.json())
