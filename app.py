from flask import Flask, render_template, request

currentSpeed = "0"

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        global currentSpeed
        currentSpeed = str(request.data)[1:]
        print(currentSpeed)
        # with open(mode="w", file="data.txt") as file:
        #     file.write(str(request.data))
        
        
    return render_template("index.html", speed=currentSpeed)
   

if __name__ == '__main__':
    app.run()
