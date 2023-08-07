import uuid
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from firebase_admin import firestore

db = firestore.client()
course_Ref = db.collection('course')

courseAPI = Blueprint('courseAPI', __name__)

@courseAPI.route('/add', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        try:
            id = uuid.uuid4()
            course_data = {
                'name': request.form['name'],
                'duration': request.form['duration'],
                'category': request.form.getlist('category[]')  # Get the selected courses
            }
            course_Ref.document(id.hex).set(course_data)
            return redirect(url_for('courseAPI.read'))
        except Exception as e:
            return f"An error occurred: {e}"
    elif request.method == 'GET':
        return render_template('add_course.html')

@courseAPI.route('/list', methods=['GET'])
def read():
    try:
        all_courses = [doc.to_dict() for doc in course_Ref.stream()]
        return render_template('list_courses.html', courses=all_courses)
    except Exception as e:
        return f"An error occurred: {e}"
    