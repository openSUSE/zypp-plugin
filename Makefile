.PHONY:	default_target package tarball

VERSION=$(shell awk '/^Version:/{print $$2}' package/*.spec)
TARBALL=package/zypp-plugin-$(VERSION).tar.bz2

default_target: package

package: tarball

tarball:
	git archive --format=tar --prefix=zypp-plugin/ HEAD | bzip2 -c >$(TARBALL)

clean:
	rm -f $(TARBALL)
