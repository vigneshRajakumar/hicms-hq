from Command import Command
from StorageClass import StorageClass
from Feedback import Feedback

class AddShop(Command):
    def __init__(self):
        self.storageObject = StorageClass()
        self.feedbackObject = Feedback()

    def execute(self,formData):

        if self.__check_database(formData):

            self.storageObject.addShopTODatabase(formData)
            self.feedbackObject.setinfo("Success: data added ")
            self.feedbackObject.setdata(formData.shopId.data)
            self.feedbackObject.setcommandtype("AddShop")

        return self.feedbackObject

    def __check_database(self, formData):
        return self.storageObject.shop_query_database(formData)

class ViewShops(Command):
    def __init__(self):
        self.storageObject = StorageClass()

    def execute(self, formData):
        return self.get_shops()

    def get_shops(self):
        return self.storageObject.get_shops_from_db()

        