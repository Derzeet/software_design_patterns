from ConcreteStrategy import Login, Register
from EmailStrategy import sendEmail
from Account import Account, Email

if __name__ == '__main__':
    list = {}
    emails = []
    derzeet = Account(Register())
    result = derzeet.do_signing('cocarecu@gmail.com', 'astana2020', list)
    print(result)
    time = Account(Register())
    print(time.do_signing('derzeet@gmail.com', 'astana2020', list))
    derzeet = Account(Login())
    res = derzeet.do_signing('cocarecu@gmail.com', 'astana2020', list)
    print(res)

    email = Email()
    email.strategy(sendEmail())
    print(email.send('cocarecu@gmail.com', list, 'Hello', 'derzeet@gmail.com', emails))

    for email in emails:
        print(email.text, email.reciever, email.email, sep=' ')

