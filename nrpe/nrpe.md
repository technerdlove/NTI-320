

Notes for NRPE configuration and class: Thursday, April 27th


1)	We’re going to compare ‘chain of escalation’ diagrams and network diagrams of networks from last quarter.
Talk about them a little bit!  


## NRPE config


### Server

```bash
yum install nagios-plugins-nrpe
yum install nagios plugins-all
```


### Client

```bash
yum install nrpe
yum install nagios-plugins-nrpe
yum install nagios-plugins-all

vi /etc/nagios/nrpe.cfg

server_address=10.128.0.5


allowed_hosts=10.128.0.5

sudo systemctl start nrpe.service
sudo systemctl enable nrpe.service
```


### Troubleshooting NRPE

From nagios server: check_nrpe -H 10.0.0.3 -c check_load
From NRPE server execute the command in libexec /usr/lib64/nagios/plugins/




notes for compiling lab: 
Key part of open source software is that it ships with its source and can be modified.  This means you can add to it, compile with certain options, etc.  To download the source for a given package via an rpm:

yum install yum-utils

yumdownloader —source mypkg


Configure a build environment on a server:
https://wiki.centos.org/HowTos/SetupRpmBuildEnvironment

https://www.cyberciti.biz/faq/yum-download-source-packages-from-rhn/

Reminder: 'build' servers should have large hard drives.  At least 50G.

http://vault.centos.org/7.2.1511/os/Source/SPackages/


