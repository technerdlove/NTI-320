Name:		hello			# Package name (should be unique)
Version: 	1.0			# Unless you bump the version, your changes won't install when your
Release:	1%{?dist}		# RPM.  Release (similar) for patches, tweeks and such.
Summary: 	A program that prints 'hello world'

Group:		NTI-320			# who makes it
License:	GPL2+			# who can use it
URL:		https://github.com/nic-instruction/NTI-320 	   	    # How to find the group who makes it
Source0:	https://github.com/nic-instruction/NTI-320/rpm-info/hello.c # How to find the source

BuildRequires:	gcc, python >= 1.3	# What packages must the people compiling the rpm have installed
Requires:	bash			# Additional packages the client must have installed to run the program

%description
'hello' will print 'hello cruel world' at each of your users when they log in.

install 'hello' if you would like a program to print 'hello cruel world' to you and 
other users of your system upon login.

%prep					# The things you need to do to set the build
					# Environment, file prep, and so forth

%setup -q				# Used to unpack your source code
					# by default, it will grab source from your source url
					# -n let's you set the name of the build dir
					


%build					# This builds from source (what we did manually last class)
%configure				# You can add additional configure flags here --with-ssl and so on
make %{?_smp_mflags}			# Make arguments here (recall nrpe is make all instead of simply make)


%install
rm -rf %{buildroot}			# Clean out the build dir				
make install DESTDIR=%{buildroot}	# Puts your freshly compiled binaries into your rpmbuild 'build' dir
%clean
rm -rf %{buildroot}			# Clean up

# RPM packages can run scripts prior to installation with %pre, and after installation with %post. You can also run scripts prior to an uninstall with %preun and after an uninstall with %postun. For example:
#%post
#/sbin/chkconfig --add ypbind
#%preun
#if [ "$1" = 0 ] ; then
#/sbin/service ypbind stop > /dev/null 2>&1
#/sbin/chkconfig --del ypbind
#fi
#exit 0
#%postun
#if [ "$1" -ge 1 ]; then
#/sbin/service ypbind condrestart > /dev/null 2>&1
#fi
#exit 0
# we'll do a 'On install: modify /home/*/.profile' to add this executable

# Note, we could easily use bash to print
                                         # "hello cruel world"
                                         # but that's not the point of this tutorial, now
                                         # is it? The point is to show you how to modify
                                         # multiple files on install.  Which is why we
                                         # are wrapping c in bash.

%files					# Additional files required by the package
%defattr(-,root,root)			# Sets default perms
/usr/bin/hello.c
%config
/etc/profile/profile.d/hello.sh		# Our example wrapper script for our package

%doc					# docs for the package


%changelog				# changes you (and others) have made and why
