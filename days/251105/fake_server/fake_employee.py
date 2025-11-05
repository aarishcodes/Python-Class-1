from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "Hello, Flask!"

employees = [
    {'id': 101, 'name': 'Aarish', 'role': 'TCE'},
    {'id': 102, 'name': 'Kirti', 'role': 'Manager'}
]

@app.route('/get_employee', methods=['GET'])
def get_employee():
    return jsonify(employees)

@app.route('/get_employee/<int:emp_id>', methods=['GET'])
def find_employee_by_id(emp_id):
    for employee in employees:
        if employee['id'] == emp_id:
            return jsonify(employee)

    return jsonify({"error": "Employee not found"}), 404
    

@app.route('/create_employee', methods=['POST'])
def create_employee():
    data = request.get_json()

    if not data or "name" not in data or 'id' not in data or 'role' not in data:
        return jsonify({"error": "Please enter the data"}), 400
    
    new_employee = {
        "id": data["id"],
        "name": data["name"],
        "role": data["role"]
    }

    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route("/delete/<int:emp_id>", methods=['DELETE'])
def delete_by_id(emp_id):
    
    for employee in employees:
        if employee["id"] == emp_id:
            employees.remove(employee)
            return jsonify({'message': 'Successfully deleted the Employee by the id'}), 200
        
    return jsonify({"message": "error while deleting the employee"}), 500


if __name__ == '__main__':
    app.run(debug=True)