from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

md_path = Path('CV_Enrico_Magazzino.md')
pdf_path = Path('CV_Enrico_Magazzino.pdf')
text = md_path.read_text(encoding='utf-8')

styles = getSampleStyleSheet()
styles['Title'].fontName = 'Helvetica-Bold'
styles['Title'].fontSize = 18
styles['Title'].leading = 22
styles['Title'].textColor = colors.HexColor('#0f1410')
styles['Title'].spaceAfter = 12

styles['Heading2'].fontName = 'Helvetica-Bold'
styles['Heading2'].fontSize = 13
styles['Heading2'].leading = 16
styles['Heading2'].textColor = colors.HexColor('#5e7a45')
styles['Heading2'].spaceAfter = 8

styles['BodyText'].fontName = 'Helvetica'
styles['BodyText'].fontSize = 10.5
styles['BodyText'].leading = 13
styles['BodyText'].textColor = colors.HexColor('#222222')
styles['BodyText'].spaceAfter = 6

story = []
for line in text.splitlines():
    if not line.strip():
        if story and not isinstance(story[-1], Spacer):
            story.append(Spacer(1, 6))
        continue
    if line.startswith('# '):
        story.append(Paragraph(line[2:].strip(), styles['Title']))
    elif line.startswith('## '):
        story.append(Paragraph(line[3:].strip(), styles['Heading2']))
    elif line.startswith('### '):
        story.append(Paragraph(line[4:].strip(), styles['Heading2']))
    elif line.startswith('- '):
        story.append(Paragraph('• ' + line[2:].strip(), styles['BodyText']))
    else:
        story.append(Paragraph(line, styles['BodyText']))

doc = SimpleDocTemplate(str(pdf_path), pagesize=A4, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
doc.build(story)
print(f'Created {pdf_path.name}')
