from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Database configuration
db_config = {
    'host': os.getenv('DB_HOST', 'terraform-20250210133316976400000001.cw34ekqygfuu.us-east-1.rds.amazonaws.com'),
    'user': os.getenv('DB_USER', 'admin'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'database': os.getenv('DB_NAME', 'mydb'),
    'port': os.getenv('DB_PORT', '3306')
}

# Create tasks table if it doesn't exist
def create_table():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            task VARCHAR(255) NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Add a task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if not task:
        return jsonify({'error': 'Task is required'}), 400

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task) VALUES (%s)', (task,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Task added successfully'}), 201

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify({'tasks': tasks}), 200

if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5000)