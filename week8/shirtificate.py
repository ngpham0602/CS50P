from fpdf import FPDF

user = input("Enter your full name (Max 23 Characters): ")
if len(user) > 23:
    print("Input too long, try something shorter!")
else:
    text = f"{user} took CS50"
    pdf = FPDF(orientation="P", format="A4", unit="mm")
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=36)
    pdf.cell(0, 50, "CS50 Shirtificate", align='C', ln=True)
    pdf.image("shirtificate.png", x=5, y=65, w=200, h=197)
    pdf.set_font("Arial", size=30)
    pdf.set_text_color(255, 255, 255)
    text_width = pdf.get_string_width(user)
    if text_width > 90:    
        pdf.cell(w=0, h=150, txt=user, align="C", ln=True)
        pdf.cell(w=0, h=-120, txt="took CS50", ln=True, align="C")
    else:
        pdf.cell(0, 150, txt=text, align="C", ln=True)
    pdf.output("test.pdf")   

