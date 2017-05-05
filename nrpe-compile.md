   * CD into the NRPE source dir you downloaded from git and run ./configure
   * You will get an error about ssl and the configure script will not complete
   * To fix this error: yum install -y openssl-devel
   * ./configure --with-ssl=/usr/bin/openssl --with-ssl-lib=/usr/lib/x86_64-linux-gnu
