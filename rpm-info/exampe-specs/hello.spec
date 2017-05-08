Name:		hello	
Version: 	1.0	
Release:	1%{?dist}
Summary: 	A program that prints 'hello world'	

Group:		NTI-320
License:	GPL2+
URL:		https://github.com/nic-instruction/NTI-320
Source0:	

BuildRequires:	https://github.com/nic-instruction/NTI-320/hello.c
Requires:	gcc

%description
'hello' will print 'hello cruel world' at each of your users when they log in.

install 'hello' if you would like a program to print 'hello cruel world' to you and 
other users of your system upon login.
%prep

%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc

On install: modify /home/*/.profile 

/etc/profile/profile.d/hello.sh		 

%changelog
