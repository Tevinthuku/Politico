"""All views pertaining to parties"""

from flask import jsonify, request, make_response, abort

from app.api.v1 import path_1
from app.api.v1.models.parties import PartiesModel, PARTIES

from app.api.utils import is_valid_string, response_fn
from app.api.v1.utils import get_all_items, get_specific_item


@path_1.route("/parties", methods=['GET'])
def get_all_parties():
    """
        This function gives access to the functionality
        of returning all parties from the list of parties
    """
    return response_fn(200, "data", get_all_items(PartiesModel, "party"))


@path_1.route("/parties", methods=["POST"])
def create_party():
    """
        This function gives access to the functionality of
        creating a new party based on the payload provided
        in the body.
    """
    try:
        data = request.get_json()
        name = data['name']
        logoUrl = data['logoUrl']
    except:
        return response_fn(400, "error", 'Check your json keys. Should be '
                           'name and logoUrl')

    if(not is_valid_string(name)):
        return response_fn(400, "error", 'The logoUrl and namefields are '
                           'present, but they are not valid')

    party = PartiesModel(
        name=name, logoUrl=logoUrl)
    party.save_party()

    return response_fn(201, "data", [{"id": len(PARTIES) - 1,
                                      "name": name, "logoUrl": logoUrl}])


@path_1.route("/parties/<int:party_id>", methods=["GET"])
def get_party(party_id):
    """
        This function provides access to the functionality of returning
        a party whose ID matches the one provided in the
        url
    """
    party = get_specific_item(PartiesModel, "party", party_id)
    if party:
        return response_fn(200, "data", party)
    return response_fn(404, "error", "This party cannot be found")


@path_1.route("/parties/<int:party_id>/name", methods=["PATCH"])
def update_party(party_id):
    """
     This function provides access to the update
     functionality where a party whose id matches
     the id provided in the url gets updated with
     the name provided in the payload
    """
    try:
        data = request.get_json()
        name = data["name"]
    except:
        return response_fn(400, "error", "name not found")
    if(not is_valid_string(name)):

        return response_fn(400, "error", "name is present, but its not valid")
    try:
        party = PartiesModel.get_party_object(party_id)[0]
    except IndexError:
        return response_fn(404, "data", "This party doesn't exist")
    party.setname(name)
    return response_fn(200, "data", [{
        "id": party_id,
        "name": name
    }])


@path_1.route("/parties/<int:party_id>", methods=['DELETE'])
def delete_party(party_id):
    """
        This function provides access to the functionality
        of deleting a party based on the ID provided.
    """
    party = PartiesModel.deleteparty(party_id)
    if party:
        return response_fn(200, "data", "Deleted successfully")
    return response_fn(404, "data", "This party doesn't exist")
