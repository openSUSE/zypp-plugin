.PHONY:	default_target package tarball

TARBALL=package/zypp-plugin.tar.bz2

default_target: package

package: tarball

tarball:
	git archive --format=tar --prefix=zypp-plugin/ HEAD | bzip2 -c >$(TARBALL)

clean:
	rm -f $(TARBALL)
