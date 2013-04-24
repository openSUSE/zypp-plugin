#
# spec file for package zypp-plugin
#
# Copyright (c) 2011-2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
Name:		zypp-plugin
Version:	0.3
Release:	0
Group:		System/Packages
License:	GPL-2.0
Url:		https://gitorious.org/opensuse/zypp-plugin
Summary:	Helper that makes writing ZYpp plugins easier
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:	%{name}-%{version}.tar.bz2

# Actually libzypp(plugin) should be required. Unfortunately the corresponing
# provides was introduced to late for SUSE Manager/SLE-11-SP1. We do not want to
# enforce libzypp update to satisfy this, so the Requires should saty disabled,
# until libzypp on SUSE Manager/SLE-11-SP1 was updated and provides libzypp(plugin).
#Requires:	libzypp(plugin)
BuildRequires:	python-devel
Requires:	python

%{?!py_sitearch: %global py_sitearch %(python -c 'from distutils.sysconfig import get_python_lib; print get_python_lib(True)')}

%description
Empty main package. Helper for different languages reside in subpackages.

%package python
Group:		System/Packages
License:	GPL-2.0
Summary:	Helper that makes writing ZYpp plugins in python easier

%description python
This API allows writing ZYpp plugins by just subclassing from a python class
and implementing the commands you want to respond to as python methods.

%prep
%setup -q -n zypp-plugin

%build

%install
%{__mkdir_p} %{buildroot}%{py_sitearch}
%{__install} python/zypp_plugin.py %{buildroot}%{py_sitearch}/zypp_plugin.py
%if 0%{?suse_version}
pushd $RPM_BUILD_ROOT/%{python_sitearch}
python %py_libdir/py_compile.py *.py
python -O %py_libdir/py_compile.py *.py
popd
%endif

%files python
%defattr(-,root,root)
%{py_sitearch}/*
