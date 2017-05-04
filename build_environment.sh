#!/bin/bash
# This should be the finishing script for a micro with a 50G hard drive

yum -y install rpm-build make gcc git
mkdir -p /root/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cd ~/
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
git clone https://github.com/NagiosEnterprises/nrpe.git
