#
# spec file for package zypp-plugin
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%if 0%{?suse_version} >= 1320
%global build_py3 1
%endif

Name:           zypp-plugin
Version:        0.6
Release:        0
Url:            https://gitorious.org/opensuse/zypp-plugin
Summary:        Helper that makes writing ZYpp plugins easier
License:        GPL-2.0
Group:          System/Packages
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2
%if 0%{?suse_version} >= 1210
BuildArch:      noarch
%endif

%description
Empty main package. Helper for different languages reside in subpackages.

%prep
%setup -q -n zypp-plugin

%build

%install
%{__mkdir_p} %{buildroot}%{python_sitelib}
%{__install} python/zypp_plugin.py %{buildroot}%{python_sitelib}/zypp_plugin.py
%py_compile -O %{buildroot}/%{python_sitelib}
%if 0%{?build_py3}
%{__mkdir_p} %{buildroot}%{python3_sitelib}
%{__install} python/zypp_plugin.py %{buildroot}%{python3_sitelib}/zypp_plugin.py
%py3_compile -O %{buildroot}/%{python3_sitelib}
%endif

%if 0%{?build_py3}
%package -n python3-%{name}
Summary:        Helper that makes writing ZYpp plugins in python easier
Group:          System/Packages
Requires:       python3
BuildRequires:  python3-devel

%description -n python3-%{name}
This API allows writing ZYpp plugins by just subclassing from a python class
and implementing the commands you want to respond to as python methods.
%endif

%package python
Summary:        Helper that makes writing ZYpp plugins in python easier
Group:          System/Packages
Provides:       python2-%{name}
BuildRequires:  python-devel
Requires:       python

%description python
This API allows writing ZYpp plugins by just subclassing from a python class
and implementing the commands you want to respond to as python methods.

%files python
%defattr(-,root,root)
%doc COPYING
%{python_sitelib}/*

%if 0%{?build_py3}
%files -n python3-%{name}
%defattr(-,root,root)
%doc COPYING
%{python3_sitelib}/*
%endif

%changelog
