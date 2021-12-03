from jinja2 import Environment, FileSystemLoader
import json, pdfkit

env = Environment(loader=FileSystemLoader("templates/template_pdf"))
template = env.get_template("temp.html")
user ={
    'id':'1',
    'username': '1724496623',
    'firstname': 'Benjamin',
    'lastname': 'Saltos',
    'career': 'Minas',
    'photo':'u'

}
html = template.render(user)
print(html)