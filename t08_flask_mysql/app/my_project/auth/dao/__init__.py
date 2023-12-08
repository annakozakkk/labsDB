
# orders DB
from .orders.channel_dao import ChannelDAO
from .orders.game_dao import GameDAO
from .orders.user_dao import UserDAO
from .orders.server_dao import ServerDAO
from .orders.message_dao import MessageDAO
from .orders.role_dao import RoleDAO
from .orders.user_channel_dao import UserInChannelDAO
from .orders.user_role_dao import UserHasRoleDAO

game_dao = GameDAO()
channel_dao = ChannelDAO()
user_dao = UserDAO()
server_dao = ServerDAO()
message_dao = MessageDAO()
role_dao = RoleDAO()
user_channel_dao = UserInChannelDAO()
user_has_role = UserHasRoleDAO()
