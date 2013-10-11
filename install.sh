#/bin/sh
#jss - jenkins support scripts
#author:  Miroslav Safr <miroslav.safr@gmail.com>
BINDIR=/usr/bin

#root check
USERID=`id -u`
[ $USERID -eq "0" ] || { 
    echo "I cannot continue, you should be root or run it with sudo!"
    exit 0
}
#automatic version 
if [ command -v appver >/dev/null 2>&1 ]; then . appver; else APP_FULL_VERSION_TAG=NA ; APP_BUILD_DATE=`date +'%Y%m%d_%H%M'`; fi

mkdir -p -m 0755 $BINDIR
install -m 0777 -v ./jss-jenkins-backup  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-jenkins-backup && rm -f $BINDIR/jss-jenkins-backup.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-jenkins-backup && rm -f $BINDIR/jss-jenkins-backup.bkp
install -m 0777 -v ./jss-rpmrepo-update  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/jss-rpmrepo-update && rm -f $BINDIR/jss-rpmrepo-update.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/jss-rpmrepo-update && rm -f $BINDIR/jss-rpmrepo-update.bkp

