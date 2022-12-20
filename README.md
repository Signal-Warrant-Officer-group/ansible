19 DEC 2022 Update: 

When creating playbooks for specifc devices (Cisco, Palo Alto, ESXI, ect) place the YAML file in the respective file 

example

/playbook/cisco_ios/<name>.yaml



# 255N-255A-Ansible-Repo
This is repository as a community group to build playbooks for SNN, WINT, CPCE, ESXI, Palo Alto and other systems we use. 
Please if you create a playbook lable it as followed. 

file name - purpose for playbook  # configure_change_tunnel.yaml

YAML playbook 
---
- name: Backup router running configuration
  hosts: routers
  connection: network_cli
  gather_facts: false

  tasks:
#This command will save back up into the nested folder when ran
    - name: Backup router with cli_command
      cli_command:
        command: show run
      register: r_backup

    - name: Capture backup to control host
      vars:
      copy:
        content: "{{ r_backup.stdout }}"
        dest: "{{ inventory_hostname }}"
        
