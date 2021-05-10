#!/bin/sh -x

pwd
ls -la

git rev-parse --short=8 HEAD

version=`git branch --show-current`
echo "Version: ${version}"

git archive \
    --format=tar.gz \
    --prefix Resteasy-${version}.Final/ \
    -o /builddir/build/SOURCES/resteasy-${version}.Final.tar.gz \
    HEAD

rpmbuild -bs resteasy.spec
