Name:		hello
Version: 	1.0
Release:	1%{?dist}
Summary: 	A program that prints 'hello world'

Group:		NTI-320	
License:	GPL2+
URL:		https://github.com/nic-instruction/NTI-320
Source0:	https://github.com/nic-instruction/NTI-320/rpm-info/hello.tar.gz

BuildRequires:	gcc, python >= 1.3
Requires:	bash

%description
'hello' will print 'hello cruel world' at each of your users when they log in.

install 'hello' if you would like a program to print 'hello cruel world' to you and 
other users of your system upon login.

%prep					
# If you didn't tar zip your files yet, you can do that here			

%setup -q	
		
# BEGIN unpack your tarball, run configure on it and make
%build					
%configure
# binaries are built here
make %{?_smp_mflags}
# END unpack your tarball, run configure on it and make

%install
# Your working directory is now rpm-buildroot	
# root/rpm/build/buildroot
rm -rf %{buildroot}
m
make install DESTDIR=%{buildroot}
%clean
rm -rf %{buildroot}

%files					
%defattr(-,root,root)	
/usr/bin/hello.c
%config
/etc/profile/profile.d/hello.sh		

%doc			


%changelog				# changes you (and others) have made and why
