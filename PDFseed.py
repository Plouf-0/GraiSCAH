from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table, TableStyle
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, PageBreak, PageTemplate, Spacer, FrameBreak, NextPageTemplate, Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER,TA_LEFT,TA_RIGHT

from datetime import datetime

from cstecouleur import *

######################################################

class Entete:

    def __init__(self, indication, nom_graine, jour):
        self.indication = indication
        self.nom_graine = nom_graine
        self.jour = jour


class Actividades:

    def __init__(self, categorie, nom, couleur, quantite, descendance, annee, mois):
        self.categorie = categorie
        self.nom = nom
        self.couleur = couleur
        self.quantite = quantite
        self.descendance = descendance
        self.annee = annee
        self.mois = mois
        

class PDFReport:

    def __init__(self, filename):
        self.filename = filename

def generate_seed_pdf(data):

    csort = 'TRIE'
    entete = Entete('Trié en fonction de', '%s' %csort , datetime.now().strftime('%d/%m/%Y'))

    file_name = 'Inventaire du %s.pdf' %datetime.now().strftime('%d.%m.%Y;%S')
    document_title = 'Inventaire De La Grainotheque SCAH'
    title = 'Inventaire De La Grainotheque SCAH'
    indication = entete.indication
    nom_graine = entete.nom_graine
    date_jour = entete.jour


    canvas = Canvas(file_name, pagesize=landscape(letter))

    doc = BaseDocTemplate(file_name, title = (''))
    contents =[]
    width,height = A4

    left_header_frame = Frame(0.2*inch, height-1.2*inch, 2*inch, 1*inch)

    right_header_frame = Frame(2.2*inch, height-1.2*inch, width-2.5*inch, 1*inch,id='normal')

    frame_later = Frame(0.2*inch, 0.6*inch, (width-0.6*inch)+0.17*inch, height-1*inch, leftPadding = 0, topPadding=0, showBoundary = 1, id='col')

    frame_table= Frame(0.2*inch, 0.7*inch, (width-0.6*inch)+0.17*inch, height-2*inch, leftPadding = 0, topPadding=0, showBoundary = 1, id='col')

    laterpages = PageTemplate(id='laterpages',frames=[frame_later])

    firstpage = PageTemplate(id='firstpage',frames=[left_header_frame, right_header_frame,frame_table],)

    contents.append(NextPageTemplate('firstpage'))
    logoleft = Image('LOGO_SCAH_OFFICIEL_2014-1_avec_titre.jpg')
    logoleft._restrictSize(1.5*inch, 1.5*inch)
    logoleft.hAlign = 'CENTER'
    logoleft.vAlign = 'CENTER'

    contents.append(logoleft)
    contents.append(FrameBreak())
    styleSheet = getSampleStyleSheet()
    style_title = styleSheet['Heading1']
    style_title.fontSize = 20 
    style_title.fontName = 'Helvetica-Bold'
    style_title.alignment=TA_CENTER

    style_data = styleSheet['Normal']
    style_data.fontSize = 16 
    style_data.fontName = 'Helvetica'
    style_data.alignment=TA_CENTER

    style_date = styleSheet['Normal']
    style_date.fontSize = 14
    style_date.fontName = 'Helvetica'
    style_date.alignment=TA_CENTER

    canvas.setTitle(document_title)

    contents.append(Paragraph(title, style_title))
    contents.append(Paragraph(indication + ': ' + nom_graine, style_data))
    contents.append(Paragraph(date_jour, style_date))
    contents.append(FrameBreak())

    title_background = colors.HexColor(orange_claire)
    if data == None:
        data = []
    head = [['Catégorie', 'Nom', 'Couleur', 'Quantité', 'Descendance', 'Année\nde\nrécolte', 'Mois\nde\nplantation']]
    data = head + data
    
    for i in range(len(data)):
        

        #data.append([i, i, i, i, i, i, i])

        tableau = Table(data, colWidths=72, rowHeights=40, repeatRows=1)
        tblStyle = TableStyle([('BACKGROUND', (0, 0), (-1, 0), title_background), ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor(noir)), ('ALIGN', (1, 0), (1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 1, colors.HexColor(noir))])

        rowNumb = len(data)
        for row in range(1, rowNumb):
            if row % 2 == 0:
                table_background = colors.HexColor(vert_tclaire)
            else:
                table_background = colors.HexColor(vert_mclaire)

            tblStyle.add('BACKGROUND', (0, row), (-1, row), table_background)

        tableau.setStyle(tblStyle)
        
    #print(data)
    contents.append(NextPageTemplate('laterpages'))
    contents.append(tableau)

    contents.append(PageBreak())

    doc.addPageTemplates([firstpage,laterpages])

    doc.build(contents)

