import json
from flask import Blueprint, request, jsonify, render_template

from mes_web.blueprints.database import add_new_lot
from mes_web.utils.socket_common import client_send

blue_print = Blueprint("lot", __name__)


# 当前工单页面
@blue_print.route("/current_lot", methods=["GET", "POST"])
def current_lot():
    if request.method == "GET":
        request_flag = {"current_lot": ""}
        current_lot_info = client_send(json.dumps(request_flag))
        return render_template("cyg_current_lot.html", **current_lot_info)


# 工单列表页面
@blue_print.route("/lot_list", methods=["GET", "POST"])
def lot_list():
    if request.method == "GET":
        return render_template("cyg_lot_list.html")


# 点击新建工单按钮
@blue_print.route("/submit_new_lot", methods=["POST"])
def submit_new_lot():
    form_data_dict = request.get_json()
    response = client_send(json.dumps({"new_lot": form_data_dict}))
    if response.get("code") == 200:
        form_data_dict.update({"recipe_name": response.get("current_recipe_name", "")})
        add_new_lot(form_data_dict)

    return jsonify(response)


@blue_print.route("/submit_end_lot", methods=["POST"])
def submit_end_lot():
    form_data_dict = request.get_json()
    response = client_send(json.dumps({"end_lot": form_data_dict}))
    return jsonify(response)


@blue_print.route("/submit_clear_signal", methods=["POST"])
def submit_clear_signal():
    client_send(json.dumps({"clear_signal": ""}))
    return jsonify({})
