from bs4 import BeautifulSoup
with open('data.html','r',encoding='utf8')as f:
    ls=f.read()
    soup = BeautifulSoup(ls)
    a=soup.find_all('div',class_='div_question')
    for index,i in enumerate(a):
        b = i.find('div', class_='div_title_question')
        c = i.find_all('li')
        print("%s、%s"%(index+1,b.text.replace('*','')))
        for j in c:
            print('□'+j.text)


