# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from novaclient.tests.unit.fixture_data import base


class V1(base.Fixture):

    base_url = 'loadbalancer/rules'

    def setUp(self):
        super(V1, self).setUp()

        get_lb_rules = {
            'lb_rules': [
                {'id': 1,
                 'type': 'host',
                 'value': 'compute1.*',
                 'allow': False},
                {'id': 2,
                 'type': 'ha',
                 'value': 'ha1',
                 'allow': True}
            ]
        }

        headers = {'Content-Type': 'application/json'}

        self.requests.register_uri('GET', self.url(),
                                   json=get_lb_rules,
                                   headers=headers)

        post_lb_rules = {
            'lb_rule':
                {
                 'type': 'host',
                 'value': 'compute2*',
                 'allow': True
                }
        }

        self.requests.register_uri('DELETE', self.url(1), status_code=202)
        self.requests.register_uri('POST', self.url(), json=post_lb_rules)
