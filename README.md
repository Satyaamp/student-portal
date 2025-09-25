
# 🎓 Student Portal

A **web-based application** for managing student information with **Flask** and **Google Sheets integration**.

![Student Portal Banner](https://img.shields.io/badge/Student-Portal-blue?style=for-the-badge&logo=python) 
![Flask](https://img.shields.io/badge/Backend-Flask-orange?style=for-the-badge&logo=flask) 
![Sheets](https://img.shields.io/badge/Data-Sheets-green?style=for-the-badge&logo=google) 
![Responsive](https://img.shields.io/badge/Responsive-✅-brightgreen?style=for-the-badge)

---

## 🔥 Live Demo

Experience it live here:  
[🌐 https://studentportal-ob5j.onrender.com/](https://studentportal-ob5j.onrender.com/)

💡 **Try these sample Enrollment Numbers:**  
- `2202051240060`  
- `2203051240078`  
- `2203051240090`

---

## ✨ Features

* 🔍 **Student Search**: Search by enrollment number with real-time validation
* 🖼 **Modern Profile Display**: Glassmorphism design with animated sections
* 📚 **View Details**:

  * **Basic Info**: Personal details, contact info
  * **Academic Info**: Department, batch, CGPA, attendance
  * **Administrative Details**: Admission info, fee status, remarks
* 📱 **Responsive UI**: Works perfectly on desktop, tablet, and mobile
* 🎨 **Modern Design**: Glassmorphism, gradient backgrounds, hover animations, and micro-interactions
* 🔤 **Typography**: Clean, modern Inter font family
* 🖼 **Icons**: Font Awesome for better visual hierarchy

---

## 💻 Tech Stack

| Layer        | Technology                           |
| ------------ | ------------------------------------ |
| Backend      | Python Flask                         |
| Frontend     | HTML5, CSS3, JavaScript              |
| Styling      | Glassmorphism & Custom CSS           |
| Data Storage | Excel (openpyxl) / Google Sheets API |
| Environment  | python-dotenv                        |

---

## 🚀 Installation

1. **Clone the repo**:

```bash
git clone https://github.com/Satyaamp/student-portal.git
cd student-portal
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set up data storage**:

* **Option A: Excel** – Add `students.xlsx` to the root directory with required columns.
- **Option B: Google Sheets** – Follow the setup guide here:  
[📄 GOOGLE_SHEETS_SETUP.md](https://github.com/Satyaamp/student-portal/blob/main/GOOGLE_SHEETS_SETUP.md)


4. **Configure environment variables** (if using Google Sheets):

```env
GOOGLE_SHEETS_CREDENTIALS_PATH=credentials.json
GOOGLE_SHEETS_SPREADSHEET_ID=your_sheet_id_here
```

5. **Run the app**:

```bash
python app.py
```

6. **Open the app** in your browser:

```
http://localhost:5000
```

---

## 📝 Usage

1. **Search a Student**: Enter the enrollment number → Click **Search Student**
2. **View Profile**: Displays full student details in a beautiful layout

---

## 🗂 Project Structure

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
└── templates/
    ├── index.html        
    ├── student_info.html         
```

---

## 🗃 Data Format

| Enrollment    | Name         | Gender | DOB        | Contact    | Email                                                                             | Address                                    | Branch | Department       | Batch | Division | Roll Number | Year | CGPA | Attendance | Admission Year | Admission Category | Fee Status | Remarks           |
| ------------- | ------------ | ------ | ---------- | ---------- | --------------------------------------------------------------------------------- | ------------------------------------------ | ------ | ---------------- | ----- | -------- | ----------- | ---- | ---- | ---------- | -------------- | ------------------ | ---------- | ----------------- |
| 2203051240090 | Satyam Kumar | Male   | 2003-01-01 | 7488253867 | [2203051240060@paruluniversity.ac.in](mailto:2203051240060@paruluniversity.ac.in) | Maurya Vihar Colony, Khagaul, Bihar 801105 | CSE AI | Computer Science | 2022  | A        | 12345       | 4    | 8.5  | 85         | 2022           | General            | Paid       | Excellent student |

---

## 🌟 Contributors

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

---

## ⚠️ Notes

* Runs in **debug mode** by default for development
* All updates are **read-only** for now (no modification allowed)
* **Modern UI/UX** ensures smooth animations and responsive design

---


