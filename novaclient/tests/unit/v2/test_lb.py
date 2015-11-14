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
from novaclient.tests.unit.fixture_data import lb as data
from novaclient.tests.unit import utils
from novaclient.v2 import lb


class LoadBalancerTest(utils.FixturedTestCase):

    client_fixture_class = client.V1
    data_fixture_class = data.V1

    def test_lb_host_list(self):
        hl = self.cs.lb.host_list()
        self.assert_called('GET', '/loadbalancer')
        [self.assertIsInstance(h, lb.LoadBalancer) for h in hl]

    def test_lb_suspend(self):
        body = {
            "suspend_host":
                {
                    "host": "compute1"
                }
        }
        self.cs.lb.suspend("compute1")
        self.assert_called('POST', '/loadbalancer/action', body)

    def test_lb_unsuspend(self):
        body = {
            "unsuspend_host":
                {
                    "host": "compute1"
                }
        }
        self.cs.lb.unsuspend("compute1")
        self.assert_called('POST', '/loadbalancer/action', body)
