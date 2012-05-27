# coding=utf-8

#############################################################################
#                                                                           #
#  This file is part of the MCBlockIt Official Python API.                  #
#  The project is licensed under the BSD Clause-2 License.                  #
#                                                                           #
#  You should have found a copy of this license included with this          #
#  file. If not, you can find more information on it at the OSI website..   #
#                                                                           #
#  http://www.opensource.org/licenses/bsd-license.php                       #
#                                                                           #
#  Or at the project's webpage..                                            #
#                                                                           #
#  https://github.com/gdude2002/MCBlockItPythonAPI                          #
#                                                                           #
#############################################################################

import urllib, urllib2

try:
    import simplejson as json
except ImportError:
    import json

class MCBlockItAPI(object):
    """
        Herpity derpity derp.
    """

    def __init__(self, api_key=None):
        self.api_key = api_key

    def bancheck(self, timestamp=0):
        pass

    def callback(self, players={}):
        pass

    def banimport(self, users=[]):
        pass

    def ban(self, user="", admin="", reason="", timestamp=0, type=0):
        pass

    def unban(self, user="", timestamp=0):
        pass

    def userdata(self, user=""):
        pass

    def _request(self, data):

        return

class NoAPIKeyException(Exception):

    def __repr__(self):
        return "This command requires an API key"
