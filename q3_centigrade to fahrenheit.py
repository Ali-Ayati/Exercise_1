def cent_to_faren(cent: float) -> float: 
    faren = cent * 1.8 + 32
    return faren

cent = float(input("Enter the temperature in Celsius: "))

# نمایش با تمام اعشار
print(cent_to_faren(cent))
# نمایش با دو رقم اعشار
print(f"{cent_to_faren(cent):.2f}")
# نمایش بدون اعشار
print(round(cent_to_faren(cent)))