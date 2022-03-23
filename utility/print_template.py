import esparto as es

page = es.Page(title='Print form')

header = es.RawHTML(''.join(open('header.html', mode='rt', encoding='utf-8').readlines()))

page.children.append(header)

page.save_html('test.html')
page.save_pdf('test.pdf')
