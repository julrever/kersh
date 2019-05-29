from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://vk.com/k_owka')
pic = r.html.find('#page_wall_posts').html.find('a')
for p in pic:
    print(p.attrs['class'])
