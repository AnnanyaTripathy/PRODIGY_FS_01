# 🔐 SecureAuth – Secure User Authentication System

A secure user authentication system developed using **Django** as part of **Prodigy InfoTech Full Stack Development Internship – Task 01**.

The application allows users to register, log in securely, access protected pages, and log out using Django's built-in authentication framework.

---

## 🚀 Features

- 👤 User Registration
- 🔑 Secure User Login
- 🚪 User Logout
- 🔒 Password Hashing using Django Authentication
- 🛡️ Session Management
- 📊 Protected Dashboard
- 🎨 Responsive Bootstrap User Interface
- 👨‍💼 Admin Panel Support

---

## 🛠️ Tech Stack

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- SQLite3

---

## 📂 Project Structure

```
PRODIGY_FS_01/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── dashboard.html
│   │       └── base.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── secure_auth/
│
├── static/
│   └── css/
│       └── style.css
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/AnnanyaTripathy/PRODIGY_FS_01.git
```

### Move into the Project

```bash
cd PRODIGY_FS_01
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

Add screenshots of:

- 🏠 Home Page
- 📝 Register Page
- 🔑 Login Page
- 📊 Dashboard
- 👨‍💼 Django Admin Panel

---

## 📌 Internship Information

**Internship:** Prodigy InfoTech

**Domain:** Full Stack Web Development

**Task:** Task-01 – Secure User Authentication System

---

## 👩‍💻 Author

**Annanya Tripathy**

GitHub: https://github.com/AnnanyaTripathy