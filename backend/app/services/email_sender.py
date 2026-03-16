import smtplib
from email.message import EmailMessage


def send_email(to_email, subject, body):

    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    return {"message": "Email sent successfully"}