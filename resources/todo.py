from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from db import db
from models.todo import TodoModel
from schemas import TodoSchema, TodoUpdateSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


blp = Blueprint("todo", __name__, description="Operations on todos")



@blp.route("/todo/<int:todo_id>")
class Todo(MethodView):
    @blp.response(200, TodoSchema)
    def get(self, todo_id):
        todo = TodoModel.query.get_or_404(todo_id)
        return todo
    
    @jwt_required(fresh=True)
    def delete(self, todo_id):
        todo = TodoModel.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return {"message": "Todo Deleted."}
    
    @jwt_required()
    @blp.arguments(TodoUpdateSchema)
    @blp.response(200, TodoSchema)
    def put(self, todo_data, todo_id):
        todo = TodoModel.query.get(todo_id)
        if todo:
            todo.status = todo_data["status"]
        else:
            todo = TodoModel(id=todo_id, **todo_data)
        db.session.add(todo)
        db.session.commit()
        return todo


@blp.route("/todo")
class TodoList(MethodView):
    @blp.response(200, TodoSchema(many=True))
    def get(self):
        return TodoModel.query.all()

    @jwt_required()
    @blp.arguments(TodoSchema)
    @blp.response(200, TodoSchema)
    def post(self, todo_data):
        todo = TodoModel(**todo_data)
        try:
            db.session.add(todo)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A todo with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the todo.")

        return todo
