%define         _electronver        electron17

Name:           nodejs-%{_electronver}-bin
Version:        17.4.9
Release:        1%{?dist}
Summary:        Build cross-platform desktop apps with JavaScript, HTML, and CSS
License:        MIT
Url:            https://github.com/electron/electron
Source0:        %{url}/releases/download/v%{version}/electron-v%{version}-linux-x64.zip
Source1:        electron-launcher.sh
Source2:        https://raw.githubusercontent.com/electron/electron/main/LICENSE

BuildRequires:  bsdtar

Provides:       nodejs-%{_electronver} %{_electronver}

AutoReqProv: no

%description
Build cross-platform desktop apps with JavaScript, HTML, and CSS

%prep
install -Dm644 %{S:2} %{_builddir}/

%build
sed -i "s|@ELECTRONVER@|%{_electronver}|" %{S:1}

%install
install -dm755 %{buildroot}%{_datadir}/%{_electronver}
bsdtar -xf %{SOURCE0} -C %{buildroot}%{_datadir}/%{_electronver}

chmod u+s %{buildroot}%{_datadir}/%{_electronver}/chrome-sandbox

install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/%{_electronver}

%files
%license LICENSE
%{_bindir}/%{_electronver}
%{_datadir}/%{_electronver}/

%changelog
* Fri Jul 15 2022 zhullyb <zhullyb@outlook.com> - 17.4.9-1
- new version

* Sun Jul 10 2022 zhullyb <zhullyb@outlook.com> - 17.4.10-1
- new version

* Wed Jun 22 2022 zhullyb <zhullyb@outlook.com> - 17.4.8-1
- new version

* Fri Jun 03 2022 zhullyb <zhullyb@outlook.com> - 17.4.7-1
- new version

* Thu May 26 2022 zhullyb <zhullyb@outlook.com> - 17.4.6-1
- new version

* Thu May 19 2022 zhullyb <zhullyb@outlook.com> - 17.4.5-1
- new version

* Sat May 14 2022 zhullyb <zhullyb@outlook.com> - 17.4.4-1
- new version

* Thu May 05 2022 zhullyb <zhullyb@outlook.com> - 17.4.3-1
- new version

* Fri Apr 29 2022 zhullyb <zhullyb@outlook.com> - 17.4.2-1
- new version

* Wed Apr 20 2022 zhullyb <zhullyb@outlook.com> - 17.4.1-1
- new version

* Wed Apr 06 2022 zhullyb <zhullyb@outlook.com> - 17.4.0-1
- new version

* Sun Apr 03 2022 zhullyb <zhullyb@outlook.com> - 17.3.1-2
- rebuilt

* Sun Apr 03 2022 zhullyb <zhullyb@outlook.com> - 17.3.1-1
- new version


