#vim:set et sts=4 sw=4: 
# 
# Zanata Python Client
#
# Copyright (c) 2011 Jian Ni <jni@redhat.com>
# Copyright (c) 2011 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.


__all__ = (
        "VersionService",
   )

from rest.client import RestClient
from service import Service 

class VersionService(Service):
    def __init__(self, base_url,headers=None):
        self.restclient = RestClient(base_url)
        self.http_headers = headers

    def disable_ssl_cert_validation(self):
        self.restclient.disable_ssl_cert_validation()
        
    def get_server_version(self):
        res, content = self.restclient.request_version('/seam/resource/restv1/version',
                                                       self.http_headers)
        return self.messages(res,content)

