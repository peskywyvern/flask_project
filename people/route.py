from flask import Blueprint, Response, jsonify, request
from people_methods import get_people, to_json

people = Blueprint("people", __name__)


@people.route('/people')
def get_people_():
    ppl = get_people()
    country = request.args.get('country')
    if country is not None:
        return jsonify([p for p in ppl['people'] if p['country'] == country])
    return jsonify(ppl['people'])


@people.route('/people', methods=['POST'])
def post_people():
    ppl = get_people()
    person = request.get_json()
    person_id = len(ppl['people'])
    ppl['people'].append({"id": person_id, **person})
    to_json(ppl)
    return jsonify({"id": person_id})


@people.route("/people/<id>")
def get_person(id):
    ppl = get_people()
    try:
        return ppl['people'][int(id)]
    except IndexError:
        return Response('Not found', status=404)


@people.route("/people/<id>", methods=['DELETE'])
def delete_person(id):
    ppl = get_people()
    try:
        ppl['people'][int(id)] = None
        to_json(ppl)
        return Response(status=204)
    except IndexError:
        return Response('Not Found', status=404)


@people.route('/people/<id>', methods=['PATCH'])
def update_person(id):
    ppl = get_people()
    try:
        ppl['people'][int(id)].update(request.get_json())
        to_json(ppl)
        return Response(status=204)
    except IndexError:
        return Response("Not Found", status=404)
