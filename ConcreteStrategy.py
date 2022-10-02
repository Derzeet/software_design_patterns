from Strategy import SignIn

class Login(SignIn):
    def do_signin(self, email, password, list) -> str:
        if email in list.keys():
            if list.get(email) == password:
                return "Welcome, " + email
            else:
                return "Incorrect Password"
        else:
            return "No such user exists"


class Register(SignIn):
    def do_signin(self, email, password, list) -> str:
        list.update({email: password})
        return "You have created an account: " + email
