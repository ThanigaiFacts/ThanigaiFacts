import os
from flask import Flask, render_template, request, url_for, redirect
from functools import wraps
from dotenv import load_dotenv
from admin import Admin
from news import News
from datetime import timedelta
import ShareMarket as shares
from placeholder import PlaceHolder

# initialization #

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

load_dotenv()
admin = Admin()
news = News()
variable = PlaceHolder(news)


# Route Starts #

# --- User Part Starts --- #

# Home page Routing #
@app.route("/")
def user():
    return redirect(url_for('IndexFun'))


@app.route("/home")
def IndexFun():
    variable.initiate_variables()
    return render_template("User/index.html")


# Contact page Routing #
@app.route("/contact", methods=['POST', 'GET'])
def contact():
    msgSentStatus, msgStatus = admin.contact_admin()
    return render_template("User/contact.html", msg=msgStatus, msgSent=msgSentStatus)


# Guessing Game page Routing #
@app.route("/NumberGuessing", methods=['POST', 'GET'])
def NumberGuessing_fun():
    variable.generateRandomNumber()
    return render_template("User/GuessingNumber.html", number=variable.randomNum)


# Blog page Routing #
@app.route("/Blog")
def blogIndexFun():
    variable.blogResp = variable.utilityObj.getBlogData()
    return render_template("User/blogindex.html", jobj=variable.blogResp)


@app.route("/Detail_Blog/<int:num>")
def showDetailBlog(num):
    return render_template("User/blog.html", jobj=variable.blogResp, blogNum=num - 1)


# News page Routing #
@app.route("/news/<int:num>")
def newsFun(num):
    news.loadNews(num)
    return render_template("User/news.html", newsData=news.NewsHeader, newsImg=news.NewsImg, newsLink=news.NewsLink,
                           detailedNews=news.detailNews, pageCounter=news.URlNextPage, posCounter=news.counterPos,
                           newsDt=news.Date)

# -- User Part Ends -- #


# -- Admin Part Starts -- #

# Admin Home page #
@app.route("/admin/")
def admin_page():
    return redirect(url_for('admin_home'))


@app.route("/admin/home")
@admin.login_required
def admin_home():
    return render_template("Admin/admin.html")


# Admin Login Page #
@app.route("/admin/login", methods=['POST', 'GET'])
def admin_login_page():
    redirectPage,LoginMsg,showAlert = admin.proceedLogin()
    if redirectPage == "LoginSuccess":
        return redirect(url_for("admin_home"))
    else:
        return render_template(redirectPage,LoginStatus = LoginMsg,show_alert = showAlert)


@app.route("/admin/logout")
def admin_logout():
    #redirectPage,LoginMsg = admin.logOut()
    redirectPage = admin.logOut()
    return redirect(redirectPage)
    #return render_template(redirectPage,LoginStatus = LoginMsg)


# -- Admin Share Market Part starts -- #

#  Stock Average Calculator Page #
@app.route("/admin/avg", methods=['POST', 'GET'])
@admin.login_required
def AvgCalculator():
    isFieldEmpty,Text,FBQ,FBP,SBQ,SBP = shares.CalculateAveragePrice()
    return render_template("Admin/AvgCalculator.html", Fempty=isFieldEmpty, outText=Text,FBQty = FBQ,FBPirce = FBP,SBQty = SBQ,SBPrice = SBP)

#  Stock Investing Page #
@app.route("/admin/sm", methods=['POST', 'GET'])
@admin.login_required
def ShareMarket():
    company = shares.getCompanyList()
    isFieldsEmpty, Text,showAlert = shares.ShareMarketData()
    return render_template("Admin/ShareMarket.html", Fempty=isFieldsEmpty,outText=Text,show_alert = showAlert ,Companies=company)


# -- Share Market Page Ends --#

# -- Admin Part Ends -- #


# Error Page  #
@app.errorhandler(404)
def not_found(e):
    return render_template("error.html")


# Main App #
if __name__ == "__main__":
    app.run(debug=True)
