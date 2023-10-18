#!/usr/bin/python

# Copyright: (c) 2019, Hetzner Cloud GmbH <info@hetzner-cloud.de>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = """
---
module: hcloud_datacenter_info

short_description: Gather info about the Hetzner Cloud datacenters.

description:
    - Gather info about your Hetzner Cloud datacenters.

author:
    - Lukas Kaemmerling (@LKaemmerling)

options:
    id:
        description:
            - The ID of the datacenter you want to get.
            - The module will fail if the provided ID is invalid.
        type: int
    name:
        description:
            - The name of the datacenter you want to get.
        type: str
extends_documentation_fragment:
- hetzner.hcloud.hcloud

"""

EXAMPLES = """
- name: Gather hcloud datacenter info
  hetzner.hcloud.hcloud_datacenter_info:
  register: output
- name: Print the gathered info
  debug:
    var: output
"""

RETURN = """
hcloud_datacenter_info:
    description:
      - The datacenter info as list
    returned: always
    type: complex
    contains:
        id:
            description: Numeric identifier of the datacenter
            returned: always
            type: int
            sample: 1937415
        name:
            description: Name of the datacenter
            returned: always
            type: str
            sample: fsn1-dc8
        description:
            description: Detail description of the datacenter
            returned: always
            type: str
            sample: Falkenstein DC 8
        location:
            description: Name of the location where the datacenter resides in
            returned: always
            type: str
            sample: fsn1
        city:
            description: City of the location
            returned: always
            type: str
            sample: fsn1
"""

from typing import List, Optional

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native

from ..module_utils.hcloud import AnsibleHCloud
from ..module_utils.vendor.hcloud import HCloudException
from ..module_utils.vendor.hcloud.datacenters import BoundDatacenter


class AnsibleHCloudDatacenterInfo(AnsibleHCloud):
    represent = "hcloud_datacenter_info"

    hcloud_datacenter_info: Optional[List[BoundDatacenter]] = None

    def _prepare_result(self):
        tmp = []

        for datacenter in self.hcloud_datacenter_info:
            if datacenter is not None:
                tmp.append(
                    {
                        "id": to_native(datacenter.id),
                        "name": to_native(datacenter.name),
                        "description": to_native(datacenter.description),
                        "location": to_native(datacenter.location.name),
                    }
                )

        return tmp

    def get_datacenters(self):
        try:
            if self.module.params.get("id") is not None:
                self.hcloud_datacenter_info = [self.client.datacenters.get_by_id(self.module.params.get("id"))]
            elif self.module.params.get("name") is not None:
                self.hcloud_datacenter_info = [self.client.datacenters.get_by_name(self.module.params.get("name"))]
            else:
                self.hcloud_datacenter_info = self.client.datacenters.get_all()

        except HCloudException as exception:
            self.fail_json_hcloud(exception)

    @classmethod
    def define_module(cls):
        return AnsibleModule(
            argument_spec=dict(
                id={"type": "int"},
                name={"type": "str"},
                **super().base_module_arguments(),
            ),
            supports_check_mode=True,
        )


def main():
    module = AnsibleHCloudDatacenterInfo.define_module()
    hcloud = AnsibleHCloudDatacenterInfo(module)

    hcloud.get_datacenters()
    result = hcloud.get_result()

    ansible_info = {"hcloud_datacenter_info": result["hcloud_datacenter_info"]}
    module.exit_json(**ansible_info)


if __name__ == "__main__":
    main()
