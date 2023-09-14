import requests

base_url = 'http://apampaabdulrasheed16.pythonanywhere.com/'  # Change this if your Flask app is running on a different address or port

# Function to send a GET request to retrieve a user by ID
def get_user(user_id):
    response = requests.get(f'{base_url}/api/{user_id}')
    return response

# Function to send a POST request to create a new user
def create_user(user_id, name, age):
    data = {
        'name': name,
        'age': age
    }
    response = requests.post(f'{base_url}/api/{user_id}', json=data)
    return response

# Function to send a PATCH request to update an existing user
def update_user(user_id, name=None, age=None):
    data = {}
    if name is not None:
        data['name'] = name
    if age is not None:
        data['age'] = age
    response = requests.patch(f'{base_url}/api/{user_id}', json=data)
    return response

# Function to send a DELETE request to delete a user by ID
def delete_user(user_id):
    response = requests.delete(f'{base_url}/api/{user_id}')
    return response

# Test cases
if __name__ == '__main__':
    # Create a new user
    create_response = create_user('1', 'John', 30)
    print(create_response.status_code)  # Expecting 201 for created

    # Retrieve the created user
    get_response = get_user('1')
    print(get_response.status_code)  # Expecting 200 for success
    print(get_response.json())

    # Update the user's age
    update_response = update_user('1', age=31)
    print(update_response.status_code)  # Expecting 200 for success
    print(update_response.json())

    # Delete the user
    delete_response = delete_user('1')
    print(delete_response.status_code)  # Expecting 204 for no content
