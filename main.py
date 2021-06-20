import mechanize
from bs4 import BeautifulSoup
import http.cookiejar
from models.Class import Class

ra = '19171'

cj = http.cookiejar.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://sae.cotuca.unicamp.br/")

br.select_form(nr=0)
br.form['usuario'] = ra
br.form['senha'] = 'cotuca unicamp20171'
br.submit()

def get_technician_grade():
    br.open(f'https://sae.cotuca.unicamp.br/alunos/{ra}/boletim?utf8=%E2%9C%93&Ano=2021&curso_aluno=28&commit=Buscar')
    soup = BeautifulSoup(br.response().read(), 'html.parser')

    notas_tabela = soup.find_all('table', class_='table table-striped table-bordered')[1]

    linhas = notas_tabela.find_all('tr')

    # exclui linhas desnecessarias
    del linhas[0]
    del linhas[0]

    classes = []

    # 2 -> materia / 4 -> nota
    for linha in linhas:
        sub_linhas = linha.find_all('td')
        classes.append(Class(sub_linhas[2].text, sub_linhas[4].text).toString())

    return classes

def get_high_school_grade():
    br.open(f'https://sae.cotuca.unicamp.br/alunos/{ra}/boletim?utf8=%E2%9C%93&Ano=2021&curso_aluno=78&commit=Buscar')
    
    soup = BeautifulSoup(br.response().read(), 'html.parser')

    notas_tabela = soup.find_all('table', class_='table table-striped table-bordered')[1]

    linhas = notas_tabela.find_all('tr')

    # exclui linhas desnecessarias
    del linhas[0]
    del linhas[0]

    classes = []

    # 2 -> materia / 4 -> nota
    for linha in linhas:
        sub_linhas = linha.find_all('td')

        classes.append(Class(sub_linhas[2].text, sub_linhas[4].text, sub_linhas[5].text, sub_linhas[7].text, sub_linhas[8].text).toString())

    return classes

print(get_high_school_grade())


