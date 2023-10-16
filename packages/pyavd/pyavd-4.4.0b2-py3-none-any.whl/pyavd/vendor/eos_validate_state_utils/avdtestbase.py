# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property
from ipaddress import ip_interface

from pyavd.vendor.errors import AristaAvdMissingVariableError
from pyavd.vendor.utils import get, get_item

LOGGER = logging.getLogger(__name__)


class AvdTestBase:
    """
    Base class for all AVD eos_validate_state tests.
    """

    def __init__(self, device_name: str, hostvars: dict):
        """
        Initialize the AvdTestBase class.

        Args:
            device_name (str): The current device name for which the plugin is being run
            hostvars (dict): A dictionnary that contains a key for each device with a value of the structured_config
                           when using Ansible, this is the equivalent of `task_vars['hostvars']`
        """
        self.hostvars = hostvars
        self.device_name = device_name

    def render(self) -> dict:
        """
        Return the test_definition of the class.

        This method attempts to retrieve the value of the `test_definition` attribute.
        If `test_definition` is not set or returns a falsy value (e.g., None),
        an empty dictionary will be returned instead.

        Returns:
            dict: The test definition if available and valid; otherwise, an empty dictionary.
        """
        return getattr(self, "test_definition", None) or {}

    @property
    def loopback0_mapping(self) -> dict:
        return self._get_eos_validate_state_vars["loopback0_mapping"]

    @property
    def vtep_mapping(self) -> dict:
        return self._get_eos_validate_state_vars["vtep_mapping"]

    @cached_property
    def _get_eos_validate_state_vars(self) -> dict:
        """
        Generates variables for the eos_validate_state tests, which are used in AvdTestBase subclasses.
        These variables include mappings for loopback and VTEP interfaces.

        Returns:
            dict: A dictionary containing:
                - "loopback0_mapping": a list of tuples where each tuple contains a hostname and its Loopback0 IP address.
                - "vtep_mapping": a list of tuples where each tuple contains a hostname and its VTEP IP address if `Vxlan1` is the source_interface.
        """
        results = {"loopback0_mapping": [], "vtep_mapping": []}

        for host in self.hostvars:
            loopback_interfaces = get(self.hostvars, f"{host}..loopback_interfaces", [], separator="..")
            for loopback_interface in loopback_interfaces:
                # TODO Add more conditions here to avoid using type `l3leaf` in connectivity tests; router_id or update_source maybe?
                if loopback_interface["name"] == "Loopback0":
                    try:
                        loopback_ip = get(loopback_interface, "ip_address", required=True)
                        results["loopback0_mapping"].append((host, str(ip_interface(loopback_ip).ip)))
                    except AristaAvdMissingVariableError as e:
                        LOGGER.warning("Variable '%s' is missing. Please validate the Loopback interfaces data model of this host.", str(e))
                        continue

            vtep_interface = get(self.hostvars, f"{host}..vxlan_interface..Vxlan1..vxlan..source_interface", separator="..")
            if vtep_interface is not None:
                try:
                    loopback_interface = get_item(loopback_interfaces, "name", vtep_interface, required=True, var_name=f"name: {vtep_interface}")
                    loopback_ip = get(loopback_interface, "ip_address", required=True)
                    results["vtep_mapping"].append((host, str(ip_interface(loopback_ip).ip)))
                except AristaAvdMissingVariableError as e:
                    LOGGER.warning("Variable '%s' is missing. Please validate the Loopback interfaces data model of this host.", str(e))
                    continue

        return results
