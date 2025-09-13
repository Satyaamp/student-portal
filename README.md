# Student Portal

A web-based application for managing student information using Flask and Excel integration.

## Description

The Student Portal is a simple yet effective web application that allows users to search for student details by enrollment number and update their information. The application uses an Excel file as the data storage backend, making it easy to manage and maintain student records without requiring a full database setup.

## Features

- **Student Search**: Search for students using their enrollment number
- **View Details**: Display comprehensive student information including personal details, course information, and fee status
- **Update Information**: Modify student details with a user-friendly form interface
- **Responsive Design**: Modern, mobile-friendly UI with smooth animations
- **Real-time Validation**: Client-side validation for enrollment numbers
- **Confirmation System**: Feedback after successful updates

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Storage**: Excel (openpyxl)
- **Styling**: Custom CSS with modern design principles

## Installation

1. **Clone the repository** (if applicable) or ensure you have the project files in your directory.

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure you have the data file**:
   - The application requires `students.xlsx` in the root directory
   - The Excel file should have the following columns: Enrollment, Name, DOB, Address, Contact, Course, Year, Email, Fee Status, Remarks

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   - Open your browser and navigate to `http://localhost:5000`

## Usage

1. **Search for a Student**:
   - Enter the enrollment number in the search field
   - Click "Search Student" to retrieve information

2. **View Student Information**:
   - The application displays all student details in a readable format

3. **Update Student Information**:
   - Modify any fields as needed
   - Click "Update" to save changes
   - Receive confirmation of successful update

## Project Structure

```
student-portal/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── students.xlsx          # Student data file
├── static/
│   ├── css/
│   │   └── style.css      # Custom stylesheets
│   └── js/
│       └── script.js      # Client-side JavaScript
└── templates/
    ├── index.html         # Search page
    ├── student_info.html  # Student details and update form
    └── confirmation.html  # Update confirmation page
```

## Data Format

The `students.xlsx` file should follow this structure:

| Enrollment | Name | DOB | Address | Contact | Course | Year | Email | Fee Status | Remarks |
|------------|------|-----|---------|---------|--------|------|-------|------------|---------|
| 2203051240090 | Satyam Kumar | 2003-01-01 | Maurya Vihar Colony, Khagaul, Bihar 801105 | 7488253867 | B.Tech CSE AI | 4 | 2203051240060@paruluniversity.ac.in | Paid | Good student |

## Contributors

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/sayout-de003.png" width="100"><br>
      <strong>Sayantan De</strong><br>
      <a href="https://github.com/sayout-de003">@sayout-de003</a>
    </td>
    <td align="center">
      <img src="https://github.com/himasnhu018.png" width="100"><br>
      <strong>Himanshu Kumar Gupta</strong><br>
      <a href="https://github.com/himasnhu018">@himasnhu018</a>
    </td>
    <td align="center">
      <img src="https://github.com/Satyaamp.png" width="100"><br>
      <strong>Satyam Kumar</strong><br>
      <a href="https://github.com/Satyaamp">@Satyaamp</a>
    </td>
  </tr>
</table>

## Notes

- Ensure the Excel file is not open in another application when updating records
- The application runs in debug mode by default for development
- All changes are saved directly to the Excel file

