def searchByColumn(p_collection_name, p_column_name, p_column_value):
    url = f"http://localhost:8989/solr/{p_collection_name}/select?q={p_column_name}:{p_column_value}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Search Results:", response.json()['response']['docs'])
    else:
        print("Error in search:", response.json())
