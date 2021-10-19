value = input("Type the value you want to get a VAT from: ")

vat = (float(value)/100)*23

print(f"The VAT from {value}zł totals {round(vat,2)}zł")