from flask import Flask, jsonify, request
from threading import Thread
from Search import Search

app = Flask('')

@app.route("/")
def initial():
    return jsonify({'message': 'COTUCA API'})

@app.route("/api/grade/technician/<year>/<ra>/<password>")
def get_technician_grade(year, ra, password):
    try:
      s = Search(year, ra, password)

      classes = s.get_technician_grade()

      dict_classes = []

      for _class in classes:
          dict_class = {'Name': _class.getName(), '1º': _class.getFirst(), '2º': _class.getSecond(), '3º': _class.getThird(), '4º': _class.getFourth()}
          dict_classes.append(dict_class)

      return jsonify(dict_classes)
    
    except:
      return jsonify({'message': 'Invalid credentials!'})

@app.route("/api/grade/highSchool/<year>/<ra>/<password>")
def get_high_school_grade(year, ra, password):
    try:
      s = Search(year, ra, password)

      classes = s.get_high_school_grade()

      dict_classes = []

      for _class in classes:
          dict_class = {'Name': _class.getName(), '1º': _class.getFirst(), '2º': _class.getSecond(), '3º': _class.getThird(), '4º': _class.getFourth()}
          dict_classes.append(dict_class)

      return jsonify(dict_classes)
    
    except:
      return jsonify({'message': 'Invalid credentials!'})

def run():
	app.run(host='0.0.0.0',port=8080)

t = Thread(target=run)
t.start()