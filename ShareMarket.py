import os

import requests
from datetime import datetime
#from tkinter import *
#from tkinter import ttk
#import messagebox

'''
#
def getDetails():
    sheet_endpoint = "https://api.sheety.co/9185ea913e3a1db7afa05d850171b7af/shareMarket/holdings"

    headerData = {
        "Authorization": "Basic dGhhbmlnYWk6c29sdXRpb25zQDEyMw",
        "Content-Type": "application/json"
    }

    res = requests.get(sheet_endpoint, headers=headerData).json()
    for data in res['holdings'][::-1]:
        if data['companyName'] == compName.get().upper():
            return (data['totalQuantity'],data['totalAmtInvested'],data['newAvgPrice'])
    return (0,0,0)
    #
'''
'''
def loadComapanyNames():
    compNameList = []
    headerData = {
        "Authorization": "Basic dGhhbmlnYWk6c29sdXRpb25zQDEyMw",
        "Content-Type": "application/json"
    }
    holdings_endpoint = "https://api.sheety.co/9185ea913e3a1db7afa05d850171b7af/shareMarket/holdings"

    res = requests.get(holdings_endpoint, headers=headerData).json()
    for company in res['holdings']:
        print(company['companyName'])
        compNameList.append(company['companyName'])

    ScompName['values'] = ['Other'] + [company['companyName'] for company in res['holdings']]
    ScompName.current(0)


def CompanySelected(ev):
    compName.delete(0, END)
    if companyListVar.get() != 'Other':
        compName.insert(0, companyListVar.get())
        buyPrice.focus()

    else:
        compName.focus()
'''




'''
def avgCalculateScreen():
    closeStartingScreen(True)

    LFirstBuy.grid(row=2, column=0, sticky='E')
    FirstBuyPrice.grid(row=2, column=1, pady=10)
    FirstBuyPrice.focus()

    LFirstQty.grid(row=3, column=0, sticky='E')
    CurrQty.grid(row=3, column=1, pady=10)

    LSecondBuy.grid(row=4, column=0, sticky='E')
    SecondBuyPrice.grid(row=4, column=1, pady=10)

    LSecondQty.grid(row=5, column=0, sticky='E')
    NewQty.grid(row=5, column=1, pady=10)

    backBtn.grid(row=6, column=0, pady=10)
    calculateBtn.grid(row=6, column=1, pady=10)

    LAvgRemark.grid(row=7, column=0, columnspan=2, pady=10)
'''

'''
<----Main---->
def CalculateAveragePrice():
    if len(FirstBuyPrice.get()) > 0 and len(SecondBuyPrice.get()) > 0 and len(CurrQty.get()) > 0 and len(NewQty.get()) > 0:
        totAmt = (float(FirstBuyPrice.get()) * float(CurrQty.get())) + (float(SecondBuyPrice.get()) * float(NewQty.get()))
        totQty = (int(CurrQty.get()) + int(NewQty.get()))
        AvgPrice = round(totAmt / totQty, 2)
        LAvgRemark.config(text=f'You have total {totQty} Qty with Avg price of ₹{AvgPrice}')

        FirstBuyPrice.delete(0,END)
        CurrQty.delete(0,END)
        SecondBuyPrice.delete(0,END)
        NewQty.delete(0,END)
        FirstBuyPrice.focus()
    else:
        messagebox.showinfo(title='Status',message='Enter all the Fields to Calculate the Avg Price!')

<----Main---->

'''

'''
def backBtnPressed():
    LFirstBuy.grid_forget()
    FirstBuyPrice.grid_forget()

    LFirstQty.grid_forget()
    CurrQty.grid_forget()

    LSecondBuy.grid_forget()
    SecondBuyPrice.grid_forget()

    LSecondQty.grid_forget()
    NewQty.grid_forget()

    backBtn.grid_forget()
    calculateBtn.grid_forget()

    LAvgRemark.grid_forget()

    closeStartingScreen(False)


def closeStartingScreen(closeScreen):
    if closeScreen:
        LSComp.grid_forget()
        ScompName.grid_forget()
        LComp.grid_forget()
        LBuyPrice.grid_forget()
        LQty.grid_forget()
        compName.grid_forget()
        buyPrice.grid_forget()
        quantity.grid_forget()
        avgCalcBtn.grid_forget()
        saveBtn.grid_forget()
    else:

        LSComp.grid(row=2, column=0, sticky='E')
        ScompName.grid(row=2, column=1, pady=10)
        #loadComapanyNames()

        LComp.grid(row=3, column=0, sticky='E')
        compName.grid(row=3, column=1, pady=10)
        compName.focus()

        LBuyPrice.grid(row=4, column=0, sticky='E')
        buyPrice.grid(row=4, column=1, pady=10)

        LQty.grid(row=5, column=0, sticky='E')
        quantity.grid(row=5, column=1, pady=10)

        avgCalcBtn.grid(row=6, column=0, pady=10)
        saveBtn.grid(row=6, column=1, pady=10)


'''

