%global debug_package %{nil}
%global     forgeurl    https://github.com/vector-im/element-web
Version:    1.10.14
%forgemeta

Name:           element-web
Release:        1%{?dist}
Summary:        A glossy Matrix collaboration client for the web.
URL:            %{forgeurl}
License:        ASL 2.0
Source0:        %{forgesource}

BuildRequires:  python
BuildRequires:  yarnpkg

BuildRequires:  nodejs >= 2:17
# https://rpm.nodesource.com/

BuildRequires:  git

%description
%{summary}.

%prep
%forgeautosetup
yarn install --no-fund

%build
export NODE_OPTIONS=--openssl-legacy-provider
VERSION=%{version} yarn build --offline

%install
install -d %{buildroot}%{_datadir}/webapps/element
install -d %{buildroot}%{_sysconfdir}/webapps/element

cp -r webapp/* %{buildroot}%{_datadir}/webapps/element/
install -Dm644 config.sample.json -t %{buildroot}%{_sysconfdir}/webapps/element/
ln -s /etc/webapps/element/config.json %{buildroot}%{_datadir}/webapps/element/
echo %{version} > %{buildroot}%{_datadir}/webapps/element/version

%files
%license    LICENSE
%{_sysconfdir}/webapps/element/
%{_datadir}/webapps/element/

%changelog
* Tue Jun 07 2022 zhullyb <zhullyb@outlook.com> - 1.10.14-1
- new version

* Wed May 25 2022 zhullyb <zhullyb@outlook.com> - 1.10.13-1
- new version

* Wed May 11 2022 zhullyb <zhullyb@outlook.com> - 1.10.12-1
- new version
- add NODE_OPTIONS to fit openssl on Fedora 36.

* Tue Apr 26 2022 zhullyb <zhullyb@outlook.com> - 1.10.11-1
- new version

* Thu Apr 14 2022 zhullyb <zhullyb@outlook.com> - 1.10.10-1
- new version

* Tue Apr 12 2022 zhullyb <zhullyb@outlook.com> - 1.10.9-1
- new version

* Mon Apr 04 2022 zhullyb <zhullyb@outlook.com> - 1.10.8-1
- First build.
