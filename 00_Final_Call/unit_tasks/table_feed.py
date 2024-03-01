from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from database import Base, SessionLocal, engine
from table_post import Post
from table_user import User


class Feed(Base):
    __tablename__ = "feed_action"
    __table_args__ = {"schema": "public"}
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)
    user = relationship(User)
    post = relationship(Post)
    action = Column(String)
    time = Column(TIMESTAMP)


if __name__ == "__main__":
    session = SessionLocal()
    results = (
        session.query(Feed)
        .limit(10)
        .all()
    )
    print([(x.user_id, x.post_id) for x in results])