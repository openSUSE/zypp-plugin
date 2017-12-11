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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
Name:           zypp-plugin
Version:        0.6.2
Release:        0
Summary:        Helper that makes writing ZYpp plugins easier
License:        GPL-2.0
Group:          System/Packages
URL:            https://github.com/openSUSE/zypp-plugin
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  %{python_module devel}
Requires:       python-base
BuildArch:      noarch
# provide old names for py2 package
%ifpython2
Obsoletes:      %{oldpython}-%{name} < %{version}
Provides:       %{oldpython}-%{name} = %{version}
Obsoletes:      %{name}-%{oldpython} < %{version}
Provides:       %{name}-%{oldpython} = %{version}
%endif
%python_subpackages

%description
This API allows writing ZYpp plugins by just subclassing from a python class
and implementing the commands you want to respond to as python methods.

%prep
%setup -q -n zypp-plugin

%build
:

%install
%ifpython2
mkdir -p %{buildroot}%{python_sitelib}
install python/zypp_plugin.py %{buildroot}%{python_sitelib}/zypp_plugin.py
%py_compile -O %{buildroot}/%{python_sitelib}
%endif
%if "%{python3_bin_suffix}" != ""
mkdir -p %{buildroot}%{python3_sitelib}
install python/zypp_plugin.py %{buildroot}%{python3_sitelib}/zypp_plugin.py
%py3_compile -O %{buildroot}/%{python3_sitelib}
%endif

%files %{python_files}
%doc COPYING
%{python_sitelib}/*

%changelog
