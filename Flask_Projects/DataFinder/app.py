from flask import Flask, render_template, request, redirect, url_for
from forms import FinderForm, VisualiserForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

@app.route("/")
def home():
  return render_template("main.html")

@app.route("/finder", methods=["GET", "POST"])
def finder():
    finder_form = FinderForm(csrf_enabled=False)
    if finder_form.validate_on_submit():
        '''
        new_id = len(recipes)+1
        recipes[new_id] = recipe_form.recipe.data
        types[new_id] = recipe_form.recipe_type.data
        descriptions[new_id] = recipe_form.description.data
        new_ingredients = recipe_form.ingredients.data
        new_instructions = recipe_form.instructions.data
        add_ingredients(new_id, new_ingredients)
        add_instructions(new_id, new_instructions)
        comments[new_id] = []
        '''
        pass
    return render_template("finder.html", template_form=finder_form)

@app.route("/visualiser", methods=["GET", "POST"])
def visualiser():
    visualiser_form = VisualiserForm(csrf_enabled=False)
    if visualiser_form.validate_on_submit():
        '''
        new_comment = comment_form.comment.data
        comments[id].append(new_comment)
        '''
        pass
    return render_template("visualiser.html", template_form=visualiser_form)

app.run()