import os
import requests
from datetime import datetime
from flask import request


##### AVG #####

def CalculateAveragePrice():
    if request.method == 'POST':
        FirstBuyQty = request.form['FirstBuyQty']
        FirstBuyPrice = request.form['FirstBuyPrice']
        SecondBuyQty = request.form['SecondBuyQty']
        SecondBuyPrice = request.form['SecondBuyPrice']

        if len(FirstBuyPrice) > 0 and len(SecondBuyPrice) > 0 and len(FirstBuyQty) > 0 and len(SecondBuyQty) > 0:
            totAmt = (float(FirstBuyPrice) * float(FirstBuyQty)) + (
                    float(SecondBuyPrice) * float(SecondBuyQty))
            totQty = (int(FirstBuyQty) + int(SecondBuyQty))
            AvgPrice = round(totAmt / totQty, 2)
            return False, f'You have total {totQty} Qty with Avg price of  ₹{AvgPrice}',FirstBuyQty, FirstBuyPrice, SecondBuyQty, SecondBuyPrice

        else:
            return True, f'Enter all the Fields',FirstBuyQty, FirstBuyPrice, SecondBuyQty, SecondBuyPrice
    else:
        return None,"","","","",""


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


def ShareMarketData():
    if request.method == 'POST':
        ordertype = request.form['ActionList']
        CompanyName = request.form['CompanyName']
        BuyQty = request.form['BuyQty']
        BuyPrice = request.form['BuyPrice']
        if len(BuyQty) > 0 and len(BuyPrice) > 0 and len(CompanyName) > 0:
            return False, postData(BuyQty, BuyPrice, CompanyName, ordertype),True
        else:
            return True, f"Enter all the Fields",True
    else:
        return None,"",False




