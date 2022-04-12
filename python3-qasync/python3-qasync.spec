%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname qasync

Name:           python%{python3_pkgversion}-%{srcname}
Version:        0.23.0
Release:        1%{?dist}
Summary:        Python library for using asyncio in Qt-based applications.
License:        BSD
URL:            https://github.com/CabbageDevelopment
Source0:        %{url}/qasync/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
%{summary}.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build


%install
%py3_install

%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Mon Apr 11 2022 zhullyb <zhullyb@outlook.com> - 0.23.0-1
- First build.
