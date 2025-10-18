from flask import Blueprint, request, jsonify
from extensions import db
from models import Comment

comments_bp = Blueprint('comments', __name__)

# CREATE
@comments_bp.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    if not data or 'task_id' not in data or 'text' not in data:
        return jsonify({"error": "Missing task_id or text"}), 400

    comment = Comment(task_id=data['task_id'], text=data['text'])
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict()), 201


# READ
@comments_bp.route('/comments/<int:task_id>', methods=['GET'])
def get_comments(task_id):
    comments = Comment.query.filter_by(task_id=task_id).all()
    return jsonify([c.to_dict() for c in comments]), 200


# UPDATE
@comments_bp.route('/comments/<int:id>', methods=['PUT'])
def update_comment(id):
    comment = Comment.query.get(id)
    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    data = request.get_json()
    comment.text = data.get('text', comment.text)
    db.session.commit()
    return jsonify(comment.to_dict()), 200


# DELETE
@comments_bp.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get(id)
    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"}), 200




