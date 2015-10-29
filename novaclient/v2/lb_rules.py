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


class LoadBalancerRule(base.Resource):

    """A 'balancer rule' is rule how nova-loadbalancer is working"""

    def __repr__(self):
        return "<LoadBalancer rule ID: %s" % self.id

    def update(self, values):
        raise NotImplementedError
        # return self.manager.update(self, values)

    def add_rule(self, host):
        raise NotImplementedError
        # return self.manager.add_rule(self, host)

    def delete(self):
        raise NotImplementedError
        # self.manager.delete(self)


class LoadBalancerRulesManager(base.ManagerWithFind):

    """
    Manage :class:'LoadBalancerRule' resources.
    """

    resource_class = LoadBalancerRule

    def list(self):
        """
        Get a list of all LoadBalancer rules.

        :rtype: list of :class:`LoadBalancerRule`.
        """
        return self._list("/loadbalancer/rules", "lb_rules")

    def create(self, type, value, allow):
        """
        Create LoadBalancer rule.

        :param type: Type of the object for which the rule is applied
        :param value: Regex string ...
        :param allow: Bool value which allow (True) or not (False) migrations
        """

        try:
            allow = strutils.bool_from_string(allow, True)
        except Exception:
            raise exceptions.CommandError(_("allow must be a boolean."))

        body = {
            "lb_rule":
            {
                "type": type,
                "value": value,
                "allow": allow
            }
        }

        return self._create("/loadbalancer/rules", body, "lb_rule")

    def delete(self, lb_rule_id):
        """
        Delete LoadBalancer rule.
        """
        return self._delete("/loadbalancer/rules/%s" % lb_rule_id)