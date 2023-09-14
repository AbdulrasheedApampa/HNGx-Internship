import requests

# Set the base URL for your API
base_url = 'http://apampaabdulrasheed16.pythonanywhere.com/'  # Change the URL if your API is hosted elsewhere

# Test data for creating a new person
new_person_data = {
    "name": "Rasheed Apampa",
    "age": 15,
    "email": "apampaabdulrasheed16@gmail.com"
}

# Function to send a POST request to create a new person
def create_person(data):
    response = requests.post(f"{base_url}/api", json=data)
    return response

# Function to send a GET request to retrieve a person by ID
def get_person(user_id):
    response = requests.get(f"{base_url}/api/{user_id}")
    return response

# Function to send a PUT request to update a person by ID
def update_person(user_id, data):
    response = requests.put(f"{base_url}/api/{user_id}", json=data)
    return response

# Function to send a DELETE request to delete a person by ID
def delete_person(user_id):
    response = requests.delete(f"{base_url}/api/{user_id}")
    return response

# Testing the API endpoints
if __name__ == '__main__':
    # Create a new person
    create_response = create_person(new_person_data)
    print("Create Response:")
    print(create_response.json())
    
    # Retrieve all persons to find the newly created person's ID
    get_all_response = requests.get(f"{base_url}/api")
    all_persons = get_all_response.json()
    created_person_id = len(all_persons) - 1  # Index of the newly created person
    
    if created_person_id >= 0:
        # Retrieve the newly created person by ID
        get_response = get_person(created_person_id)
        print("Get Response:")
        print(get_response.json())

        # Update the person's information
        updated_data = {
            "name": "Rasheed Apampa Updated",
            "age": 31,
            "email": "rasheedupdated@example.com"
        }
        update_response = update_person(created_person_id, updated_data)
        print("Update Response:")
        print(update_response.json())

        # Delete the person
        delete_response = delete_person(created_person_id)
        print("Delete Response:")
        print(delete_response.json())
    else:
        print("Error: Could not retrieve the newly created person's ID.")
