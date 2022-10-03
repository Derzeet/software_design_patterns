from Strategy import mail
from Component import Email

class sendEmail(mail):
    def sendEmail(self, email, text, reciever, emails) -> str:
        mail = Email()
        mail.create(email, text, reciever)
        emails.append(mail)
        return "Your message was sent"

