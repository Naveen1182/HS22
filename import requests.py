import requests

def createCollection(p_collection_name):
    url = f"http://localhost:8989/solr/admin/collections?action=CREATE&name={p_collection_name}&numShards=1&replicationFactor=1"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Collection '{p_collection_name}' created successfully.")
    else:
        print("Error creating collection:", response.json())
