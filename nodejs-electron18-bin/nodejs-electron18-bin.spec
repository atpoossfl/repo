%define         _electronver        electron18

Name:           nodejs-%{_electronver}-bin
Version:        18.3.8
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
* Wed Aug 10 2022 zhullyb <zhullyb@outlook.com> - 18.3.8-1
- new version

* Sun Jul 31 2022 zhullyb <zhullyb@outlook.com> - 18.3.6-1
- new version

* Thu Jun 23 2022 zhullyb <zhullyb@outlook.com> - 18.3.5-1
- new version

* Thu Jun 16 2022 zhullyb <zhullyb@outlook.com> - 18.3.4-1
- new version

* Fri Jun 10 2022 zhullyb <zhullyb@outlook.com> - 18.3.3-1
- new version

* Fri Jun 03 2022 zhullyb <zhullyb@outlook.com> - 18.3.2-1
- new version

* Thu May 26 2022 zhullyb <zhullyb@outlook.com> - 18.3.1-1
- new version

* Tue May 24 2022 zhullyb <zhullyb@outlook.com> - 18.3.0-1
- new version

* Thu May 19 2022 zhullyb <zhullyb@outlook.com> - 18.2.4-1
- new version

* Sat May 14 2022 zhullyb <zhullyb@outlook.com> - 18.2.3-1
- new version

* Wed May 11 2022 zhullyb <zhullyb@outlook.com> - 18.2.2-1
- new version

* Thu May 05 2022 OneToroto <onetoroto@outlook.com> - 18.2.1-1
- new version
