%{?!python3_pkgversion:%global python3_pkgversion 3}

Name:           python3-mpv
Version:        0.5.2
Release:        1%{?dist}
Summary:        Python interface to the awesome mpv media player
License:        AGPLv3
URL:            https://github.com/jaseg/python-mpv
Source0:        https://files.pythonhosted.org/packages/source/p/python-mpv/python-mpv-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       mpv-libs
%{?python_enable_dependency_generator}

%description
%{summary}.

%prep
%autosetup -p1 -n python-mpv-%{version}


%build
%py3_build


%install
%py3_install

%files
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/python_mpv-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/mpv.py

%changelog
* Sat May 14 2022 zhullyb <zhullyb@outlook.com>
- First build.