'''

root = Tk()
root.title("Thanigai's Share Market Info")
root.config(pady=30, padx=60)
activityVar = StringVar()
companyListVar = StringVar()
durationVar = IntVar()
activities = ['Running', 'Yoga']
durationList = ['15', '30', '45', '60']

Label(text='Share Matket', fg='dodgerblue', font=('arial', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

Label(text=datetime.now().strftime('%d-%m-%Y'), fg='red', font=('arial', 12, 'normal')).grid(row=1, column=0,
                                                                                             columnspan=2, pady=10)
#Upload Share Data Part####

LSComp = Label(text='Select Company :', fg='brown', font=('arial', 10, 'bold'))
ScompName = ttk.Combobox(root, textvariable= companyListVar,state='readonly',font=('arial', 10, 'normal'))
ScompName.bind("<<ComboboxSelected>>", CompanySelected)


LComp = Label(text='Enter Company Name :', fg='brown', font=('arial', 10, 'bold'))
compName = Entry(fg='red', font=('arial', 10, 'normal'))


LBuyPrice = Label(text='Enter Buy Price :', fg='brown', font=('arial', 10, 'bold'))
buyPrice = Entry(fg='red', font=('arial', 10, 'normal'))


LQty = Label(text='Enter the Quanity :', fg='brown', font=('arial', 10, 'bold'))
quantity = Entry(fg='red', font=('arial', 10, 'normal'))

avgCalcBtn = Button(text='Average Calculator', font=('arial', 10, 'bold'), width=17, command=avgCalculateScreen)
saveBtn = Button(text='Save', font=('arial', 10, 'bold'), width=15, command=postData)

###Average share price calculator part###

LFirstBuy = Label(text='Enter Current Avg Price :', fg='brown', font=('arial', 10, 'bold'))
FirstBuyPrice = Entry(fg='red', font=('arial', 10, 'normal'))

LFirstQty = Label(text='Enter Current Qty :', fg='brown', font=('arial', 10, 'bold'))
CurrQty = Entry(fg='red', font=('arial', 10, 'normal'))

LSecondBuy = Label(text='Enter New Buy Price :', fg='brown', font=('arial', 10, 'bold'))
SecondBuyPrice = Entry(fg='red', font=('arial', 10, 'normal'))

LSecondQty = Label(text='Enter New Qty :', fg='brown', font=('arial', 10, 'bold'))
NewQty = Entry(fg='red', font=('arial', 10, 'normal'))

backBtn = Button(text='Back', font=('arial', 10, 'bold'), width=15, command=backBtnPressed)
calculateBtn = Button(text='Calculate', font=('arial', 10, 'bold'), width=17, command=CalculateAveragePrice)

LAvgRemark = Label(fg='dodgerblue', font=('arial', 10, 'bold'))

avgCalculateScreen()
root.mainloop()

'''
##### AVG #####

def CalculateAveragePrice(FirstBuyQty,FirstBuyPrice,SecondBuyQty,SecondBuyPrice):
    if len(FirstBuyPrice) > 0 and len(SecondBuyPrice) > 0 and len(FirstBuyQty) > 0 and len(SecondBuyQty) > 0:
        totAmt = (float(FirstBuyPrice) * float(FirstBuyQty)) + (
                    float(SecondBuyPrice) * float(SecondBuyQty))
        totQty = (int(FirstBuyQty) + int(SecondBuyQty))
        AvgPrice = round(totAmt / totQty, 2)
        return False, f'You have total {totQty} Qty with Avg price of  ₹{AvgPrice}'

    else:
        return True , f'Enter all the Fields'


