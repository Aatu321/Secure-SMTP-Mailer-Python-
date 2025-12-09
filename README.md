# Secure-SMTP-Mailer-Python-
A simple Python-based SMTP mailer that sends emails using Gmail’s SMTP server with secure app passwords. Includes config storage, easy UI, and error handling.
# SMTP Mailer (Python)

SMTP Mailer is a lightweight Python tool that allows you to securely send emails directly from your terminal using Gmail's SMTP server and an App Password.  
It is designed for cybersecurity learners, automation scripts, and developers who want a simple, fast, and secure way to send emails programmatically.

---

## 🚀 Features
- Send emails from terminal using Python
- Secure authentication using Gmail App Password
- Automatic configuration file generation (`smtp_config.json`)
- Saves your SMTP settings for future use
- Error-handled and user-friendly CLI interface
- Pure Python — no external libraries required

---

## 📦 Installation
Clone the repository:

```bash
git clone https://github.com/Aatu321/SMTP-Mailer.git
cd SMTP-Mailer
```

No extra dependencies needed.

---

## 🧠 How It Works
On first run, the script asks for:

- Your Gmail address  
- Your Gmail App Password  

These are saved securely in `smtp_config.json`.

Next, you enter:

- Receiver email  
- Subject  
- Message  

And the email is sent through Gmail’s SMTP server.

---

## 📝 Usage

Run:

```bash
python smtp_mailer.py
```

Example Prompt Flow:

```
=== SMTP Mailer (Python) ===

Receiver Email: example@gmail.com
Subject: Test Email
Message: Hello! This is an SMTP test message.

Connecting to SMTP server...
Email sent successfully!
```

---

## 🔐 Security Notes

- Works only with **Gmail App Password**, not your normal password  
- App Password requires **2-step verification enabled**  
- Your app password is stored locally in a config file  
- Do NOT share this file with anyone  

---

## 📄 Requirements
- Python 3.x  
- Gmail Account with App Password Enabled  

---

## ⚠️ Disclaimer
This tool is intended for **educational, personal automation, and ethical use cases only**.  
Do NOT use this script for spamming or unauthorized emailing.

---

## 📚 License
MIT License — Free to use and modify.

---

