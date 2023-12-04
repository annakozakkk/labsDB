from t08_flask_mysql.app.my_project import db

user_channel_association = db.Table(
    'user_channel_association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('channel_id', db.Integer, db.ForeignKey('channel.channel_id'))
)

# user_role_association = db.Table(
#     'user_role_association',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
#     db.Column('role_id', db.Integer, db.ForeignKey('role.role_id')))
