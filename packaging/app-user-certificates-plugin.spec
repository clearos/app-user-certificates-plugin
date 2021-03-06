
Name: app-user-certificates-plugin
Epoch: 1
Version: 2.1.6
Release: 1%{dist}
Summary: Security Certificates Policies - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-user-certificates-plugin-%{version}.tar.gz
Buildarch: noarch

%description
User Certificates Policies provide access control for the security certificates.

%package core
Summary: Security Certificates Policies - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
User Certificates Policies provide access control for the security certificates.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/user_certificates_plugin
cp -r * %{buildroot}/usr/clearos/apps/user_certificates_plugin/

install -D -m 0644 packaging/user_certificates.php %{buildroot}/var/clearos/accounts/plugins/user_certificates.php

%post core
logger -p local6.notice -t installer 'app-user-certificates-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/user_certificates_plugin/deploy/install ] && /usr/clearos/apps/user_certificates_plugin/deploy/install
fi

[ -x /usr/clearos/apps/user_certificates_plugin/deploy/upgrade ] && /usr/clearos/apps/user_certificates_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-user-certificates-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/user_certificates_plugin/deploy/uninstall ] && /usr/clearos/apps/user_certificates_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/user_certificates_plugin/packaging
%dir /usr/clearos/apps/user_certificates_plugin
/usr/clearos/apps/user_certificates_plugin/deploy
/usr/clearos/apps/user_certificates_plugin/language
/var/clearos/accounts/plugins/user_certificates.php
