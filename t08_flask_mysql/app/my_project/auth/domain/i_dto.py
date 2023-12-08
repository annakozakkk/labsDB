from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict


class IDto:
    """
    Interface to put and extract DTO objects to/from domain objects.
    """

    @abstractmethod
    def put_into_dto(self) -> Dict[str, object]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """

    @staticmethod
    @abstractmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """


@dataclass
class UserDto(IDto):
    """
    Data Transfer Object for User.
    """
    user_id: int
    username: str
    email: str
    password: str
    about_user: str
    in_discord: datetime

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'UserDto':
        return UserDto(**dto_dict)


@dataclass
class ServerDto(IDto):
    """
    Data Transfer Object for User.
    """
    server_id: int
    name: str
    creation_date: datetime

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'ServerDto':
        return ServerDto(**dto_dict)


@dataclass
class GameDto(IDto):
    """
    Data Transfer Object for User.
    """
    game_id: int
    name: str
    release_date: date

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'GameDto':
        return GameDto(**dto_dict)

@dataclass
class ChannelDto(IDto):
    """
    Data Transfer Object for Channel.
    """
    channel_id: int
    name: str
    creation_date: datetime
    owner: str
    type: str
    server_id: int

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'ChannelDto':
        return ChannelDto(**dto_dict)



@dataclass
class MessageDto(IDto):
    """
    Data Transfer Object for Channel Message.
    """
    message_id: int
    user_id: int
    message_text: str
    url: str
    timestamp: datetime

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'MessageDto':
        return MessageDto(**dto_dict)


@dataclass
class RoleDto(IDto):
    """
    Data Transfer Object for Channel Message.
    """
    role_id: int
    name: str
    description: str

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'RoleDto':
        return RoleDto(**dto_dict)


@dataclass
class UserInChannelDto(IDto):
    """
    Data Transfer Object for UserInChannel.
    """
    id: int
    user_id: int
    channel_id: int

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'UserInChannelDto':
        return UserInChannelDto(**dto_dict)

@dataclass
class UserHasRoleDto(IDto):
    """
    Data Transfer Object for UserInChannel.
    """
    id: int
    user_id: int
    role_id: int

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'UserHasRoleDto':
        return UserHasRoleDto(**dto_dict)

