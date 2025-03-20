from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {
        'id': 1,
        'name': 'tiger',
        'age': 10
    },
    {
        'id': 2,
        'name': 'jacob',
        'age': 11
    }
]

@app.route('/students-list', methods=['GET'])
def get_students_list():
    return jsonify(students)

@app.route('/student/get/<int:id>', methods=['GET'])
def get_student_by_id(id):
    student = next((std for std in students if std['id'] == id), None)
    if student:
        return jsonify(student)
    return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5010, debug=True)