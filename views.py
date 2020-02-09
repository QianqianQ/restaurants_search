from flask import Blueprint, current_app, request, jsonify

from search_app.utils import check_params_valid, matching_check


bp = Blueprint('bp', __name__, url_prefix='/')


@bp.route("/", methods=["GET"])
def index():
    return jsonify(current_app.config["DATA"])


@bp.route("/restaurants/search", methods=["GET"])
def restaurant_search():
    # get the query parameters
    q = request.args.get("q", type=str)
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)

    # validate the parameters
    check_params_valid(q, lat, lon)

    # requirement settings
    all_restaurants = current_app.config["DATA"]["restaurants"]
    str_query_fields = ["name", "description", "tags"]
    max_distance = 3
    query_loc = [lon, lat]

    # get the list of matched restaurants
    matched_restaurants = list(filter(lambda item: matching_check(item, q, str_query_fields,
                                                                  query_loc, max_distance), all_restaurants))
    return jsonify({"matched_restaurants": matched_restaurants})
