#1. import modules
import reportlab as rp
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

#2. ata
DATA = [ #uppercase
['Date', 'Name', 'Subscription', 'Price (€)'],
['16/11/2025', 'Python Developer', 'Lifetime', '500'],
[ "16/11/2020", "coding Classes: Live Session", "6 months", "9,999.00/-"],
[ "Sub Total", "", "", "208.00/-"],
[ "Discount", "", "", "-30.00/-"],
[ "Total", "", "", "178.00/-"],
]

#3 . Base document tamplate 
pdf = SimpleDocTemplate('receipt.pdf', pagesize = A4)
styles = getSampleStyleSheet()

#4. Getting the style of the top-level heading (Heading1)
title_style = styles['Heading1'] #defoult style

# 5. 0: left, 1: center, 2: right
title_style.alignment = 1  # title center

#6. Create the paragraphÑ
title = Paragraph('Receipt', title_style)

#7. create a table style
style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
    ]
)

# 8. create a table object and pass the style to it
table = Table(DATA, style=style)

# 9. Create PDF
pdf.build([title, table])
