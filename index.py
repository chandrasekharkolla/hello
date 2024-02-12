from flask import Flask
helloworld = Flask(__name__)
@helloworld.route("/hello")
def run():
    return "{\"message\":\"Hey there python\"}"

if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("80"), debug=True)