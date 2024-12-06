from flask import Blueprint, request, render_template

blue_print = Blueprint("point", __name__)


# 点位管理页面
@blue_print.route("/point_list", methods=["GET", "POST"])
def point_list():
    if request.method == "GET":
        return render_template("cyg_point_list.html")
