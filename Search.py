import mechanize
from bs4 import BeautifulSoup
import http.cookiejar
from Class import Class

class Search:

    def __init__(self, ra, password):
        self.ra = ra
        self.password = password
        cj = http.cookiejar.CookieJar()
        self.br = mechanize.Browser()
        self.br.set_cookiejar(cj)
        self.br.open("https://sae.cotuca.unicamp.br/")

        self.br.select_form(nr=0)
        self.br.form['usuario'] = ra
        self.br.form['senha'] = 'cotuca unicamp20171'
        self.br.submit()
    
    def get_technician_grade(self):
        self.br.open(f'https://sae.cotuca.unicamp.br/alunos/{self.ra}/boletim?utf8=%E2%9C%93&Ano=2021&curso_aluno=28&commit=Buscar')
        soup = BeautifulSoup(self.br.response().read(), 'html.parser')

        notas_tabela = soup.find_all('table', class_='table table-striped table-bordered')[1]

        linhas = notas_tabela.find_all('tr')

        # exclui linhas desnecessarias
        del linhas[0]
        del linhas[0]

        classes = []

        # 2 -> materia / 4 -> nota
        for linha in linhas:
            sub_linhas = linha.find_all('td')
            classes.append(Class(sub_linhas[2].text, sub_linhas[4].text))

        return classes

    def get_high_school_grade(self):
        self.br.open(f'https://sae.cotuca.unicamp.br/alunos/{self.ra}/boletim?utf8=%E2%9C%93&Ano=2021&curso_aluno=78&commit=Buscar')
        
        soup = BeautifulSoup(self.br.response().read(), 'html.parser')

        notas_tabela = soup.find_all('table', class_='table table-striped table-bordered')[1]

        linhas = notas_tabela.find_all('tr')

        # exclui linhas desnecessarias
        del linhas[0]
        del linhas[0]

        classes = []

        # 2 -> materia / 4 -> nota
        for linha in linhas:
            sub_linhas = linha.find_all('td')

            classes.append(Class(sub_linhas[2].text, sub_linhas[4].text, sub_linhas[5].text, sub_linhas[7].text, sub_linhas[8].text))

        return classes

    


