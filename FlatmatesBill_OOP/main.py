from flat import Bill, Flatmate
from reports import PdfReport

amount_input = float(input("Enter the bill amount: "))
period_input = input("What is the bill period? E.g. December 2021: ")

name1_input = input("Enter your name: ")
days1_input = int(input(f"How many days did {name1_input} stay in the house during the bill period? "))

name2_input = input("Enter the name of the other flatmate: ")
days2_input = int(input(f"How many days did {name2_input} stay in the house during the bill period? "))

the_bill = Bill(amount=amount_input, period=period_input)
the_flatmate1 = Flatmate(name=name1_input, days_in_house=days1_input)
the_flatmate2 = Flatmate(name=name2_input, days_in_house=days2_input)

print(f"{the_flatmate1.name} pays: ", the_flatmate1.pays(bill=the_bill, other_flatmate=the_flatmate2))
print(f"{the_flatmate2.name} pays: ", the_flatmate2.pays(bill=the_bill, other_flatmate=the_flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=the_flatmate1, flatmate2=the_flatmate2, bill=the_bill)
