from flask import Blueprint, request, render_template

blue_print = Blueprint("recipe", __name__)


# 配方管理页面
@blue_print.route("/recipe_list", methods=["GET", "POST"])
def recipe_list():
    if request.method == "GET":
        return render_template("cyg_recipe_list.html")
