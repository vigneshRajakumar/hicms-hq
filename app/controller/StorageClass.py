
'''
    This class will retrieve data from the database which inturn is represented
     by the SQL-alchemy classes.
     
'''
from app.model.models import db, Customer, Shops
from flask import session

class StorageClass(object):
    
    def addCustomerTODatabase(self,formData):
        newCustomerData = Customer(formData.customername.data,formData.customeraddress.data,
                                   formData.handphone.data,formData.emailid.data,formData.dateofjoining.data,
                                   formData.passwordcustomer.data)
    
        db.session.add(newCustomerData)
        try:
        	db.session.commit()
        except Exception as e:
        	#log data
        	# this part need to check whether exception works
        	db.session.flush()
        	raise e


    def query_database(self, formData):
    	emailquery = Customer.query.filter_by(email = formData.emailid.data).first()
    	if emailquery:
    		# email already present in database
    		return False
    	else:
    		return True
        # need to check if data is being added to database automatically
        #db.session.flush()
        #db.session.refresh(newCustomerData)
        #db.session.close()
        #return "from StorageClass"

    def addShopTODatabase(self,formData):
        newShopData = Shops(formData.shopId.data, formData.city.data, formData.country.data,
                            formData.address.data, formData.admin.data, formData.contactNumber.data)
        db.session.add(newShopData)
        db.session.commit()

    def shop_query_database(self, formData):
        shopidquery = Shops.query.filter_by(shopId = formData.shopId.data).first()
        if shopidquery:
            return False
        else:
            return True