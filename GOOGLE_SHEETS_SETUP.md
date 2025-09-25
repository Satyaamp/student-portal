# 📝 Google Sheets API Setup Guide

Follow these steps to integrate **Google Sheets** with the **Student Portal** app.

![Google Sheets](https://img.shields.io/badge/Sheets-Google-green?style=for-the-badge\&logo=google) ![API](https://img.shields.io/badge/API-Google-blue?style=for-the-badge\&logo=google) ![Flask](https://img.shields.io/badge/Flask-Python-orange?style=for-the-badge\&logo=flask)

---

## 1️⃣ Step 1: Create a Google Cloud Project

1. 🌐 Go to [Google Cloud Console](https://console.cloud.google.com/)
2. ➕ Create a **new project** or select an existing one
3. 🔓 Enable **Google Sheets API**:

   * Navigate to **APIs & Services → Library**
   * Search for **Google Sheets API**
   * Click **Enable** ✅

---

## 2️⃣ Step 2: Create Service Account Credentials

1. 🛠 Go to **APIs & Services → Credentials**
2. ➕ Click **Create Credentials → Service Account**
3. 📝 Fill in the details:

   * **Name**: `student-portal-service`
   * **Description**: `Service account for Student Portal app`
   * Click **Create and Continue**
4. ⏭ Skip optional steps → Click **Done**
5. 🔑 Open the newly created **service account**
6. 🗝 Go to the **Keys** tab
7. ➕ Click **Add Key → Create new key**
8. 🗂 Select **JSON** format
9. 💾 Download the file and save as `credentials.json` in your project root

---

## 3️⃣ Step 3: Share Google Sheet with Service Account

1. 🆕 Create a new Google Sheet or use an existing one
2. 🔗 Copy the **Sheet ID** from the URL (between `/d/` and `/edit`)
3. 📤 Share the sheet with the service account email:

   * Click **Share**
   * Paste the service account email from `credentials.json` (`client_email`)
   * Give **Editor** permissions
   * Click **Send** ✅

---

## 4️⃣ Step 4: Set Environment Variables

Create a `.env` file in your project root:

```env
GOOGLE_SHEETS_CREDENTIALS_PATH=credentials.json
GOOGLE_SHEETS_SPREADSHEET_ID=your_sheet_id_here
```

---

## 5️⃣ Step 5: Install Dependencies

Required packages are in `requirements.txt`:

* 📦 `google-api-python-client`
* 🔐 `google-auth-httplib2`
* 🔑 `google-auth-oauthlib`
* 📄 `gspread`

Install via:

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Step 6: Update Your Code

🔄 Modify the Flask app to use **Google Sheets** instead of Excel.

---

## ⚠️ Important Notes

* 🔒 Keep `credentials.json` **secure**; never commit it
* ❌ Add `credentials.json` to `.gitignore`
* 👥 The service account **must have access** to the Google Sheet to read/write data

---
