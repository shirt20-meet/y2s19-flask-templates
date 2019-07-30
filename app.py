from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return "pasta"


@app.route('/shir')
def home_page2():
    favoriteFoods=["pasta", "peach", "salad", "sushi"]
    opposite_day=True
    return render_template('index.html', food=favoriteFoods, leastFavFoods=opposite_day)


if __name__ == '__main__':
   app.run(debug = True)
