# Student Portal

A web-based application for managing student information using Flask and Excel integration.

## Description

The Student Portal is a simple yet effective web application that allows users to search for student details by enrollment number and update their information. The application uses an Excel file as the data storage backend, making it easy to manage and maintain student records without requiring a full database setup.

## Features

- **Student Search**: Search for students using their enrollment number with real-time validation
- **Modern Student Profile Display**: Beautiful glassmorphism design with animated sections showing comprehensive student information
- **View Details**: Display student information in organized sections:
  - Basic Information (Personal details, contact info)
  - Academic Information (Department, batch, CGPA, attendance)
  - Administrative Details (Admission info, fee status, remarks)
- **Update Information**: Modify student details with a user-friendly form interface
- **Responsive Design**: Fully responsive UI that works on all devices with smooth animations
- **Modern UI/UX**: Glassmorphism effects, gradient backgrounds, hover animations, and micro-interactions
- **Confirmation System**: Visual feedback with confetti animations after successful updates
- **Typography**: Clean, modern typography using Inter font family
- **Icons**: Font Awesome icons for better visual hierarchy

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Storage**: Excel (openpyxl) or Google Sheets API
- **Styling**: Custom CSS with modern design principles
- **Environment**: python-dotenv for configuration management

## Installation

1. **Clone the repository** (if applicable) or ensure you have the project files in your directory.

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up data storage**:
   - **Option A: Excel File**: Ensure you have `students.xlsx` in the root directory with all required columns as shown in the Data Format section below
   - **Option B: Google Sheets**: Follow the setup guide in `GOOGLE_SHEETS_SETUP.md` for cloud-based data storage

4. **Configure environment variables** (if using Google Sheets):
   Create a `.env` file in your project root:
   ```env
   GOOGLE_SHEETS_CREDENTIALS_PATH=credentials.json
   GOOGLE_SHEETS_SPREADSHEET_ID=your_sheet_id_here
   ```
   **Note**: Keep `credentials.json` secure and add it to `.gitignore`

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   - Open your browser and navigate to `http://localhost:5000`

## Usage

1. **Search for a Student**:
   - Enter the enrollment number in the search field
   - Click "Search Student" to retrieve information

2. **View Student Information**:
   - The application displays all student details in a readable format



## Project Structure

```
student-portal/
│
├── app.py                         
├── requirements.txt                               
├── README.md                    
├── .env
│
├── static/                
│   ├── css/
│   │   ├── style.css          
│   │   └── student_info_custom.css 
│   ├── js/
│   │   └── script.js              
│   
│
└── templates/
    ├── index.html        
    ├── student_info.html         
    └── confirmation.html          
```

## Data Format

The `spreadsheet` file should follow this structure with all required columns:

| Enrollment | Name | Gender | DOB | Contact | Email | Address | Branch | Department | Batch | Division | Roll Number | Year | CGPA | Attendance | Admission Year | Admission Category | Fee Status | Remarks |
|------------|------|--------|-----|---------|-------|---------|--------|------------|-------|----------|-------------|------|------|------------|---------------|-------------------|------------|---------|
| 2203051240090 | Satyam Kumar | Male | 2003-01-01 | 7488253867 | 2203051240060@paruluniversity.ac.in | Maurya Vihar Colony, Khagaul, Bihar 801105 | CSE AI | Computer Science | 2022 | A | 12345 | 4 | 8.5 | 85 | 2022 | General | Paid | Good student |

## Contributors

<table align="center">
 <tr>
    <td align="center">
      <img src="https://github.com/mohit-kumar-saini.png" width="100"><br>
      <strong>Mohit Kumar Saini</strong><br>
      <a href="https://github.com/mohit-kumar-saini">@mohit-kumar-saini</a>
    </td>
    <td align="center">
      <img src="https://github.com/rajakRahul1283.png" width="100"><br>
      <strong>Rahul Kumar Rajak</strong><br>
      <a href="https://github.com/rajakRahul1283">@rajakRahul1283</a>
    </td>
    <td align="center">
      <img src="https://github.com/Satyaamp.png" width="100"><br>
      <strong>Satyam Kumar</strong><br>
      <a href="https://github.com/Satyaamp">@Satyaamp</a>
    </td>
</tr>
</table>

## Notes

- The application runs in debug mode by default for development
- All changes are saved directly to the SpreadSheet file

