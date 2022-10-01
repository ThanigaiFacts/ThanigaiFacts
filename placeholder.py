import utility


class PlaceHolder():
    def __init__(self, news):
        self.val = 0
        self.randomNum = 5  # some random number
        self.blogResp = None
        self.utilityObj = utility
        self.newsObj = news
        # self.newsDataCounter = {}

    def initiate_variables(self):
        # self.newsDataCounter = {}
        self.newsObj.clearData()
        #self.randomNum = utility.randomNumberGenerator()

    def generateRandomNumber(self):
        self.randomNum = self.utilityObj.randomNumberGenerator()
