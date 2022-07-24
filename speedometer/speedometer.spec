%{?!python3_pkgversion:%global python3_pkgversion 3}

Name:           speedometer
Version:        2.9
Release:        1%{?dist}
Summary:        Measure and display the rate of data across a network connection or data being stored in a file
License:        LGPLv2+
URL:            https://excess.org/speedometer/
Source0:        https://github.com/wardi/speedometer/archive/refs/tags/release-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
%{summary}.


%prep
%autosetup -n %{name}-release-%{version}


%build
%py3_build


%install
%py3_install
mv %{buildroot}%{_bindir}/speedometer{.py,}

%files
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/Speedometer-%{version}-py%{python3_version}.egg-info/


%changelog
* Sun Jul 24 2022 zhullyb <zhullyb@outlook.com>
- First Version.