#####  SM  ######


def getCompanyList():
    compNameList = []
    param = {
        "action": "getData"
    }
    holdings_endpoint = os.getenv("SHEET_ENDPOINT")

    res = requests.get(holdings_endpoint, params=param).json()
    for comp in res:
        compNameList.append(comp["CompanyName"])
    return compNameList


def getShareData(CompName):
    sheet_endpoint = os.getenv("SHEET_ENDPOINT")
    param = {
        "action": "getData"
    }
    res = requests.get(sheet_endpoint, params=param).json()
    for comp in res:
        if comp["CompanyName"] == CompName.upper():
            return (comp["Quantity"], comp["AmtInvested"], comp["AvgPrice"], comp["rowID"], True)
    return (0, 0, 0, 0, False)


def updateShareData(avgprice, quantity, amtInvested, rowID, companyPresent,Company,fullySold):
    if companyPresent:
        if not fullySold:
            holdings_endpoint = os.getenv("SHEET_ENDPOINT")
            param = {
                "action": "updateHolding"
            }

            holding = {
                "AvgPrice": avgprice,
                "Quantity": quantity,
                "AmtInvested": amtInvested,
                "rowID": rowID + 2
            }

            return requests.post(holdings_endpoint, params=param, json=holding).text
        else:

            holdings_endpoint = os.getenv("SHEET_ENDPOINT")
            param = {
                "action": "deleteHolding"
            }

            holding = {
                "rowID": rowID + 2
            }
            return requests.post(holdings_endpoint, params=param, json=holding).text





    else:
        holdings_endpoint = os.getenv("SHEET_ENDPOINT")

        param ={
          "action" : "writeHolding"
        }

        holding = {
                "CompanyName": Company.upper(),
                "AvgPrice": avgprice,
                "Quantity": quantity,
                "AmtInvested": amtInvested
        }
        return requests.post(holdings_endpoint, params=param,json=holding).text



def postData(Bqty,Bprice,CompanyName,ordertype):

    heldQty, totAmt, avpprice, rowID, isCompanyPresent = getShareData(CompanyName)
    fullySold = False

    if ordertype == "Buy":
        totQty = float(heldQty) + float(Bqty)
        amtInvested = round(float(Bprice), 2) * float(Bqty)
        totAmtInvested = float(amtInvested) + float(totAmt)
        newAvgPrice = round(totAmtInvested / totQty, 2)
    else:
        totQty = float(heldQty) - float(Bqty)
        amtInvested = (round(float(Bprice), 2) * float(Bqty)) * -1
        totAmtInvested = float(totAmt) + float(amtInvested)
        newAvgPrice = avpprice
        Bqty = str(int(Bqty) * -1)
        if totQty == 0:
            fullySold = True
            newAvgPrice = 0

    shareData_endpoint = os.getenv("SHEET_ENDPOINT")

    shareDatum = {
        "Date": datetime.now().strftime("%d/%m/%Y"),
        "OrderType": ordertype,
        "CompanyName": CompanyName.upper(),
        "PrevAvgPrice": avpprice,
        "HeldQuantity": heldQty,
        "BuyPrice": round(float(Bprice), 2),
        "BuyQuantity": int(Bqty),
        "AmtInvested": amtInvested,
        "NewAvgPrice": newAvgPrice,
        "TotalQuantity": totQty,
        "TotalAmtInvested": totAmtInvested
    }
    param = {
        "action": "writeData"
    }

    res = requests.post(shareData_endpoint, params=param, json=shareDatum)
    if res.text == "Success":
        if updateShareData(newAvgPrice, totQty, totAmtInvested, rowID, isCompanyPresent,CompanyName,fullySold) == "Success":
           return "Data Saved Successfully!"
        return  "Share Data Saved! Holding Data Not Saved!!"

    else:
        return 'Oops Something Went Wrong, Try again!'

def ShareMarketData(BuyQty,BuyPrice,CompanyName,ordertype):

    if len(BuyQty) > 0 and len(BuyPrice) > 0 and len(CompanyName) > 0:
        return False,  postData(BuyQty,BuyPrice,CompanyName,ordertype)
    else:
        return True , f"Enter all the Fields"

