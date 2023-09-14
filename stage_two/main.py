import os
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Check if the database file exists; if not, create it
if not os.path.isfile('database.db'):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create a persons table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
else:
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

@app.route('/api', methods=['POST'])
def create_person():
    data = request.json

    if not data:
        return jsonify({"error": "Invalid request data"}), 400

    # Ensure that the request contains necessary data (e.g., 'name', 'age', 'email')
    required_fields = ['name', 'age', 'email']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # Insert a new person into the database
    cursor.execute('''
        INSERT INTO persons (name, age, email)
        VALUES (?, ?, ?)
    ''', (data["name"], data["age"], data["email"]))
    conn.commit()

    return jsonify({"message": "Person created successfully"}), 201

@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    cursor.execute('SELECT * FROM persons WHERE id = ?', (user_id,))
    person = cursor.fetchone()

    if person is None:
        return jsonify({"error": "Person not found"}), 404

    person_info = {
        "id": person[0],
        "name": person[1],
        "age": person[2],
        "email": person[3]
    }

    return jsonify(person_info)

@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    data = request.json

    if not data:
        return jsonify({"error": "Invalid request data"}), 400

    cursor.execute('SELECT * FROM persons WHERE id = ?', (user_id,))
    person = cursor.fetchone()

    if person is None:
        return jsonify({"error": "Person not found"}), 404

    # Update the person's details in the database
    cursor.execute('''
        UPDATE persons
        SET name = ?, age = ?, email = ?
        WHERE id = ?
    ''', (data["name"], data["age"], data["email"], user_id))
    conn.commit()

    return jsonify({"message": "Person updated successfully"}), 200

@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    cursor.execute('SELECT * FROM persons WHERE id = ?', (user_id,))
    person = cursor.fetchone()

    if person is None:
        return jsonify({"error": "Person not found"}), 404

    # Delete the person from the database
    cursor.execute('DELETE FROM persons WHERE id = ?', (user_id,))
    conn.commit()

    return jsonify({"message": "Person deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
