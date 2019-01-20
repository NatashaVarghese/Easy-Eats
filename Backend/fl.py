from flask import Flask

ingredients = []


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/Watson/<image>")
def getWatson(image):
    #Natasha code -> Pipe it some how




    return image

@app.route("/MakeRecipe/<foods>")
def AddToRecipe(food):
    if not  (food in ingredients):
        ingredients.append(food)


    return "Success " + str(food)


@app.route("/recipe/")
def getRecipe():
    s=""
    for i in ingredients:
        s+= str(i)+","
    if s != "":
        s[:len(s)-1]
    else:
        pass

    return "Recipe!"



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


