#!/usr/bin/env python3

import json
import requests
import urllib3

# Desactiva advertencias SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_HOST = "https://192.168.3.6:8006"
API_TOKEN_ID = "admintst@pam!mytokenid"
API_TOKEN_SECRET = "ca6d23ae-161a-4236-87f7-0e0a2ce7e506"
HEADERS = {
    "Authorization": f"PVEAPIToken={API_TOKEN_ID}={API_TOKEN_SECRET}",
    "Content-Type": "application/json"
}

def get_json(url):
    response = requests.get(url, headers=HEADERS, verify=False)
    response.raise_for_status()
    return response.json()['data']

def main():
    inventory = {
        "_meta": {
            "hostvars": {}
        },
        "proxmox": {
            "hosts": [],
            "vars": {}
        }
    }

    nodes = get_json(f"{API_HOST}/api2/json/nodes")

    for node in nodes:
        node_name = node['node']
        # Obtener VMs QEMU
        try:
            vms = get_json(f"{API_HOST}/api2/json/nodes/{node_name}/qemu")
            for vm in vms:
                if 'name' in vm:
                    inventory["proxmox"]["hosts"].append(vm['name'])
                    inventory["_meta"]["hostvars"][vm['name']] = {
                        "proxmox_node": node_name,
                        "vmid": vm['vmid'],
                        "type": "qemu"
                    }
        except:
            pass

        # Obtener LXC
        try:
            lxcs = get_json(f"{API_HOST}/api2/json/nodes/{node_name}/lxc")
            for lxc in lxcs:
                if 'name' in lxc:
                    inventory["proxmox"]["hosts"].append(lxc['name'])
                    inventory["_meta"]["hostvars"][lxc['name']] = {
                        "proxmox_node": node_name,
                        "vmid": lxc['vmid'],
                        "type": "lxc"
                    }
        except:
            pass

    print(json.dumps(inventory, indent=2))

if __name__ == "__main__":
    main()
