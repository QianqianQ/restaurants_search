import re

from flask import abort
from math import sin, cos, sqrt, atan2, radians


def check_params_valid(query_string, latitude, longitude):
    """
    Check whether the query parameters are valid
    :param query_string: str
    :param latitude: float
    :param longitude: float
    :raises 400 HTTPException if the query parameters are invalid
    """
    valid = True

    error_message = "Invalid query parameters: "
    if query_string is None or len(query_string) < 1:
        error_message += "Please provide a valid query string with a minimum length of one character. "
        valid = False
    if latitude is None or latitude > 90 or latitude < -90:
        error_message += "Please provide a valid latitude value between -90 and +90. "
        valid = False
    if longitude is None or longitude > 180 or longitude < -180:
        error_message += "Please provide a valid longitude value between -180 and +180. "
        valid = False
    
    if not valid:
        abort(400, error_message)


def haversine_distance(origin, destination):
    """
    Calculate the Haversine distance.
    :param origin: list of float [long, lat]
    :param destination: list of float [long, lat]
    :return: distance (in km)
    :rtype: float
    :raise TypeError: if origin or destination is not a list
    """
    if not isinstance(origin, list) or not isinstance(destination, list):
        raise TypeError("Only lists are supported as arguments")

    radius = 6371  # km
    lon1, lat1 = origin
    lon2, lat2 = destination
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius * c
    return distance


def matching_check(item_checked, query_str, str_query_fields, origin_loc, distance_threshold):
    """
    :param dict item_checked: the item (restaurant) being checked
    :param str query_str: a minimum length is one character
    :param list str_query_fields: the fields where the query_string is searched from
    :param list origin_loc: list of float [long, lat], the original location
    :param float distance_threshold: threshold of the maximum distance of a matching item (in km)
    :return: whether_match, whether the item matches the query requirements
    :rtype bool
    """
    whether_match = False  # init flag

    # check whether matches the query string
    for field in str_query_fields:
        value = item_checked.get(field)
        if not value:  # here if the field not in the dict, continue
            continue
        # string matching, here if an error is raised, then continue
        try:
            if isinstance(value, str):
                if re.search(query_str, value, re.IGNORECASE):
                    whether_match = True
                    # print(item_checked["name"], "field", field, item_checked[field], "matches")
                    break
            elif isinstance(item_checked[field], list):
                for v in value:
                    if re.search(query_str, v, re.IGNORECASE):
                        whether_match = True
                        # print(item_checked["name"], "field", field, item_checked[field], "matches")
                        break
                if whether_match:
                    break
            # elif  # maybe some other types
        except:
            continue

    # if matches query string, check the distance
    if whether_match:
        if not item_checked.get("location"):
            whether_match = False
            return whether_match

        distance = haversine_distance(origin_loc, item_checked['location'])
        # distance = geopy.distance.great_circle(tuple(origin_loc[::-1]),
        #                                        tuple(item_checked['location'][::-1])).kilometers  # use geopy package
        if distance > distance_threshold:
            whether_match = False

    return whether_match


