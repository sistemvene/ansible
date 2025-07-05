# Inventario Dinámico Proxmox

Esta carpeta contiene inventarios dinámicos para cada nodo Proxmox independiente:

- `proxmox-nodo01.yml`: Nodo TEST (192.168.3.6)
- `proxmox-nodo02.yml`: Nodo PROD (192.168.2.5)

**No se exponen credenciales ni IPs directamente.** Las variables de entorno son necesarias para que funcione el plugin:

### Variables esperadas para cada nodo

#### Nodo 01 (TEST)

- `PROXMOX_URL_NODE01`: https://192.168.3.6:8006
- `PROXMOX_USER_NODE01`: usuario@pve
- `PROXMOX_PASSWORD_NODE01`: contraseña

#### Nodo 02 (PROD)

- `PROXMOX_URL_NODE02`: https://192.168.2.5:8006
- `PROXMOX_USER_NODE02`: usuario@pve
- `PROXMOX_PASSWORD_NODE02`: contraseña

