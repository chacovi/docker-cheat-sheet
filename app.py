from flask import Flask
from multiprocessing import Value

counter = Value('i', 0)

app = Flask(__name__)

@app.route("/")
def hello():
  with counter.get_lock():
    counter.value += 1

  return "Visita numero = {0} ".format(counter.value)

if __name__ == '__main__':
  app.run(host='0.0.0.0')