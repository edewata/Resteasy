srpm:
	dnf install -y git
	.copr/build-srpm.sh
	mv /builddir/build/SRPMS/* ${outdir}
