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

from openstack import resource


class TapMirrorRule(resource.Resource):
    """Tap Mirror Rule (``rules`` sub-resource of a Tap Mirror)"""

    resource_key = 'rule'
    resources_key = 'rules'
    base_path = '/taas/tap_mirrors/%(tap_mirror_id)s/rules'

    # capabilities
    allow_create = True
    allow_fetch = True
    allow_commit = False
    allow_delete = True
    allow_list = True

    _allow_unknown_attrs_in_body = True

    _query_mapping = resource.QueryParameters(
        "sort_key",
        "sort_dir",
        'fields',
        'project_id',
        'priority',
        'action',
        'direction',
        'ethertype',
        'protocol',
    )

    # Properties
    #: The ID of the Tap Mirror the rule belongs to.
    tap_mirror_id = resource.URI('tap_mirror_id')
    #: The ID of the Tap Mirror Rule.
    id = resource.Body('id')
    #: The ID of the project that owns the Tap Mirror Rule.
    project_id = resource.Body('project_id', alias='tenant_id')
    #: Tenant_id (deprecated attribute).
    tenant_id = resource.Body('tenant_id', deprecated=True)
    #: The priority of the rule (1-32767), higher values are matched first.
    priority = resource.Body('priority', type=int)
    #: The action of the rule: mirror or skip.
    action = resource.Body('action')
    #: The direction the rule applies to: IN, OUT or None for both.
    direction = resource.Body('direction')
    #: The ethertype of the matched traffic: IPv4, IPv6 or None for every
    #: frame (derived from the IP prefixes when given).
    ethertype = resource.Body('ethertype')
    #: The IP protocol of the matched traffic (tcp, udp, sctp, icmp,
    #: ipv6-icmp) or None.
    protocol = resource.Body('protocol')
    #: The source IP prefix of the matched traffic.
    source_ip_prefix = resource.Body('source_ip_prefix')
    #: The destination IP prefix of the matched traffic.
    destination_ip_prefix = resource.Body('destination_ip_prefix')
    #: The lower bound of the matched source port range.
    source_port_range_min = resource.Body('source_port_range_min', type=int)
    #: The upper bound of the matched source port range.
    source_port_range_max = resource.Body('source_port_range_max', type=int)
    #: The lower bound of the matched destination port range.
    destination_port_range_min = resource.Body(
        'destination_port_range_min', type=int
    )
    #: The upper bound of the matched destination port range.
    destination_port_range_max = resource.Body(
        'destination_port_range_max', type=int
    )
