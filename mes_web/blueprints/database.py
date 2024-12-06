
from flask import Blueprint, request, jsonify
from mysql_api.mysql_database import MySQLDatabase
from mysql_table_model.semikron import LotInfo, Point, Recipe, DbcLinkTray

blue_print = Blueprint("database", __name__, url_prefix="/")


mysql_api = MySQLDatabase("root", "liuwei.520")


def add_new_lot(lot_info):
    mysql_api.add_data(LotInfo, lot_info)


@blue_print.route("/get_lots", methods=["GET"])
def get_lots():
    page = int(request.args.get("page"))  # 获取 page 参数
    limit = int(request.args.get("limit"))  # 获取 limit 参数
    instances = mysql_api.query_data_all(LotInfo)
    lot_list = [instance.as_dict() for instance in instances]
    response_info = {
        "code": 0,
        "count": len(lot_list),
        "data": lot_list[(page - 1) * limit:page * limit]
    }
    return response_info


@blue_print.route("/add_point", methods=["POST"])
def add_point():
    point_info = request.get_json()
    mysql_api.add_data(Point, point_info)
    return jsonify({})


@blue_print.route("/get_points", methods=["GET"])
def get_points():
    page = int(request.args.get("page"))  # 获取 page 参数
    limit = int(request.args.get("limit"))  # 获取 limit 参数
    instances = mysql_api.query_data_all(Point)
    lot_list = [instance.as_dict() for instance in instances]
    response_info = {
        "code": 0,
        "count": len(lot_list),
        "data": lot_list[(page - 1) * limit:page * limit]
    }
    return response_info


@blue_print.route("/get_point_names", methods=["GET"])
def get_point_names():
    instances = mysql_api.query_data_all(Point)
    point_list = [instance.as_dict() for instance in instances]
    point_names = [recipe_info.get("point_name") for recipe_info in point_list]
    return jsonify(point_names)


@blue_print.route("/get_recipes", methods=["GET"])
def get_recipes():
    page = int(request.args.get("page"))  # 获取 page 参数
    limit = int(request.args.get("limit"))  # 获取 limit 参数
    instances = mysql_api.query_data_all(Recipe)
    recipe_list = [instance.as_dict() for instance in instances]
    response_info = {
        "code": 0,
        "count": len(recipe_list),
        "data": recipe_list[(page - 1) * limit:page * limit]
    }
    return response_info


@blue_print.route("/get_recipe_names", methods=["GET"])
def get_recipe_names():
    instances = mysql_api.query_data_all(Recipe)
    recipe_list = [instance.as_dict() for instance in instances]
    recipe_names = [recipe_info.get("recipe_name") for recipe_info in recipe_list]
    return jsonify(recipe_names)


@blue_print.route("/add_recipe", methods=["POST"])
def add_recipe():
    recipe_info = request.get_json()
    print(recipe_info)
    mysql_api.add_data(Recipe, recipe_info)
    return jsonify({})


@blue_print.route("/get_dbc_links", methods=["GET"])
def get_dbc_links():
    page = int(request.args.get("page"))  # 获取 page 参数
    limit = int(request.args.get("limit"))  # 获取 limit 参数
    instances = mysql_api.query_data_all(DbcLinkTray)
    dbc_link_list = [instance.as_dict() for instance in instances]
    response_info = {
        "code": 0,
        "count": len(dbc_link_list),
        "data": dbc_link_list[(page - 1) * limit:page * limit]
    }
    return response_info
