# 🔐 Password Generator

A simple, secure, and production-ready Python password generator with full DevOps pipeline integration.

---

[![CI/CD](https://github.com/Danuptra/generate-password/actions/workflows/main.yml/badge.svg)](https://github.com/Danuptra/generate-password/actions)
[![Coverage](https://img.shields.io/badge/coverage-automated-brightgreen)](htmlcov/index.html)
[![Security Scanning](https://img.shields.io/badge/security-SAST-blue)](https://github.com/Danuptra/generate-password/actions)

---

## 🚀 DevOps & Security Highlights

This repository demonstrates strong DevOps and security practices:

- **Automated CI/CD** with GitHub Actions
    - Unit testing with coverage reporting
    - Build artifacts for password output and coverage reports
- **SAST (Static Application Security Testing)**
    - Bandit for Python static code analysis
- **Security Best Practices**
    - Password generation uses Python's `secrets` module (cryptographically secure)
    - Automated checks for code quality and vulnerabilities
- **Modular & Testable Code**
    - Testable with `unittest`
    - Coverage report generated and uploaded as artifact

---

## 📦 Requirements

- Python 3.7 or newer

---

## ✨ Features

- Generate strong and secure passwords
- Customize password length
- Choose character types:
  - ✅ Uppercase letters (A-Z)
  - ✅ Lowercase letters (a-z)
  - ✅ Numbers (0-9)
  - ✅ Symbols (!@#$%^&*...)
- Easy to use and extend
- Option to **save the generated password to a file**

---

## ⚙️ Configuration Options

- **Password length**: e.g. 12, 16, 20
- **Character types**:
  - Include uppercase letters
  - Include lowercase letters
  - Include numbers
  - Include symbols

---

## 🚀 How to Use

1. **Clone the repository**

    ```bash
    git clone https://github.com/Danuptra/generate-password.git
    cd generate-password
    ```

2. **Run the script**

    ```bash
    python main.py
    ```

---

## 🛡️ CI/CD & Security Pipeline Example

CI/CD pipeline (GitHub Actions):
- SAST: `bandit -r .` (static code analysis)
- Unit Test & Coverage: `coverage run -m unittest test_main.py` + `coverage report` + `coverage html`
- Artifacts: Password file & HTML coverage report auto-uploaded

You can see the workflow in `.github/workflows/main.yml`.

---

## 📄 License

MIT License. Feel free to use, modify, and distribute.

---

Made with ❤️ by [Danuptra](https://github.com/Danuptra)