def vat(totalprice):
   result=totalprice+ (totalprice*7/100)
   return result
x = int(input())
print(vat(x))