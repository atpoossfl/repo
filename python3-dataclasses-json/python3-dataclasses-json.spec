%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname dataclasses-json

Name:           python-dataclasses-json
Version:        0.5.7
Release:        1%{?dist}
Summary:        Easily serialize Python Data Classes to and from JSON
License:        MIT
URL:            https://github.com/lidatong/dataclasses-json
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
%{summary}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
%{summary}.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install\

%files -n  python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/dataclasses_json/
%{python3_sitelib}/dataclasses_json-%{version}-py%{python3_version}.egg-info/
%{_bindir}/publish.py


%changelog
* Sat May 14 2022 zhullyb <zhullyb@outlook.com>
- First build
