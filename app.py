from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def home():
    if request.post:
        with open(mode="w", file="data.txt") as file:
            file.write(request.get_data())


    return render_template('index.html')

if __name__ == '__main__':
    app.run()
