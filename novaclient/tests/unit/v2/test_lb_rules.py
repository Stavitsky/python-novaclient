# -*- coding: utf-8 -*-
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


from novaclient.tests.unit.fixture_data import client
from novaclient.tests.unit.fixture_data import lb_rules as data
from novaclient.tests.unit import utils
from novaclient.v2 import lb_rules


class LbRulesTest(utils.FixturedTestCase):

    client_fixture_class = client.V1
    data_fixture_class = data.V1

    def test_list_lb_rules(self):
        rl = self.cs.lb_rules.list()
        self.assert_called('GET', '/loadbalancer/rules')
        [self.assertIsInstance(r, lb_rules.LoadBalancerRule) for r in rl]

    def test_delete_lb_rule(self):
        self.cs.lb_rules.delete(1)
        self.assert_called('DELETE', '/loadbalancer/rules/1')

    def test_create_lb_rule(self):
        body = {
            'lb_rule':
                {
                 'type': 'host',
                 'value': 'compute2*',
                 'allow': True
                }
        }
        lbr = self.cs.lb_rules.create(type='host',
                                      value='compute2*',
                                      allow=True)
        self.assert_called('POST', '/loadbalancer/rules', body=body)
        self.assertIsInstance(lbr, lb_rules.LoadBalancerRule)
