import pdfkit
# 有下面3中途径生产pdf
options = {
 'page-size': 'Letter',
 'margin-top': '0.75in',
 'margin-right': '0.75in',
 'margin-bottom': '0.75in',
 'margin-left': '0.75in',
 'encoding': "UTF-8",
 'no-outline': None
 }
path_wk = r'C:/软件/Python/Python37/Lib/site-packages/wkhtmltox/bin/wkhtmltopdf.exe' #安装位置
config = pdfkit.configuration(wkhtmltopdf = path_wk)


pdfkit.from_file('C:/Users/Administrator/Desktop/票房网/cloud.html', 'C:/a/output.pdf',configuration=config)

