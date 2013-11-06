%define APP_BUILD_DATE %(date +'%%Y%%m%%d_%%H%%M')

Name:        jss
Summary:     Jenkins support scripts 
Version:     1.0.0
Release:     1
Group:       System/Libraries
License:     LGPL v2.1
BuildArch:   noarch
URL:         https://github.com/safrm/jss
Vendor:      Miroslav Safr <miroslav.safr@gmail.com>
Source0:     %{name}-%{version}.tar.bz2
Autoreq:     on
Autoreqprov: on
Requires:    gpg
Requires:    yum-utils
Requires:    createrepo

%description
Jenkins common tasks support scripts

%prep
%setup -c -n ./%{name}-%{version}

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/usr/bin
install -m 755 ./jss-jenkins-backup %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-jenkins-backup && rm -f %{buildroot}/usr/bin/jss-jenkins-backup.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-jenkins-backup && rm -f %{buildroot}/usr/bin/jss-jenkins-backup.bkp
install -m 755 ./jss-rpmrepo-update %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-rpmrepo-update && rm -f %{buildroot}/usr/bin/jss-rpmrepo-update.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-rpmrepo-update && rm -f %{buildroot}/usr/bin/jss-rpmrepo-update.bkp
install -m 755 ./jss-debrepo-signcheck %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-debrepo-signcheck && rm -f %{buildroot}/usr/bin/jss-debrepo-signcheck.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-debrepo-signcheck && rm -f %{buildroot}/usr/bin/jss-debrepo-signcheck.bkp
install -m 755 ./jss-debrepo-update %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-debrepo-update && rm -f %{buildroot}/usr/bin/jss-debrepo-update.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-debrepo-update && rm -f %{buildroot}/usr/bin/jss-debrepo-update.bkp

%files
%defattr(-,root,root,-)
%{_bindir}/jss-jenkins-backup
%{_bindir}/jss-rpmrepo-update
%{_bindir}/jss-debrepo-signcheck
%{_bindir}/jss-debrepo-update


