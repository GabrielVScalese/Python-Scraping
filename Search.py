import mechanize
from bs4 import BeautifulSoup
import http.cookiejar
from Class import Class

class Search:

    def __init__(self, year, ra, password):
        self.year = year
        self.ra = ra
        self.password = password
        cj = http.cookiejar.CookieJar()
        self.br = mechanize.Browser()
        self.br.set_cookiejar(cj)
        self.br.open("https://sae.cotuca.unicamp.br/")

        self.br.select_form(nr=0)
        self.br.form['usuario'] = ra
        self.br.form['senha'] = password
        self.br.submit()
    
    def get_grades (self, courseCode):
      self.br.open(f'https://sae.cotuca.unicamp.br/alunos/{self.ra}/boletim?utf8=%E2%9C%93&Ano={self.year}&curso_aluno={courseCode}&commit=Buscar')

      soup = BeautifulSoup(self.br.response().read(), 'html.parser')

      grade_table = soup.find_all('table', class_='table table-striped table-bordered')[1]

      lines = grade_table.find_all('tr')

      del lines[0]
      del lines[0]

      classes = []

      # 2 -> name / 4 -> grade
      for line in lines:
        sub_lines = line.find_all('td')

        classes.append(Class(sub_lines[2].text.strip(), sub_lines[4].text, sub_lines[5].text, sub_lines[8].text, sub_lines[9].text))

      return classes 
    
    def get_technician_grade(self):
      return self.get_grades(28)

    def get_high_school_grade(self):
      return self.get_grades(78)