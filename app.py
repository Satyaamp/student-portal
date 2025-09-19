from flask import Flask, render_template, request, redirect, jsonify
import gspread
from google.oauth2.service_account import Credentials
import os
import json
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables (for local .env file)
load_dotenv()

app = Flask(__name__)

# Headers for students
HEADERS = [
    'Enrollment No. ', 'Name', 'Gender', 'DOB', 'Contact', 'Email', 'Address',
    'Course', 'Department', 'Batch', 'Section', 'Roll Number', 'Year', 'CGPA',
    '  Attendance  ', '  Admission Year  ', '  Admission Category  ',
    'Fee Status', 'Remarks'
]


# Google Sheets client setup
def get_google_sheets_client():
    spreadsheet_id = os.environ.get("GOOGLE_SHEETS_SPREADSHEET_ID")
    creds_json = os.environ.get("GOOGLE_SHEETS_CREDENTIALS_JSON")

    if spreadsheet_id is None:
        raise ValueError("GOOGLE_SHEETS_SPREADSHEET_ID not set")

    if creds_json:
        # Running on Render (env variable contains JSON)
        creds_dict = json.loads(creds_json)
        creds = Credentials.from_service_account_info(
            creds_dict,
            scopes=[
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]
        )
    else:
        # Running locally (use credentials.json file)
        creds = Credentials.from_service_account_file(
            "credentials.json",
            scopes=[
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]
        )

    client = gspread.authorize(creds)
    return client.open_by_key(spreadsheet_id).sheet1


def get_student(enroll_no):
    try:
        sheet = get_google_sheets_client()
        records = sheet.get_all_records()
        enroll_no = str(enroll_no).strip()

        for record in records:
            if str(record.get('Enrollment No. ', '')).strip() == enroll_no:
                student = [record.get(header, '') for header in HEADERS]

                # Format DOB mm/dd/yyyy -> dd/mm/yyyy
                if student[3]:
                    try:
                        dt = datetime.strptime(student[3], "%m/%d/%Y")
                        student[3] = dt.strftime("%d/%m/%Y")
                    except:
                        pass
                return student
        return None
    except Exception as e:
        print(f"Error accessing Google Sheets: {e}")
        return None


def update_student(enroll_no, updated_data):
    try:
        sheet = get_google_sheets_client()
        records = sheet.get_all_records()
        enroll_no = str(enroll_no).strip()

        for i, record in enumerate(records, start=2):  # Row 2 onwards
            if str(record.get('Enrollment No. ', '')).strip() == enroll_no:
                sheet.update(f'A{i}:S{i}', [updated_data])
                return True
        return False
    except Exception as e:
        print(f"Error updating Google Sheets: {e}")
        return False


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        enroll_no = request.form.get('enroll_no')
        if not enroll_no:
            return "Enrollment number is missing", 400

        student = get_student(enroll_no)
        if student:
            cleaned_headers = [h.lower().replace(' ', '_') for h in HEADERS]
            return render_template(
                'student_info.html',
                student=student,
                headers=HEADERS,
                cleaned_headers=cleaned_headers
            )
        else:
            return "Enrollment number not found"
    return render_template('index.html')


@app.route('/api/student/<enroll_no>')
def get_student_api(enroll_no):
    student = get_student(enroll_no)
    if student:
        short_info = {
            'enrollment': student[0],
            'name': student[1],
            'course': student[7],
            'year': student[12],
            'mail': student[5]
        }
        return jsonify(short_info)
    else:
        return jsonify({'error': 'Student not found'}), 404


@app.route('/student/<enroll_no>')
def student_info(enroll_no):
    student = get_student(enroll_no)
    if student:
        cleaned_headers = [h.lower().replace(' ', '_') for h in HEADERS]
        return render_template(
            'student_info.html',
            student=student,
            headers=HEADERS,
            cleaned_headers=cleaned_headers
        )
    else:
        return "Student not found", 404


@app.route('/update', methods=['POST'])
def update():
    updated_data = [
        request.form.get('enrollment'),
        request.form.get('name'),
        request.form.get('gender'),
        request.form.get('dob'),
        request.form.get('contact'),
        request.form.get('email'),
        request.form.get('address'),
        request.form.get('course'),
        request.form.get('department'),
        request.form.get('batch'),
        request.form.get('section'),
        request.form.get('roll_number'),
        request.form.get('year'),
        request.form.get('cgpa'),
        request.form.get('attendance'),
        request.form.get('admission_year'),
        request.form.get('admission_category'),
        request.form.get('fee_status'),
        request.form.get('remarks')
    ]
    success = update_student(updated_data[0], updated_data)
    if success:
        return render_template('confirmation.html', student=updated_data)
    else:
        return "Error updating student. Ensure Google Sheets is accessible.", 500


if __name__ == '__main__':
    app.run(debug=True)
