from flask import render_template
from flask import jsonify
from app import app
from .db_utils import per_request_connection_select_query, build_dict, SCIFI, HORROR, COMEDY, ACTION, DRAMA

@app.route('/')
def index():
    return render_template("movies.html")

@app.route('/SCIFI')
def scifi():
    db_query = per_request_connection_select_query(SCIFI)
    dict_data = build_dict(db_query)
    return jsonify(dict_data)

@app.route('/DRAMA')
def drama():
    db_query = per_request_connection_select_query(DRAMA)
    dict_data = build_dict(db_query)
    return jsonify(dict_data)

@app.route('/ACTION')
def action():
    db_query = per_request_connection_select_query(ACTION)
    dict_data = build_dict(db_query)
    return jsonify(dict_data)

@app.route('/HORROR')
def horror():
    db_query = per_request_connection_select_query(HORROR)
    dict_data = build_dict(db_query)
    return jsonify(dict_data)

@app.route('/COMEDY')
def comedy():
    db_query = per_request_connection_select_query(COMEDY)
    dict_data = build_dict(db_query)
    return jsonify(dict_data)
