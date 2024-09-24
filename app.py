from flask import Flask,request,render_template


app= Flask(__name__)

@app.route('/')

def welcome():
    return "Welcome to Flask"

@obj.route('/cal',method=["GET"])
def main_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    if operation=="add":
        result=number1+number2
    elif peration=="multiply":
        result=number1*number2
    elif peration=="divide":
         result=number1/number2
    else:
        result=number1-number2
    retuen result

    
print(__name__)
if __name__ == '__main__':
    app.run()

