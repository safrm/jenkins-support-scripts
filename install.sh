#/bin/sh
#jenkins support scripts - http://safrm.net/projects/jenkins-support-scripts
#author:  Miroslav Safr <miroslav.safr@gmail.com>
#
BINDIR=/usr/bin
COMPLETION_DIR=/etc/bash_completion.d
MANDIR=/usr/share/man

#root check
USERID=`id -u`
[ $USERID -eq "0" ] || {
    echo "I cannot continue, you should be root or run it with sudo!"
    exit 0
}

#automatic version
if command -v appver 1>/dev/null 2>&1; then . appver; else APP_SHORT_VERSION=NA ; APP_FULL_VERSION_TAG=NA ; APP_BUILD_DATE=`date +'%Y%m%d_%H%M'`; fi

for TEST in $(  grep -r -l -h "#\!/bin/sh" --exclude-dir=.git . )
do
		sh -n $TEST
		if  [ $? != 0 ]; then
			echo "syntax error in $TEST, exiting.." 
			exit 1
		fi
done

#update documentation
./jss-docs-update ./doc

mkdir -p -m 0755 $BINDIR

install -m 0777 -v ./jss-backup  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-backup && rm -f $BINDIR/jss-backup.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-backup && rm -f $BINDIR/jss-backup.bkp

install -m 0777 -v ./jss-debrepo-update  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-debrepo-update && rm -f $BINDIR/jss-debrepo-update.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-debrepo-update && rm -f $BINDIR/jss-debrepo-update.bkp
install -m 0777 -v ./jss-debrepo-signcheck  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-debrepo-signcheck && rm -f $BINDIR/jss-debrepo-signcheck.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-debrepo-signcheck && rm -f $BINDIR/jss-debrepo-signcheck.bkp
install -m 0777 -v ./jss-debrepo-repomanage  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-debrepo-repomanage && rm -f $BINDIR/jss-debrepo-repomanage.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-debrepo-repomanage && rm -f $BINDIR/jss-debrepo-repomanage.bkp

install -m 0777 -v ./jss-html-validator  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-html-validator && rm -f $BINDIR/jss-html-validator.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-html-validator && rm -f $BINDIR/jss-html-validator.bkp

install -m 0777 -v ./jss-jenkins-backup  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-jenkins-backup && rm -f $BINDIR/jss-jenkins-backup.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-jenkins-backup && rm -f $BINDIR/jss-jenkins-backup.bkp

install -m 0777 -v ./jss-rpmrepo-update  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-rpmrepo-update && rm -f $BINDIR/jss-rpmrepo-update.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-rpmrepo-update && rm -f $BINDIR/jss-rpmrepo-update.bkp

install -m 0777 -v ./jss-xml-validator  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-xml-validator && rm -f $BINDIR/jss-xml-validator.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-xml-validator && rm -f $BINDIR/jss-xml-validator.bkp

install -m 0777 -v ./jss-docs-update  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-docs-update && rm -f $BINDIR/jss-docs-update.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-docs-update && rm -f $BINDIR/jss-docs-update.bkp

install -m 0777 -v ./jss-jenkins-watchdog  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-jenkins-watchdog && rm -f $BINDIR/jss-jenkins-watchdog.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-jenkins-watchdog && rm -f $BINDIR/jss-jenkins-watchdog.bkp

mkdir -p -m 0755 $COMPLETION_DIR
install -m 0777 -v ./jss_completion  $COMPLETION_DIR/

MANPAGES=`find ./doc/manpages -type f`
install -d -m 755 $MANDIR/man1
install -m 644 $MANPAGES $MANDIR/man1

