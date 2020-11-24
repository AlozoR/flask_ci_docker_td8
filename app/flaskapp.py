from flask import Flask
from redis import Redis, RedisError

redis = Redis(host="redis-server", db=0)

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Hello World! </h1>"

@app.route('/visit')
def counter_insc():
    try:
        visits = redis.incr("counter")
    except:
        visits = "<i>cannot connect to redis server<i>"
    html = "<h1>Number of visits: {}</h1>".format(visits)
    return html


def main():
    app.run()

if __name__ == "__main__":
    main()
