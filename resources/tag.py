from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import StoreModel, TagModel
from schemas import TagSchema

blp = Blueprint("Tags", "tags", description="Operations on tags")

@blp.route("/store<store_id>/tags")
class TagsInStore(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store.tags.all()
    @blp.arguments(TagSchema)
    @blp.response(201, TagSchema)
    def post(self, tag_data, store_id):
        if TagModel.query.filter_by(TagModel.store_id == store_id,TagModel.name==tag_data["name"]).first():
            abort(400, "Tag already exists")
        tag = TagModel(**tag_data, store_id=store_id)
        
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))
            
        return tag
    
    
@blp.route("/tag/<tag_id>")
class Tags(MethodView):
    @blp.response(200, TagSchema)
    def get(self, tag_id):
        return TagModel.query.get_or_404(tag_id)
    