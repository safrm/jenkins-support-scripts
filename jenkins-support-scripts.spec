%define APP_BUILD_DATE %(date +'%%Y%%m%%d_%%H%%M')

Name:        jenkins-support-scripts
Summary:     Jenkins support scripts 
Version:     1.0.0
Release:     1
Group:       System/Libraries
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
BuildRequires:  libxslt
BuildRequires: docbook-xsl-stylesheets
BuildRequires:  appver >= 1.1.1

%description
Jenkins common tasks support scripts

%prep
%setup -c -n ./%{name}-%{version}

%build
cd doc && ./update_docs.sh %{version} && cd -

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


#documentation
MANPAGES=`find ./doc/manpages -type f`
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 $MANPAGES %{buildroot}%{_mandir}/man1

DOCS="./README ./LICENSE.LGPL"
install -d -m 755 %{buildroot}%{_docdir}/jenkins-support-scripts
install -m 644 $DOCS %{buildroot}%{_docdir}/jenkins-support-scripts
sed -i".bkp" "1,/Version: /s/Version:   */Version:   %{version} %{APP_BUILD_DATE}/"  %{buildroot}%{_docdir}/jenkins-support-scripts/README && rm -f %{buildroot}%{_docdir}/jenkins-support-scripts/README.bkp

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
%{_bindir}/jss-html-validator
%{_bindir}/jss-jenkins-backup
%{_bindir}/jss-rpmrepo-update

#man pages
%{_mandir}/man1/gr-authorcheck.1*
%{_mandir}/man1/gr-branches.1*
%{_mandir}/man1/gr-clean.1*
%{_mandir}/man1/gr-commits2tag.1*
%{_mandir}/man1/gr-gr.1*
%{_mandir}/man1/gr-initbare.1*
%{_mandir}/man1/gr-pull.1*
%{_mandir}/man1/gr-pullreset.1*
%{_mandir}/man1/gr-remotes.1*
%{_mandir}/man1/gr-scripts.1*
%{_mandir}/man1/gr-show.1*
%{_mandir}/man1/gr-showlocal.1*
%{_mandir}/man1/gr-tags.1*

#other docs
%dir %{_docdir}/jenkins-support-scripts
%{_docdir}/jenkins-support-scripts/README
%{_docdir}/jenkins-support-scripts/LICENSE.LGPL

