from Strategy import mail
from Account import Email

class sendEmail(mail):
    def sendEmail(self, email, list, text, reciever, emails) -> str:
        if reciever in list.keys():
            mail = Email()
            mail.create(email, text, reciever)
            emails.append(mail)
            return "Your message was sent"
        else:
            return "No such email"

