from django.shortcuts import render, redirect
from .forms import SignIn_Form, SignUp_Form
from .authentication import SignIn, SignUp

# Create your views here.

def sign_in(request):
    if 'user_email' not in request.session:
        form = {
            'signIn_form' : SignIn_Form() 
        }

        if request.method == 'POST':
            signin_form = SignIn_Form(request.POST)

            if signin_form.is_valid():
                user = SignIn(
                    signin_form.cleaned_data['email'],
                    signin_form.cleaned_data['password'],
                    request
                )

                if user.is_verified:
                    user.save_to_session()
                    return redirect('shop')
                
                form['notif'] = 'Invalid Email or Password'

        return render(request, 'user_authentication/login.html', form , status=200)
    return redirect('shop')


def sign_up(request):
    if 'user_email' not in request.session:
        form = {
            'signUp_form' : SignUp_Form()
        }

        if request.method == "POST":
            signup_form = SignUp_Form(request.POST)

            if signup_form.is_valid():
                user = SignUp(
                    signup_form.cleaned_data['email'],
                    signup_form.cleaned_data['password'],
                    signup_form.cleaned_data['first_name'],
                    signup_form.cleaned_data['last_name'],
                    request
                )
                
                if not user.email_exist:
                    if len(request.POST['password']) >= 8:
                        user.register_account()
                        user.save_to_session()
                        return redirect('shop')
                    
                    form['notif'] = 'password must be 8 characters above'
                else:
                    form['notif'] = 'The email already exists'

            if '@gmail.com' not in request.POST['email']:
                form['notif'] = 'Email addresses must have @gmail.com'         
            
        return render(request, 'user_authentication/signUp.html', form, status=200)
    return redirect('shop')


def sign_out(request):
    if 'user_email' in request.session:
        del request.session['user_email']
    return redirect('index')