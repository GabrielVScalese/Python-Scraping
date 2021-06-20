from flask import Flask, jsonify, request
import json
from Search import Search

app = Flask(__name__)

@app.route("/")
def initial():
    return jsonify({'message': 'API running!'})

# @app.route("/api/grade/technician/<ra>/<password>")
# def get_technician_grade(ra, password):
#     s = Search(ra, password)

#     classes = s.get_technician_grade()

#     dict_classes = []

#     for _class in classes:
#         dict_class = {'Name': _class.getName(), 'First': _class.getFirst(), 'Second': _class.getSecond(), 'Third': _class.getThird(), 'Fourth': _class.getFourth()}
#         dict_classes.append(dict_class)

#     return jsonify(dict_classes)

@app.route("/api/grade/highSchool/<ra>/<password>")
def get_high_school_grade(ra, password):
    s = Search(ra, password)

    classes = s.get_high_school_grade()

    dict_classes = []

    for _class in classes:
        dict_class = {'Name': _class.getName(), 'First': _class.getFirst(), 'Second': _class.getSecond(), 'Third': _class.getThird(), 'Fourth': _class.getFourth()}
        dict_classes.append(dict_class)

    return jsonify(dict_classes)

app.run()