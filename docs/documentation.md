# Documentation: DualAuth – SQL Injection Demonstration WebApp

## Overview

**DualAuth** is a dual-mode login system demonstrating insecure and secure database authentication flows to highlight the risks and defenses against SQL injection attacks. The vulnerable mode uses unsafe SQL concatenation while the secure mode implements parameterized queries.

## Goals

- Simulate SQL injection attacks on a vulnerable login page.
- Compare with a properly secured login using best practices.
- Educate developers, testers, and students on injection flaws.

## Technologies Used

- Python 3.8+
- Flask for backend logic
- SQLite for embedded DB
- HTML5/CSS3 for UI
- Pytest for testing
- Docker (optional for deployment)

## Key Features

### Vulnerable Login
- Accepts raw input into SQL string
- Demonstrates injection like `' OR '1'='1' --`
- Logs suspicious inputs

### Secure Login
- Uses parameterized queries (`?`)
- Filters unauthorized access

### Dashboard
- Detects if login used SQLi payload
- Greets with success or warning based on method

### Awareness Page
- Explains SQL injection risk and prevention
- Links to real-world incidents and OWASP guides

## Security Concepts Demonstrated

| Concept           | Description                                   |
|------------------|-----------------------------------------------|
| SQL Injection    | Input manipulating SQL query logic            |
| Parameterization | Prevents SQLi by separating query from data   |
| Input Validation | Basic filtering of empty/invalid inputs       |
| Logging          | Tracks potentially malicious behavior         |

## SQL Injection Examples

- Bypass login:
  ```
  ' OR '1'='1' --
  ```
- Data extraction (advanced case, not shown in this app):
  ```
  ' UNION SELECT name, password FROM admin --
  ```

## Preventive Measures

- Use parameterized queries (always)
- Validate user input strictly (type, length, format)
- Restrict DB permissions (least privilege)
- Avoid raw SQL execution
- Use ORM frameworks when possible

## Known Vulnerabilities

The `/login-vuln` route is intentionally vulnerable. This route should never be used in production environments. It exists purely for educational purposes.

## License

This project is intended for ethical use and educational demonstrations only. Use responsibly and legally. Do not perform unauthorized testing on real systems.