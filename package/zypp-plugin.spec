#
Name:		zypp-plugin-python
Version:	0.3
Release:	0
Group:		System/Packages
License:	GPLv2
Url:		https://gitorious.org/opensuse/zypp-plugin
Summary:	Helper that makes writing ZYpp plugins in python easier
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:	zypp-plugin.tar.bz2

# Actually libzypp(plugin) should be required. Unfortunately the corresponing
# provides was introduced to late for SUSE Manager/SLE-11-SP1. We do not want to
# enforce libzypp update to satisfy this, so the Requires should saty disabled,
# until libzypp on SUSE Manager/SLE-11-SP1 was updated and provides libzypp(plugin).
#Requires:	libzypp(plugin)
BuildRequires:	python-devel
Requires:	python

%description
This API allows writing ZYpp plugins by just subclassing from a python class
and implementing the commands you want to respond to as python methods.

%prep
%setup -q -n zypp-plugin

%build

%install
%{__mkdir_p} %{buildroot}%{py_sitedir}
%{__install} python/zypp_plugin.py %{buildroot}%{py_sitedir}/zypp_plugin.py

%files
%defattr(-,root,root)
%{py_sitedir}/zypp_plugin.py
