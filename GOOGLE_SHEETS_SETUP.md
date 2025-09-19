# Google Sheets API Setup Guide

## Step 1: Create a Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Sheets API:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click "Enable"

## Step 2: Create Service Account Credentials
1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "Service Account"
3. Fill in the service account details:
   - Name: `student-portal-service`
   - Description: `Service account for Student Portal app`
   - Click "Create and Continue"
4. Skip the optional steps and click "Done"
5. Click on the newly created service account
6. Go to "Keys" tab
7. Click "Add Key" > "Create new key"
8. Select "JSON" format
9. Download the JSON file and save it as `credentials.json` in your project root

## Step 3: Share Google Sheet with Service Account
1. Create a new Google Sheet or use an existing one
2. Copy the Sheet ID from the URL (the long string between `/d/` and `/edit`)
3. Share the sheet with the service account email:
   - Click "Share" button
   - Paste the service account email (found in credentials.json as "client_email")
   - Give "Editor" permissions
   - Click "Send"

## Step 4: Set Environment Variables
Create a `.env` file in your project root with:
```
GOOGLE_SHEETS_CREDENTIALS_PATH=credentials.json
GOOGLE_SHEETS_SPREADSHEET_ID=your_sheet_id_here
```

## Step 5: Install Dependencies
The required packages are already added to requirements.txt:
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- gspread

## Step 6: Update Your Code
The Flask app will be modified to use Google Sheets instead of Excel.

## Important Notes:
- Keep the `credentials.json` file secure and never commit it to version control
- Add `credentials.json` to your `.gitignore` file
- The service account needs access to the Google Sheet to read/write data
