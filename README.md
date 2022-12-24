Welcome to our Ansible project on the commercial side!

Our organization is focused on using Ansible to create and test projects in a local environment. By bringing together a diverse group of collaborators, we aim to learn from each other and make the most of our shared passion for automation.

This project on GitHub is dedicated to developing and improving our ansible skills outside of work, while keeping our production network playbooks separate in our Army github.

We believe that by working together and sharing our knowledge and resources, we can make a real impact on the efficiency and effectiveness of our projects. Whether you are an experienced developer or new to ansible, we welcome your contribution and participation.

Together, let's build and test innovative projects using ansible. We look forward to collaborating with you!

--------------------------------
This is the layout of the lab based on the configuration I have under the repository.

<img width="427" alt="Screenshot 2022-12-24 at 2 07 53 PM" src="https://user-images.githubusercontent.com/13005984/209451062-7feba0b2-5d5c-413f-ac84-6a2e6c458372.png">

Running the follow systems 

1 Dell server with ESX-I 6.5 

3 CSRV-1000

1 Ansible server (ubunutu LTS 20.04)

1 Windows server 2012 (Radius)

1 Palo Alto Firewall VM

--------------------------------
To install Ansible on an Ubuntu server, follow these steps:

Update the package manager's package list:
```
sudo apt-get update
```
Install the software-properties-common package, which allows you to use the add-apt-repository command:
```
sudo apt-get install software-properties-common
```
Add the Ansible package repository to your system's package sources list:
```
sudo add-apt-repository ppa:ansible/ansible
```
Update the package manager's package list again to include the packages from the new repository:
```
sudo apt-get update
```
Install Ansible:
```
sudo apt-get install ansible
```
To verify that Ansible has been installed correctly, you can check the version:
```
ansible --version
```
This should output the version of Ansible that you have installed.

Note: These instructions are for Ubuntu 20.04. If you are using a different version of Ubuntu, the package names and repository names may be different. You may need to adjust the instructions accordingly.



--------------------------------

--- update December 22 2022 ---

I wanted to bring to your attention that due to the new policy, we are no longer able to push code up for testing in an environment. This means that the usual process of using VS Code to test and push playbooks will not be possible.  Otherwise we would need to pay for the team plan which is $4 per user.

The only option available to us at this time is to create playbooks locally, test them, and then manually upload them into the repository. This may require a bit more time and effort on our part, but it is important that we follow the new policy in order to maintain the integrity and security of our systems.

--------------------------------

19 DEC 2022 Update: 

When creating playbooks for specifc devices (Cisco, Palo Alto, ESXI, ect) place the YAML file in the respective file 

example

/playbook/cisco_ios/<name>.yaml


