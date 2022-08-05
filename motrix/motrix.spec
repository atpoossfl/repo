# Note: Npm depends on network. Network should be enabled when building this software.

%global debug_package %{nil}

Name:           motrix
Version:        1.6.11
Release:        4%{?dist}
Summary:        A full-featured download manager.
License:        MIT
Url:            https://github.com/agalwood/Motrix
Source0:        https://github.com/agalwood/Motrix/archive/refs/tags/v%{version}.tar.gz
Source1:        motrix-launcher.sh
Source2:        motrix.desktop
Source3:        motrix.xml

BuildRequires:  nvm
BuildRequires:  /usr/bin/yarn
Requires:       electron11

%description
A full-featured download manager.

%prep
%autosetup -n Motrix-%{version}

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
nvm install 14

yarn
yarn run build:dir

%install
install -Dm644 release/linux-unpacked/resources/app.asar -t "%{buildroot}%{_datadir}/motrix/"
cp -r release/linux-unpacked/resources/engine "%{buildroot}%{_datadir}/motrix/"
install -Dm644 static/512x512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/motrix.png
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/motrix
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/motrix.desktop
install -Dm644 %{SOURCE3} %{buildroot}%{_datadir}/mime/packages/motrix.xml

%files
%{_bindir}/motrix
%{_datadir}/motrix
%{_datadir}/applications/motrix.desktop
%{_datadir}/icons/hicolor/512x512/apps/motrix.png
%{_datadir}/mime/packages/motrix.xml

%changelog
* Fri Aug 05 2022 zhullyb <zhullyb@outlook.com> - 1.6.11-4
- use nodejs14 so we can remove the patch
- remove npm

* Thu Aug 04 2022 zhullyb <zhullyb@outlook.com> - 1.6.11-3
- use nvm to build successfullly

* Sun Apr 03 2022 zhullyb <zhullyb@outlook.com> - 1.6.11-2
- Move the path of this software

* Sat Mar 05 2022 zhullyb <zhullyb@outlook.com> - 1.6.11-1
- First build.


