srpm:
	mkdir -p /builddir/build/SOURCES
	curl -L https://github.com/ahmetb/kubectx/archive/refs/tags/v0.9.4.tar.gz -o /builddir/build/SOURCES/v0.9.4.tar.gz
	rpmbuild -bs kubectx.spec
	cp /builddir/build/SRPMS/*.src.rpm $(outdir)
