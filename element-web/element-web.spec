%global debug_package %{nil}
%global     forgeurl    https://github.com/vector-im/element-web
Version:    1.11.2
%forgemeta

Name:           element-web
Release:        1%{?dist}
Summary:        A glossy Matrix collaboration client for the web.
URL:            %{forgeurl}
License:        ASL 2.0
Source0:        %{forgesource}

BuildRequires:  python
BuildRequires:  /usr/bin/yarn
BuildRequires:  nvm
BuildRequires:  git

%description
%{summary}.

%prep
%forgeautosetup

%build
_ensure_local_nvm() {
  which nvm >/dev/null 2>&1 && nvm deactivate && nvm unload
  export NVM_DIR="%{_builddir}/.nvm"

  # The init script returns 3 if version specified
  # in ./.nvrc is not installed in $NVM_DIR
  # but nvm itself still gets loaded ok
  source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]
}

_ensure_local_nvm
nvm install 17

yarn install --no-fund
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
* Wed Aug 03 2022 zhullyb <zhullyb@outlook.com> - 1.11.2-1
- new version
- use nvm install of nodejs 17

* Sun Jul 10 2022 zhullyb <zhullyb@outlook.com> - 1.11.0-1
- new version

* Tue Jun 14 2022 zhullyb <zhullyb@outlook.com> - 1.10.15-1
- new version

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
