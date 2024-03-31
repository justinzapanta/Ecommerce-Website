from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
    

class SignIn():
    def __init__(self, email, password, request) -> None:
        self.email = email
        self.is_verified = authenticate(username=email, password=password)
        self.request = request


    def save_to_session(self) -> None:
        self.request.session['user_email'] = self.email


class SignUp():
    def __init__(self, email, password, first_name, last_name, request) -> None:
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.request = request

        self.email_exist = User.objects.filter(username=email)


    def register_account(self) -> None:
        if not self.email_exist:
            User.objects.create_user(
                username=self.email,
                email=self.email,
                password=self.password,
                first_name=self.first_name,
                last_name=self.last_name
            )
    

    def save_to_session(self):
        self.request.session['user_email'] = self.email


    def notify_user(self) -> str :
        if '@gmail.com' not in self.email:
            return 'Email addresses must have @gmail.com '
        
        return 'The password must be 8 characters or more'


        
    
