%global debug_package %{nil}

%global     forgeurl    https://github.com/jeffvli/sonixd
Version:        0.15.3
%forgemeta

%global     _electronver    electron13

Name:           sonixd
Release:        1%{?dist}
Summary:        A full-featured Subsonic/Jellyfin compatible desktop music player

License:        GPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        sonixd-wrapper.sh
Source2:        sonixd.desktop

BuildRequires:  nodejs
BuildRequires:  yarnpkg
BuildRequires:  desktop-file-utils
Requires:       electron13

%description
%{summary}.

%prep
%forgeautosetup
sed -i "s|@ELECTRON@|%{_electronver}|" %{S:1}

%build
yarn upgrade
yarn build
yarn run electron-builder --linux --x64

%install
install -Dm755 %{S:1} %{buildroot}%{_bindir}/sonixd
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:2}

pushd release/linux-unpacked/resources/
install -Dm644 app.asar -t %{buildroot}%{_datadir}/%{name}
cp -a assets %{buildroot}%{_datadir}/%{name}
popd

pushd assets/icons/
for size in 16 24 32 48 64 96 128 512 1024; do
    install -Dm644 ${size}x${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done
popd

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/sonixd.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Thu Jul 28 2022 zhullyb <zhullyb@outlook.com> - 0.15.3-1
- new version

* Sat May 14 2022 zhullyb <zhullyb@outlook.com>
- First build
