def getEmpCount(p_collection_name):
    url = f"http://localhost:8989/solr/{p_collection_name}/select?q=*:*&rows=0"
    response = requests.get(url)
    if response.status_code == 200:
        count = response.json()['response']['numFound']
        print(f"Employee Count in '{p_collection_name}':", count)
    else:
        print("Error getting employee count:", response.json())
