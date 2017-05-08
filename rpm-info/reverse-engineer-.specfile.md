```
yum -y install rpmrebuild
rpmrebuild -e [packagename]
```
You'll be asked some questions, it will open the specfile in vi.  When this happens, use the terminal to save off a copy of the spec file

```
:w /tmp/nagios.spec
:q!
```
If will ask if you want to rebuild the rpm and you can go ahead and say no.
