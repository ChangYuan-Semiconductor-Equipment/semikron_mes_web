from flask import Blueprint, request, render_template

blue_print = Blueprint("dbc_link", __name__)


# 配方管理页面
@blue_print.route("/dbc_link_list", methods=["GET", "POST"])
def dbc_link_list():
    if request.method == "GET":
        return render_template("cyg_dbc_link_list.html")
