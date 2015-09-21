#/bin/sh
#jenkins support scripts - http://safrm.net/projects/jenkins-support-scripts
#author:  Miroslav Safr <miroslav.safr@gmail.com>
. appver-installer

appver_basic_scripts_test

$MKDIR_755 $BINDIR
$INSTALL_755 ./jss-backup $BINDIR
appver_update_version_and_date $BINDIR/jss-backup
$INSTALL_755 ./jss-debrepo-update $BINDIR
appver_update_version_and_date $BINDIR/jss-debrepo-update
$INSTALL_755 ./jss-debrepo-signcheck $BINDIR
appver_update_version_and_date $BINDIR/jss-debrepo-signcheck
$INSTALL_755 ./jss-debrepo-repomanage $BINDIR
appver_update_version_and_date $BINDIR/jss-debrepo-repomanage
$INSTALL_755 ./jss-html-validator $BINDIR
appver_update_version_and_date $BINDIR/jss-html-validator
$INSTALL_755 ./jss-jenkins-backup $BINDIR
appver_update_version_and_date $BINDIR/jss-jenkins-backup
$INSTALL_755 ./jss-rpmrepo-update $BINDIR
appver_update_version_and_date $BINDIR/jss-rpmrepo-update
$INSTALL_755 ./jss-xml-validator $BINDIR
appver_update_version_and_date $BINDIR/jss-xml-validator
$INSTALL_755 ./jss-docs-update $BINDIR
appver_update_version_and_date $BINDIR/jss-docs-update
$INSTALL_755 ./jss-watchdog $BINDIR
appver_update_version_and_date $BINDIR/jss-watchdog
$INSTALL_755 ./jss-jenkins-watchdog $BINDIR
appver_update_version_and_date $BINDIR/jss-jenkins-watchdog
$INSTALL_755 ./jss-mbm-checker $BINDIR
appver_update_version_and_date $BINDIR/jss-mbm-checker

$MKDIR_755 $COMPLETION_DIR
$INSTALL_755 ./jss_completion  $COMPLETION_DIR/

