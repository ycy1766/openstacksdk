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

from typing import Any

from openstack.network.v2 import tap_mirror_rule
from openstack.tests.unit import base


IDENTIFIER = 'IDENTIFIER'
TAP_MIRROR_ID = 'TAP_MIRROR_ID'
EXAMPLE: dict[str, Any] = {
    'id': IDENTIFIER,
    'project_id': '42',
    'tap_mirror_id': TAP_MIRROR_ID,
    'priority': 100,
    'action': 'mirror',
    'direction': 'IN',
    'ethertype': 'IPv4',
    'protocol': 'tcp',
    'source_ip_prefix': None,
    'destination_ip_prefix': '10.0.0.0/24',
    'source_port_range_min': None,
    'source_port_range_max': None,
    'destination_port_range_min': 443,
    'destination_port_range_max': 443,
}


class TestTapMirrorRule(base.TestCase):
    def test_basic(self):
        sot = tap_mirror_rule.TapMirrorRule()
        self.assertEqual('rule', sot.resource_key)
        self.assertEqual('rules', sot.resources_key)
        self.assertEqual(
            '/taas/tap_mirrors/%(tap_mirror_id)s/rules', sot.base_path
        )
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_fetch)
        self.assertFalse(sot.allow_commit)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = tap_mirror_rule.TapMirrorRule(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['project_id'], sot.project_id)
        self.assertEqual(EXAMPLE['tap_mirror_id'], sot.tap_mirror_id)
        self.assertEqual(EXAMPLE['priority'], sot.priority)
        self.assertEqual(EXAMPLE['action'], sot.action)
        self.assertEqual(EXAMPLE['direction'], sot.direction)
        self.assertEqual(EXAMPLE['ethertype'], sot.ethertype)
        self.assertEqual(EXAMPLE['protocol'], sot.protocol)
        self.assertEqual(
            EXAMPLE['destination_ip_prefix'], sot.destination_ip_prefix
        )
        self.assertEqual(
            EXAMPLE['destination_port_range_min'],
            sot.destination_port_range_min,
        )
        self.assertEqual(
            EXAMPLE['destination_port_range_max'],
            sot.destination_port_range_max,
        )

        self.assertDictEqual(
            {
                'limit': 'limit',
                'marker': 'marker',
                'project_id': 'project_id',
                'priority': 'priority',
                'action': 'action',
                'direction': 'direction',
                'ethertype': 'ethertype',
                'protocol': 'protocol',
                'sort_key': 'sort_key',
                'sort_dir': 'sort_dir',
                'fields': 'fields',
            },
            sot._query_mapping._mapping,
        )
