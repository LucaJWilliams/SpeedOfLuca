from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        with open(mode="w", file="data.txt") as file:
            file.write(str(request.data))


    return render_template('index.html')

if __name__ == '__main__':
    app.run()
