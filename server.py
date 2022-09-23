from flask import Flask, render_template, request, url_for, redirect
from functools import wraps
from admin import Admin
import ShareMarket
import utility

app = Flask(__name__)
admin = Admin(app)
num = 0
res = None
# Route Starts #
# User Part
@app.route("/")
def user():
    return redirect(url_for('IndexFun'))

@app.route("/home")
def IndexFun():
    global num
    num = utility.randomNumberGenerator()
    return render_template("User/index.html")


@app.route("/contact" ,methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        Name = request.form['userName']
        Mail = request.form['userMail']
        Mobile = request.form['userMobile']
        Message = request.form['userMessage']
        msgStatus = utility.send_mail(Name,Mail,Mobile,Message)
        return render_template("User/contact.html",msg = msgStatus)
    return render_template("User/contact.html")


@app.route("/NumberGuessing/<int:value>")
def NumberGuessing_fun(value):
    return render_template("User/GuessingNumber.html", number=num, guessedVal=value)


@app.route("/Blog")
def blogIndexFun():
    global res
    res = utility.getBlogData()
    return render_template("User/blogindex.html", jobj=res)


@app.route("/Detail_Blog/<int:num>")
def showDetailBlog(num):
    return render_template("User/blog.html", jobj=res, blogNum=num - 1)


# Admin Part #

@app.route("/admin")
def admin_page():
    return redirect(url_for('admin_home'))

@app.route("/admin/home")
@admin.login_required
def admin_home():
    return render_template("Admin/admin.html")


@app.route("/admin/login", methods=['POST', 'GET'])
def admin_login_page():
    if not admin.isLogin:
        if request.method == 'POST':
            UserName = request.form['userName']
            Passw = request.form['password']
            if admin.login(UserName, Passw):
                return redirect(url_for('admin_home'))
            else:
                return render_template("Admin/login.html", LoginStatus="Invalid Credentials")
        return render_template("Admin/login.html")

    else:
        return redirect(url_for('admin_home'))


@app.route("/admin/logout")
def admin_logout():
    if admin.isLogin:
        admin.isLogin = False
    return redirect(url_for('admin_login_page'))


#admin Share Market Part #

@app.route("/admin/avg", methods=['POST', 'GET'])
@admin.login_required
def AvgCalculator():
        if request.method == 'POST':
            FBQ = request.form['FirstBuyQty']
            FBP = request.form['FirstBuyPrice']
            SBQ = request.form['SecondBuyQty']
            SBP = request.form['SecondBuyPrice']
            isFieldsEmpty, Text = ShareMarket.CalculateAveragePrice(FBQ, FBP, SBQ, SBP)
            if isFieldsEmpty:
                return "Enter All Fields"
            else:
                return render_template("Admin/AvgCalculator.html", outText=Text, FBQty=FBQ, FBPirce=FBP, SBQty=SBQ,
                                       SBPrice=SBP)
        else:
            return render_template("Admin/AvgCalculator.html")


@app.route("/admin/sm", methods=['POST', 'GET'])
@admin.login_required
def ShareMarket():
       if request.method == 'POST':
           CompName = request.form['CompanyName']
           FBQ = request.form['BuyQty']
           FBP = request.form['BuyPrice']

           '''
           isFieldsEmpty, Text = ShareMarket.ShareMarketData(FBQ, FBP,CompName)
           if isFieldsEmpty:
               return "Enter All Fields"
           else:
               return render_template("ShareMarket.html", outText=Text)
           '''
           return "hello"

       else:
            return render_template("Admin/ShareMarket.html")





@app.errorhandler(404)
def not_found(e):
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)