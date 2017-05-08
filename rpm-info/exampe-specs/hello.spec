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
hello allows you to run a program that will say 'hello cruel world'

install hello if you would like a program to say hello cruel world to you.
%prep

%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog
