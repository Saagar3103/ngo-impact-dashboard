# 🌐 NGO Impact Dashboard

A full-stack web application designed to help NGOs submit monthly impact reports and enable administrators to view consolidated analytics.

---

## 🚀 Features

- 📥 Submit NGO monthly reports
- 📊 View aggregated dashboard insights
- 📅 Filter data by month
- ⚡ Real-time data processing
- 🎯 Clean and responsive UI

---

## 🧰 Tech Stack

### Frontend
- HTML
- CSS (Custom styling)
- JavaScript (Fetch API)

### Backend
- Python (Flask)
- Flask-CORS

### Database
- SQLite

### Deployment (Planned)
- Backend: Render
- Frontend: Static hosting (Netlify / Vercel)

---

## 📡 API Endpoints

### 1. Submit Report
```http
POST /report


//REQUEST BODY
{
  "ngo_id": "NGO1",
  "month": "2026-04",
  "people_helped": 100,
  "events": 5,
  "funds": 20000
}

GET DASHBOARD DATA:
GET /dashboard?month=YYYY-MM

//Example :
GET /dashboard?month=2026-04

--> Response :
{
  "total_ngos": 3,
  "total_people": 670,
  "total_events": 15,
  "total_funds": 115000
}

||Project Structure||

ngo-impact-dashboard/
│
├── backend/
│   ├── app.py
│   ├── database.db
│   ├── requirements.txt
│   └── Procfile
│
├── frontend/
│   ├── index.html
│   ├── dashboard.html
│   └── style.css
│
└── README.md


->Approach
The project was built using a backend-first approach. The API endpoints were designed to handle data submission and aggregation efficiently using SQLite. Once validated using Postman, a lightweight frontend was developed to interact with these APIs.

Focus was given to:

Clean architecture
Simple and functional UI
Accurate data aggregation logic



<-- AI TOOLS were used to: -->
Understand backend API structuring
Debug CORS and server issues
Improve UI design and code organization

<-- Future Improvements -->
Add authentication for admin users
Introduce charts and data visualization
Migrate frontend to React for scalability
Add validation and error handling enhancements
Deploy complete system with live endpoints

