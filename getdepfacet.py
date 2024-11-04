def getDepFacet(p_collection_name):
    url = f"http://localhost:8989/solr/{p_collection_name}/select?q=*:*&facet=true&facet.field=Department"
    response = requests.get(url)
    if response.status_code == 200:
        facets = response.json()['facet_counts']['facet_fields']['Department']
        print("Department Facet Count:", facets)
    else:
        print("Error getting department facet:", response.json())
