%global debug_package %{nil}
%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname sublime-music

Name:           sublime-music
Version:        0.11.16
Release:        1%{?dist}
Summary:        A native Revel/Gonic/Subsonic/Airsonic/*sonic client for Linux. Built using Python and GTK+.
License:        GPLv3
URL:            https://sublimemusic.app
Source0:        https://gitlab.com/sumner/sublime-music/-/archive/v%{version}/sublime-music-v%{version}.tar.gz
Source1:        https://files.pythonhosted.org/packages/source/s/sublime-music/sublime_music-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx

%{?python_enable_dependency_generator}

%description
%{summary}.

%prep
%setup -b 0 -a 1 -q -T -n %{srcname}-v%{version}

%build
cd docs
make man
cd ../sublime_music-%{version}
%py3_build


%install
install -Dm644 docs/_build/man/sublime-music.1 %{buildroot}%{_datadir}/man/man1/sublime-music.1
pushd sublime_music-%{version}
%py3_install
popd

mkdir -p %{buildroot}%{_datadir}/%{srcname}/adapters/subsonic %{buildroot}%{_datadir}/%{srcname}/dbus %{buildroot}%{_datadir}/%{srcname}/ui
pushd %{buildroot}%{python3_sitelib}/sublime_music/
mv adapters/icons %{buildroot}%{_datadir}/%{srcname}/adapters
mv adapters/images %{buildroot}%{_datadir}/%{srcname}/adapters
mv adapters/subsonic/icons %{buildroot}%{_datadir}/%{srcname}/adapters/subsonic
mv dbus/mpris_specs %{buildroot}%{_datadir}/%{srcname}/dbus
mv ui/icons %{buildroot}%{_datadir}/%{srcname}/ui
mv ui/images %{buildroot}%{_datadir}/%{srcname}/ui
popd

desktop-file-install --dir=%{buildroot}%{_datadir}/applications sublime-music.desktop
install -Dm644 sublime-music.metainfo.xml %{buildroot}%{_datadir}/metainfo/sublime-music.metainfo.xml

pushd logo/rendered
for size in 16 22 32 48 64 72 96 128 192 512 1024; do
    install -Dm644 ${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/sublime-music.png
done
popd

%files
%license LICENSE
%{python3_sitelib}/sublime_music/
%{python3_sitelib}/sublime_music-%{version}-py%{python3_version}.egg-info/
%{_bindir}/%{srcname}
%{_datadir}/applications/sublime-music.desktop
%{_datadir}/%{srcname}/
%{_datadir}/icons/hicolor/*/apps/sublime-music.png
%{_datadir}/man/man1/sublime-music.1.gz
%{_datadir}/metainfo/sublime-music.metainfo.xml

%changelog
* Sat May 14 2022 zhullyb <zhullyb@outlook.com>
- First build.
