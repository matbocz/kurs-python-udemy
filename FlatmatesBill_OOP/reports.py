import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their names, their due amounts and the period
    of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        # Create flatmate pay strings
        flatmate1_pay = str(round(flatmate1.pays(bill=bill, other_flatmate=flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill=bill, other_flatmate=flatmate1), 2))

        # Create pdf object and add page
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Insert icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        # Insert period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name label and due amount of the first flatmate
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=20, txt=flatmate1_pay, border=1, ln=1)

        # Insert name label and due amount of the second flatmate
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=20, txt=flatmate2_pay, border=1, ln=1)

        # Change directory to files
        os.chdir("files")

        # Generate pdf file
        pdf.output(self.filename)

        # Open pdf file
        webbrowser.open(self.filename)
