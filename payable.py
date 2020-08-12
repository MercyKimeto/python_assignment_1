'''Company= Computer pride
Amount= 30,000
VAT= 16%
'''
def Customer_payment():
    Pay= eval(input("Enter amount"))
    VAT= eval(input("Enter VAT"))
    return Pay,VAT

def VAT_calculator(data):
    return data[0]*(data[1]/100)
print(Customer_payment())
Amount= VAT_calculator(Customer_payment())
print(float(Amount))
