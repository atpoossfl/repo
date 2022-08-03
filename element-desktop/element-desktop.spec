%global debug_package %{nil}
%global     forgeurl    https://github.com/vector-im/element-desktop
Version:    1.11.2
%forgemeta

%define     _electronver    electron17

Name:           element-desktop
Release:        1%{?dist}
Summary:        A glossy Matrix collaboration client for desktop.
URL:            %{forgeurl}
License:        ASL 2.0
Source0:        %{forgesource}
Source1:        element-desktop-launcher.sh
Source2:        io.element.Element.desktop
Patch0:         autolaunch.patch

Requires:       %{_electronver}
Requires:       element-web = %{version}
Requires:       sqlcipher
BuildRequires:  python
BuildRequires:  /usr/bin/yarn
BuildRequires:  gcc-c++
BuildRequires:  nodejs
BuildRequires:  git
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  tcl-devel
BuildRequires:  libsecret-devel
BuildRequires:  sqlcipher-devel

%description
%{summary}.

%prep
%forgeautosetup -p1
sed -i "s|@ELECTRON@|%{_electronver}|" %{S:1}
sed -i 's|"target": "deb"|"target": "dir"|' package.json
sed -i 's|"https://packages.element.io/desktop/update/"|null|' element.io/release/config.json
yarn install --no-fund

%build
yarn run build:native
yarn run build

%install
install -d %{buildroot}%{_datadir}/element
install -d %{buildroot}%{_sysconfdir}/webapps/element
# Install the app content, replace the webapp with a symlink to the system package
cp -r dist/linux-unpacked/resources/* %{buildroot}%{_datadir}/element/
ln -s /usr/share/webapps/element %{buildroot}%{_datadir}/element/webapp
# Config file
ln -s /etc/element/config.json %{buildroot}%{_sysconfdir}/webapps/element/config.json
install -Dm644 element.io/release/config.json -t %{buildroot}%{_sysconfdir}/element
# Required extras
install -Dm644 %{S:2} -t %{buildroot}%{_datadir}/applications/
install -Dm755 %{S:1} %{buildroot}%{_bindir}/%{name}
# Icons
for i in 16 24 48 64 96 128 256 512; do
    install -Dm644 build/icons/${i}x${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/io.element.Element.png
done

%files
%license    LICENSE
%config(noreplace) %{_sysconfdir}/element/config.json
%{_bindir}/%{name}
%{_sysconfdir}/webapps/element/config.json
%{_datadir}/element
%{_datadir}/applications/io.element.Element.desktop
%{_datadir}/icons/hicolor/*/apps/io.element.Element.png

%changelog
* Wed Aug 03 2022 zhullyb <zhullyb@outlook.com> - 1.11.2-1
- new version
- regenerate autolaunch.patch

* Sun Jul 10 2022 zhullyb <zhullyb@outlook.com> - 1.11.0-1
- new version

* Tue Jun 14 2022 zhullyb <zhullyb@outlook.com> - 1.10.15-1
- new version

* Tue Jun 07 2022 zhullyb <zhullyb@outlook.com> - 1.10.14-1
- new version
- remove the patch that use system sqlcipher, because upstream has merged that.

* Wed May 25 2022 zhullyb <zhullyb@outlook.com> - 1.10.13-1
- new version

* Sat May 14 2022 zhullyb <zhullyb@outlook.com> - 1.10.12-1
- new version

* Sat May 14 2022 zhullyb <zhullyb@outlook.com> - 1.10.11-2
- Stop building statically-linked sqlcipher

* Tue Apr 26 2022 zhullyb <zhullyb@outlook.com> - 1.10.11-1
- new version

* Thu Apr 14 2022 zhullyb <zhullyb@outlook.com> - 1.10.10-1
- new version

* Tue Apr 12 2022 zhullyb <zhullyb@outlook.com> - 1.10.9-1
- new version

* Mon Apr 04 2022 zhullyb <zhullyb@outlook.com> - 1.10.8-1
- First build.
