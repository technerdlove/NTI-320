#!/bin/bash
yum -y install yum-utils rpmbuild

yumdownloader --source nrpe
yumdownloader --source nagios

#This will give you the source packages for nrpe and nagios on centos7
# Note: this process is much easier on other flavors of linux
