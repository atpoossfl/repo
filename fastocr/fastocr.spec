%global debug_package %{nil}

%{?!python3_pkgversion:%global python3_pkgversion 3}
%global forgeurl https://github.com/BruceZhang1993/FastOCR
Version:         0.3.7
%forgemeta

Name:       fastocr
Release:    1%{?dist}
Summary:    FastOCR is a desktop application for OCR API.
URL:        %{forgeurl}
License:    LGPLv3
Source:     %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python3-qt5
%{?python_enable_dependency_generator}
Requires:       qt5-qtquickcontrols2

Provides:       python%{python3_pkgversion}-%{name} = %{version}
BuildArch:      noarch

%description
%{summary}.

%prep
%forgesetup

%build
%py3_build

%install
%py3_install
install -Dm644 fastocr/data/FastOCR.desktop %{buildroot}%{_datadir}/applications/FastOCR.desktop

%files
%license    LICENSE
%{_bindir}/fastocr
%{python3_sitelib}/%{name}*
%{_datadir}/applications/FastOCR.desktop

%changelog
* Tue May 03 2022 zhullyb <zhullyb@outlook.com> - 0.3.7-1
- new version

* Mon Apr 11 2022 zhullyb <zhullyb@outlook.com> - 0.3.6-1
- First build.
