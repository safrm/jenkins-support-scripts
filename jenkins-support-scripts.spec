%define APP_BUILD_DATE %(date +'%%Y%%m%%d_%%H%%M')

Name:        jenkins-support-scripts
Summary:     Jenkins support scripts 
Version:     1.0.0
Release:     1
Group:       Development/Tools
License:     LGPL v2.1
BuildArch:   noarch
URL:         http://safrm.net/projects/jenkins-support-scripts
Vendor:      Miroslav Safr <miroslav.safr@gmail.com>
Source0:     %{name}-%{version}.tar.bz2
Autoreq:     on
Autoreqprov: on
Requires:    gpg
Requires:    yum-utils
Requires:    createrepo
Requires:    tidy
Requires:    libxml2
Requires:    libxslt
Requires:    docbook-xsl-stylesheets
Requires:    docbook-dtds
BuildRequires:  libxslt
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook-dtds
BuildRequires:  appver >= 1.1.1

#buildroot fix for older distros
%if 0%{?suse_version} <= 1200 || 0%{?fedora} < 18 || 0%{?rhel_version} < 500 || 0%{?centos_version} < 500
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: gnupg2
%endif

%description
Jenkins common tasks support scripts

%prep
%setup -c -n ./%{name}-%{version}

%build
./jss-docs-update ./doc -sv %{version}

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/usr/bin
install -m 755 ./jss-debrepo-signcheck %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-debrepo-signcheck && rm -f %{buildroot}/usr/bin/jss-debrepo-signcheck.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-debrepo-signcheck && rm -f %{buildroot}/usr/bin/jss-debrepo-signcheck.bkp
install -m 755 ./jss-debrepo-update %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-debrepo-update && rm -f %{buildroot}/usr/bin/jss-debrepo-update.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-debrepo-update && rm -f %{buildroot}/usr/bin/jss-debrepo-update.bkp
install -m 755 ./jss-html-validator %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-html-validator && rm -f %{buildroot}/usr/bin/jss-html-validator.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-html-validator && rm -f %{buildroot}/usr/bin/jss-html-validator.bkp
install -m 755 ./jss-jenkins-backup %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-jenkins-backup && rm -f %{buildroot}/usr/bin/jss-jenkins-backup.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-jenkins-backup && rm -f %{buildroot}/usr/bin/jss-jenkins-backup.bkp
install -m 755 ./jss-rpmrepo-update %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-rpmrepo-update && rm -f %{buildroot}/usr/bin/jss-rpmrepo-update.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-rpmrepo-update && rm -f %{buildroot}/usr/bin/jss-rpmrepo-update.bkp
install -m 755 ./jss-xml-validator %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-xml-validator && rm -f %{buildroot}/usr/bin/jss-xml-validator.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-xml-validator && rm -f %{buildroot}/usr/bin/jss-xml-validator.bkp

install -m 755 ./jss-docs-update %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-docs-update && rm -f %{buildroot}/usr/bin/jss-docs-update.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-docs-update && rm -f %{buildroot}/usr/bin/jss-docs-update.bkp

#documentation
MANPAGES=`find ./doc/manpages -type f`
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 $MANPAGES %{buildroot}%{_mandir}/man1

%clean
rm -fr %{buildroot}

%check
for TEST in $(  grep -r -l -h "#\!/bin/sh" . )
do
		sh -n $TEST
		if  [ $? != 0 ]; then
			echo "syntax error in $TEST, exiting.." 
			exit 1
		fi
done 

%files
%defattr(-,root,root,-)
%{_bindir}/jss-debrepo-signcheck
%{_bindir}/jss-debrepo-update
%{_bindir}/jss-docs-update
%{_bindir}/jss-html-validator
%{_bindir}/jss-jenkins-backup
%{_bindir}/jss-rpmrepo-update
%{_bindir}/jss-xml-validator

#man pages
%{_mandir}/man1/jenkins-support-scripts.1*
%{_mandir}/man1/jss-debrepo-signcheck.1*
%{_mandir}/man1/jss-debrepo-update.1*
%{_mandir}/man1/jss-html-validator.1*
%{_mandir}/man1/jss-jenkins-backup.1*
%{_mandir}/man1/jss-rpmrepo-update.1*
%{_mandir}/man1/jss-xml-validator.1*
%{_mandir}/man1/jss-docs-update.1*


