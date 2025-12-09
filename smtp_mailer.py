import smtplib
from email.mime.text import MIMEText

print("\n=== SMTP Mail Sender (Python) ===\n")

sender_email = input("Your Gmail Address: ").strip()
app_password = input("Your App Password: ").strip()
receiver_email = input("Receiver Email: ").strip()
subject = input("Subject: ").strip()
message_body = input("Message: ").strip()

msg = MIMEText(message_body)
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

print("\nSending email...\n")

try:
    # Gmail SMTP Server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender_email, app_password)
    server.send_message(msg)

    print("✔ Email sent successfully!")

except Exception as e:
    print("❌ Error:", e)

finally:
    try:
        server.quit()
    except:
        pass
