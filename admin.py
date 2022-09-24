import os

class Admin:
    def __init__(self,app):
        self.flaskObj = app
        self.isLogin = False

    def login(self ,user ,passw):
        if user.lower() == os.getenv("ADMIN_USER")and passw == os.getenv("ADMIN_PASSWORD"):
            self.isLogin = True
        return self.isLogin

    def logged_In(self):
        return self.isLogin

    def login_required(self,f):
       # @wraps(f)
        def wrapper(*args, **kwargs):
            if not self.isLogin:
                return self.flaskObj.redirect(self.flaskObj.url_for('admin_login_page'))
            return f(*args, **kwargs)

        wrapper.__name__ = f.__name__
        return wrapper


