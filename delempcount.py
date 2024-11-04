def delEmpById(p_collection_name, p_employee_id):
    url = f"http://localhost:8989/solr/{p_collection_name}/update?commit=true"
    headers = {"Content-Type": "text/xml"}
    data = f"<delete><id>{p_employee_id}</id></delete>"
    response = requests.post(url, data=data, headers=headers)
    
    if response.status_code == 200:
        print(f"Employee ID '{p_employee_id}' deleted from '{p_collection_name}'.")
    else:
        print("Error deleting employee:", response.json())
