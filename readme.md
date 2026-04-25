# 🚀 NGO Impact Tracker

A full-stack web application to collect, manage, and visualize NGO activity data through a clean and interactive dashboard.

---

## 🔗 Live Demo

- 🌐 Frontend: https://ngo-impact-tracker.netlify.app  
- ⚙️ Backend API: https://ngo-impact-backend-0dlg.onrender.com  
- 💻 GitHub Repository: https://github.com/Saagar3103/ngo-impact-dashboard  

---

## 📌 Overview

The **NGO Impact Tracker** enables users to submit monthly NGO reports and view aggregated insights such as total NGOs, people impacted, events conducted, and funds utilized.

This project demonstrates **end-to-end full-stack development**, including frontend UI, backend API, database handling, and cloud deployment.

---

## ⚙️ Features

- 📥 Submit NGO reports via form  
- 📊 View summarized dashboard analytics  
- 🔄 Real-time API integration  
- 🌍 Fully deployed application  
- 🎯 Clean, minimal, professional UI  

---

## 🛠️ Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript (Fetch API)

### Backend
- Python  
- Flask  

### Database
- SQLite  

### Deployment
- Netlify (Frontend)  
- Render (Backend)  
- GitHub (Version Control)  

---

## 🧠 Approach

1. Designed a minimal and intuitive UI for data entry and visualization  
2. Developed RESTful APIs using Flask:
   - `POST /report` → Submit NGO data  
   - `GET /dashboard` → Fetch aggregated insights  
3. Stored data using SQLite database  
4. Connected frontend and backend using Fetch API  
5. Deployed backend on Render and frontend on Netlify  
6. Ensured smooth communication between client and server  

---

## 📁 Project Structure

```text
ngo-impact-dashboard/
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


---

## 🚀 Setup Instructions

###
 
 
 1. Clone Repository
```bash
git clone https://github.com/Saagar3103/ngo-impact-dashboard.git
cd ngo-impact-dashboard

2. Backend Setup
    cd backend
pip install -r requirements.txt
python app.py

3. Frontend
Open:
frontend/index.html

📊 API Endpoints
➤ Submit Report
POST /report

Request Body (JSON):
    {
  "ngo_id": "NGO1",
  "month": "2026-04",
  "people_helped": 100,
  "events": 5,
  "funds": 5000
}

➤ Get Dashboard 
GET /dashboard?month=2026-04

Response:
-> {
  "total_ngos": 1,
  "total_people": 100,
  "total_events": 5,
  "total_funds": 5000
}

Future Improvements
->Add authentication (Login/Register)
-> Add charts & data visualization
-> Use PostgreSQL for scalability
-> Improve responsiveness (mobile-friendly UI)
-> Export reports (PDF/CSV)
-> Use of AI Tools

AI tools were used for:

Debugging deployment issues
Improving UI/UX design
Structuring backend logic
Generating documentation

👨‍💻 Author
Saagar Priyadarshi
GitHub: https://github.com/Saagar3103

⭐ Conclusion

This project demonstrates the ability to build, deploy, and integrate a complete full-stack application with real-world functionality, showcasing strong development and problem-solving skills.
