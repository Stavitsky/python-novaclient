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

    base_url = 'loadbalancer/'

    def setUp(self):
        super(V1, self).setUp()

        get_lb_compute_nodes = {
            'compute_nodes': [
                {
                    "hypervisor_hostname": "compute1.students.dev",
                    "cpu_used_percent": 14.00,
                    "ram_total": 2048,
                    "ram_used": 1024,
                    "ram_used_percent": 50.00,
                    "suspend_state": "active",
                    "mac_to_wake": "00:00:00:00:00:00",
                    "vcpus": 4
                },
                {
                    "hypervisor_hostname": "compute2.students.dev",
                    "cpu_used_percent": 23.00,
                    "ram_total": 4096,
                    "ram_used": 1024,
                    "ram_used_percent": 25.00,
                    "suspend_state": "active",
                    "mac_to_wake": "00:00:00:00:00:00",
                    "vcpus": 8
                }
            ]
        }

        headers = {'Content-Type': 'application/json'}
        self.requests.register_uri('GET', self.url(),
                                   json=get_lb_compute_nodes,
                                   headers=headers)

        self.requests.register_uri('POST', self.url('action'),
                                   headers=headers,
                                   status_code=202)
