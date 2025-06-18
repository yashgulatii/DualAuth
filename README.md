# DualAuth – SQL Injection Demonstration WebApp

**DualAuth** is an educational web application that demonstrates both **vulnerable** and **secure** login systems, helping users understand the dangers of SQL Injection (SQLi) and how to prevent them. This project provides hands-on experience for both Red Team and Blue Team perspectives.

##  Features

- Dual login modes: vulnerable and secure
- Realistic SQL injection attack simulation
- Custom dashboard showing whether a login was hacked
- Awareness page with in-depth guidance on SQLi
- Input validation and error handling
- Logging of attempted injections
- Modular frontend-backend structure
- Test suite for frontend and backend
- Docker-ready architecture

##  Project Structure

```
DualAuth/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── database/
│   └── logs/
├── frontend/
│   ├── templates/
│   └── static/
├── tests/
├── docker-compose.yml
├── .gitignore
├── README.md
└── Docs/
    └── documentation.md
```

##  Getting Started (Local Setup)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/DualAuth.git
cd DualAuth
```

### 2. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```

Then go to: [http://localhost:5000](http://localhost:5000)

##  Docker Usage

```bash
docker-compose up --build
```

##  Run Tests

```bash
pip install pytest
pytest tests/
```

##  Learn More

- [docs/documentation.md](docs/documentation.md)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger SQLi](https://portswigger.net/web-security/sql-injection)