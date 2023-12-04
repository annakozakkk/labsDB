from .orders.game_service import GameService
from .orders.channel_service import ChannelService
from .orders.message_service import MessageService
from .orders.server_service import ServerService
from .orders.user_service import UserService
from .orders.role_service import RoleService
from .orders.user_channel_service import UserInChannel
from .orders.user_role_service import UserHasRoleService



channel_service = ChannelService()
game_service = GameService()
message_service = MessageService()
server_service = ServerService()
user_service = UserService()
role_service = RoleService()
user_channel_service = UserInChannel()
user_role_service = UserHasRoleService()
