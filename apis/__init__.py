from flask import Blueprint

bp = Blueprint('api', __name__)

from apis import api
