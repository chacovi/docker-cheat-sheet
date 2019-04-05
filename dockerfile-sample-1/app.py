from flask import Flask
import redis

cache = redis.Redis(host="redis", port=6379, db=0)
cache.set("counter", 0)

app = Flask(__name__)

@app.route("/")
def hello():
  cache.incr("counter")
  return "Visita numero = {0} ".format(cache.get("counter"))

if __name__ == '__main__':
    app.run(host='0.0.0.0')