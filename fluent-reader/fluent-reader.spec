%global debug_package %{nil}

%global forgeurl    https://github.com/yang991178/fluent-reader/
Version:        1.1.0
%forgemeta

Name:           fluent-reader
Release:        1%{?dist}
Summary:        Modern desktop RSS reader built with Electron, React, and Fluent UI

License:        BSD
URL:            https://hyliu.me/fluent-reader/
Source0:        %{forgesource}
Source1:        fluent-reader-wrapper.sh
Source2:        fluent-reader.desktop

BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  desktop-file-utils
Requires:       electron16

%description
%{summary}.

%prep
%autosetup


%build
npm install
export NODE_ENV=production
npm run build
node_modules/.bin/electron-builder --linux dir -p never

%install
install -Dm644 bin/linux/x64/linux-unpacked/resources/app.asar -t %{buildroot}%{_datadir}/%{name}/
install -Dm755 %{S:1} %{buildroot}%{_bindir}/%{name}
install -Dm644 dist/icons/logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:2}

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Sun May 15 2022 zhullyb <zhullyb@outlook.com>
- First build.
