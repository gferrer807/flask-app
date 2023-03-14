from flask import Blueprint

test_route = Blueprint("test_route", __name__)

@test_route.route("/test")
def test():
    return "Hello, this is a test route!"