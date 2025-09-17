from .db import Session, Message

def save_message(user_id, role, content):
    session = Session()
    msg = Message(user_id=user_id, role=role, content=content)
    session.add(msg)
    session.commit()

def get_history(user_id, limit=10):
    session = Session()
    messages = session.query(Message).filter_by(user_id=user_id).order_by(Message.id.desc()).limit(limit).all()
    return [(m.role, m.content) for m in reversed(messages)]
