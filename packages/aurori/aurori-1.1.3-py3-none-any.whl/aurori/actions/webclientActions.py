"""
The aurori project

Copyright (C) 2022  Marcus Drobisch,

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__authors__ = ["Marcus Drobisch"]
__contact__ = "aurori@fabba.space"
__credits__ = []
__license__ = "AGPLv3+"

from aurori.actions.actionGenerator import BaseAction


class ResetLoginAction(BaseAction):
    def __init__(self, app):
        print("Instance of ResetLoginAction created")


class UpdateSessionTokenAction(BaseAction):
    action = 'updateToken'
    target = 'webclient'

    def __init__(self, app):
        pass

    @classmethod
    def generate(cls, token, userinfo, delay=0.0):
        action = super(UpdateSessionTokenAction, cls).generate(delay)
        action['token'] = token
        action['userinfo'] = userinfo

        return action


class RouteAction(BaseAction):
    action = 'route'
    target = 'webclient'

    def __init__(self, app):
        pass

    @classmethod
    def generate(cls, route, delay=0.0):
        action = super(RouteAction, cls).generate(delay)
        action['route'] = route
        return action


class NotificationAction(BaseAction):
    action = 'notify'
    target = 'webclient'

    def __init__(self, app):
        pass

    @classmethod
    def generate(cls, message, messagetype, delay=0.0):
        action = super(NotificationAction, cls).generate(delay)
        action['message'] = message
        action['messagetype'] = messagetype
        return action


class LoadViewAction(BaseAction):
    action = 'loadView'
    target = 'webclient'

    def __init__(self, app):
        pass

    @classmethod
    def generate(cls, uri, properties, entries, metadata={}, delay=0.0):
        action = super(LoadViewAction, cls).generate(delay)
        action['viewname'] = uri
        action['viewdata'] = {}
        action['viewdata']['properties'] = properties
        action['viewdata']['entries'] = entries
        action['viewdata']['metadata'] = metadata
        return action


class UpdateMenuAction(BaseAction):
    action = 'updateMenu'
    target = 'webclient'

    def __init__(self, app):
        pass

    @classmethod
    def generate(cls, menu, delay=0.0):
        action = super(UpdateMenuAction, cls).generate(delay)
        action['data'] = menu
        return action


class UpdateActionlinkStatusAction(BaseAction):
    action = 'updateActionlinkStatus'
    target = 'webclient'

    def __init__(self, app):
        pass

    @classmethod
    def generate(cls, status, message, delay=0.0):
        action = super(UpdateActionlinkStatusAction, cls).generate(delay)
        action['status'] = status
        action['message'] = message
        return action
