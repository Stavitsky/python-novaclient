# Copyright (c) 2015 Servionica, LLC
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from novaclient import base
from novaclient import exceptions
from novaclient.i18n import _
from oslo_utils import strutils


class LoadBalancer(base.Resource):

    """LoadBalancer resource class."""

    def __repr__(self):
        return "<LoadBalancer: %s" % self


class LoadBalancerManager(base.ManagerWithFind):

    """
    Manage :class: 'LoadBalancer' resources.
    """

    resource_class = LoadBalancer

    def list(self):
        pass

    def host_list(self):

        """List Compute Nodes."""

        return self._list("/loadbalancer", "compute_nodes")

    def suspend(self, hostname):
        """
        Suspend host.
        """
        body = {"suspend_host":
                {"host": hostname}
                }
        url = "/loadbalancer/action"
        return self.api.client.post(url, body=body)

    def unsuspend(self, hostname):
        """
        Unsuspend host.
        """
        body = {"unsuspend_host":
                {"host": hostname}
                }
        url = "/loadbalancer/action"
        return self.api.client.post(url, body=body)
