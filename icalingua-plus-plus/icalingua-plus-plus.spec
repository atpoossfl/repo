# Note: Npm depends on network. Network should be enabled when building this software.

%global debug_package %{nil}

Name:           icalingua-plus-plus
Version:        2.6.4
Release:        1%{?dist}
Summary:        A Linux client for QQ and more
License:        AGPL 3.0
Url:            https://github.com/Icalingua-plus-plus/Icalingua-plus-plus
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        icalingua-launcher.sh
Source2:        icalingua-plus-plus.desktop
Patch0:         icalingua-build-production.patch

Requires:       electron17

BuildRequires:  nodejs >= 2:17
# https://rpm.nodesource.com/

BuildRequires:  clang
BuildRequires:  yarnpkg
BuildRequires:  python

%description
%{summary}.

%prep
%setup -q -n Icalingua-plus-plus-%{version}
%patch0

%build
export NODE_OPTIONS=--openssl-legacy-provider
cd icalingua
yarn
yarn build:ci
yarn build:electron --dir -c.extraMetadata.version=%{version}

%install
install -Dm755 %{S:1} %{buildroot}%{_bindir}/icalingua++
install -Dm644 icalingua/build/linux-unpacked/resources/app.asar -t %{buildroot}%{_datadir}/icalingua-plus-plus/
cd pkgres
install -Dm644 512x512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/icalingua-plus-plus.png
install -Dm644 %{S:2} %{buildroot}%{_datadir}/applications/icalingua-plus-plus.desktop

%files
%license LICENSE
%{_bindir}/icalingua++
%{_datadir}/icalingua-plus-plus/
%{_datadir}/applications/icalingua-plus-plus.desktop
%{_datadir}/icons/hicolor/512x512/apps/icalingua-plus-plus.png

%changelog
* Sat Jun 04 2022 zhullyb <zhullyb@outlook.com> - 2.6.4-1
- new version

* Sun May 22 2022 zhullyb <zhullyb@outlook.com> - 2.6.3-1
- new version

* Wed May 11 2022 zhullyb <zhullyb@outlook.com> - 2.6.1-2
- add NODE_OPTIONS to fit openssl on Fedora 36.

* Sun Apr 03 2022 zhullyb <zhullyb@outlook.com> - 2.6.1-1
- new version

* Sun Apr 03 2022 zhullyb <zhullyb@outlook.com> - 2.6.0-2
- Move the path of this software

* Thu Mar 31 2022 zhullyb <zhullyb@outlook.com> - 2.6.0-1
- new version

* Fri Mar 18 2022 zhullyb <zhullyb@outlook.com> - 2.5.8-1
- New version
- Depend on electron17 now
- add LICENSE

* Wed Mar 09 2022 zhullyb <zhullyb@outlook.com> - 2.5.5-1
- First build.


