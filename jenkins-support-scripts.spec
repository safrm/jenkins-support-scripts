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
BuildRequires:  libxslt
BuildRequires:  appver >= 1.1.1
BuildRequires:  docbook-style-xsl
#BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook-dtds
Requires: jss-debrepo
Requires: jss-rpmrepo
Requires: jss-validators
Requires: jss-backup
Requires: jss-misc

#buildroot fix for older distros
%if 0%{?suse_version} <= 1200 || 0%{?fedora} < 18 || 0%{?rhel_version} < 500 || 0%{?centos_version} < 500
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%endif

%description
Jenkins common tasks support scripts

%package -n jss-common
Summary:    Jenkins support scripts  - common files
Group:      Development/Tools

%description -n jss-common
Jenkins support scripts  - common files


%package -n jss-debrepo
Summary:    Jenkins support scripts  - debian repositories helpers
Group:      Development/Tools
Requires:   jss-common = %{version}-%{release}

%description -n jss-debrepo
Jenkins support scripts  - debian repositories helpers


%package -n jss-rpmrepo
Summary:    Jenkins support scripts  - rpm repositories helpers
Group:      Development/Tools
Requires:   jss-common = %{version}-%{release}
Requires:   gpg
Requires:   yum-utils
Requires:   createrepo
Requires:   rpm
%if 0%{?suse_version} <= 1200 || 0%{?fedora} < 18 || 0%{?rhel_version} < 500 || 0%{?centos_version} < 500
Requires: gnupg2
%endif

%description -n jss-rpmrepo
Jenkins support scripts  - rpm repositories helpers


%package -n jss-validators
Summary:    Jenkins support scripts  - format and file validators
Group:      Development/Tools
Requires:   jss-common = %{version}-%{release}
Requires:   tidy
Requires:   libxml2
Requires:   libxslt

%description -n jss-validators
Jenkins support scripts  - format and file validators

%package -n jss-backup
Summary:    Jenkins support scripts  - backup helpers
Group:      Development/Tools
Requires:   jss-common = %{version}-%{release}

%description -n jss-backup
Jenkins support scripts  - backup helpers

%package -n jss-misc
Summary:    Jenkins support scripts  - miscellaneous helpers
Group:      Development/Tools
Requires:   jss-common = %{version}-%{release}
Requires:    docbook-dtds
Requires:    docbook-style-xsl
#Requires:    docbook-xsl-stylesheets
Requires:   libxslt

%description -n jss-misc
Jenkins support scripts  - miscellaneous helpers


%prep
%setup -c -n ./%{name}-%{version}

%build
./jss-docs-update ./doc -sv %{version}

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/usr/bin
install -m 755 ./jss-backup %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-backup && rm -f %{buildroot}/usr/bin/jss-backup.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-backup && rm -f %{buildroot}/usr/bin/jss-backup.bkp
install -m 755 ./jss-debrepo-signcheck %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-debrepo-signcheck && rm -f %{buildroot}/usr/bin/jss-debrepo-signcheck.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-debrepo-signcheck && rm -f %{buildroot}/usr/bin/jss-debrepo-signcheck.bkp
install -m 755 ./jss-debrepo-update %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-debrepo-update && rm -f %{buildroot}/usr/bin/jss-debrepo-update.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-debrepo-update && rm -f %{buildroot}/usr/bin/jss-debrepo-update.bkp
install -m 755 ./jss-debrepo-repomanage %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-debrepo-repomanage && rm -f %{buildroot}/usr/bin/jss-debrepo-repomanage.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-debrepo-repomanage && rm -f %{buildroot}/usr/bin/jss-debrepo-repomanage.bkp
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
install -m 755 ./jss-jenkins-watchdog %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-jenkins-watchdog && rm -f %{buildroot}/usr/bin/jss-jenkins-watchdog.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-jenkins-watchdog && rm -f %{buildroot}/usr/bin/jss-jenkins-watchdog.bkp
install -m 755 ./jss-watchdog %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-watchdog && rm -f %{buildroot}/usr/bin/jss-watchdog.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-watchdog && rm -f %{buildroot}/usr/bin/jss-watchdog.bkp
install -m 755 ./jss-mbm-checker %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/jss-mbm-checker && rm -f %{buildroot}/usr/bin/jss-mbm-checker.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/jss-mbm-checker && rm -f %{buildroot}/usr/bin/jss-mbm-checker.bkp

mkdir -p -m 0755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 0777 -v ./jss_completion %{buildroot}%{_sysconfdir}/bash_completion.d

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


%postun -n jss-backup
rm -fr /var/log/jss-watchdog

%files
%defattr(-,root,root,-)



%files -n jss-debrepo
%defattr(-,root,root,-)
%{_bindir}/jss-debrepo-signcheck
%{_bindir}/jss-debrepo-update
%{_bindir}/jss-debrepo-repomanage
%{_mandir}/man1/jss-debrepo-signcheck.1*
%{_mandir}/man1/jss-debrepo-repomanage.1*
%{_mandir}/man1/jss-debrepo-update.1*


%files -n jss-rpmrepo
%defattr(-,root,root,-)
%{_bindir}/jss-rpmrepo-update
%{_mandir}/man1/jss-rpmrepo-update.1*

%files -n jss-validators
%defattr(-,root,root,-)
%{_bindir}/jss-html-validator
%{_bindir}/jss-mbm-checker
%{_bindir}/jss-xml-validator
%{_mandir}/man1/jss-html-validator.1*
%{_mandir}/man1/jss-mbm-checker.1*
%{_mandir}/man1/jss-xml-validator.1*

%files -n jss-backup
%defattr(-,root,root,-)
%{_bindir}/jss-backup
%{_bindir}/jss-jenkins-backup
%{_mandir}/man1/jss-backup.1*
%{_mandir}/man1/jss-jenkins-backup.1*

%files -n jss-misc
%defattr(-,root,root,-)
%{_bindir}/jss-docs-update
%{_bindir}/jss-jenkins-watchdog
%{_bindir}/jss-watchdog
%{_mandir}/man1/jss-docs-update.1*
%{_mandir}/man1/jss-watchdog.1*
%{_mandir}/man1/jss-jenkins-watchdog.1*

%files -n jss-common
%defattr(-,root,root,-)
%{_sysconfdir}/bash_completion.d/jss_completion
%{_mandir}/man1/jenkins-support-scripts.1*
