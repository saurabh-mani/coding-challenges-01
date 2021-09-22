'''
Title: Find the Discount 

Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

Examples

dis(1500, 50) ➞ 750
dis(89, 20) ➞ 71.2
dis(100, 75) ➞ 25

Notes

Your answer should be rounded to two decimal places.

'''

def dis(price,discount):
    discountAmt = (price*discount)/100
    return round((price-discountAmt),2)
price = float(input("Enter Price: "))
discount = float(input("Enter Discount: "))
print("Discounted Price is "+str(dis(price,discount)))
