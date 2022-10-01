import os
import utility
from flask import request,redirect,url_for

class Admin:
    def __init__(self):
        self.utilityObj = utility
        self.isLoggedIn = False

    def login(self ,user ,passw):
        print(len(user))
        print(len(passw))
        if len(user) > 0 or len(passw) > 0:
            if user.lower() == os.getenv("ADMIN_USER") and passw == os.getenv("ADMIN_PASSWORD"):
               self.isLoggedIn = True
            return self.isLoggedIn,False
        return self.isLoggedIn,True

    def logOut(self):
        if self.isLoggedIn:
            self.isLoggedIn = False
        return "Admin/login.html",""

    def proceedLogin(self):
        if not self.isLoggedIn:
            if request.method == 'POST':
                UserName = request.form['userName']
                Passw = request.form['password']
                isloginSuccess,isFieldsEmpty = self.login(UserName, Passw)
                print(isFieldsEmpty)
                if isFieldsEmpty:
                    return "Admin/login.html", "Enter all Fields"
                else:
                    if isloginSuccess:
                      return "Admin/admin.html",""
                    else:
                      return "Admin/login.html","Invalid Credentials"
            return "Admin/login.html",""
        else:
            return  "Admin/admin.html",""

    def contact_admin(self):
        if request.method == 'POST':
            Name = request.form['userName']
            Mail = request.form['userMail']
            Mobile = request.form['userMobile']
            Message = request.form['userMessage']
            MsgSent, msgStatus = utility.send_mail(Name, Mail, Mobile, Message)
            return MsgSent, msgStatus
        return False,''

    def login_required(self,f):
       # @wraps(f)
        def wrapper(*args, **kwargs):
            if not self.isLoggedIn:
                return redirect(url_for('admin_login_page'))
            return f(*args, **kwargs)

        wrapper.__name__ = f.__name__
        return wrapper


