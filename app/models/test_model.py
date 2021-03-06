from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base_model import BaseModel


class TestModel(BaseModel):
    username = db.Column(db.String(64), server_default="", comment="用户名称")

    # password_hash = method$salt$hash
    password_hash = db.Column(db.String(128), server_default="", comment="密码")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
