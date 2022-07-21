%global srcurl  https://github.com/cslarsen/%{name}

Name:           jp2a
Version:        1.1.1
Release:        1%{?dist}
Summary:        Small utility that converts JPG images to ASCII (text) using libjpeg

License:        GPLv2+
URL:            https://github.com/Talinx/jp2a
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  autoconf autoconf-archive automake gcc
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
Recommends:     %{name}-bash-completion

%description
jp2a is a simple JPEG to ASCII converter. jp2a is very flexible.
It can use ANSI colors and html in output.
jp2a can also download and convert images from Internet via command line.

%package bash-completion
Summary:        bash completion files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       bash

%description bash-completion
This package installs %{summary}.

%prep
%autosetup
autoreconf -vi


%build
bashcompdir=/usr/share/bash-completion/completions %configure --with-jpeg-prefix=%{_prefix}
%make_build


%install
%make_install


%check
make %{?_smp_mflags} check


%files
%license COPYING
%doc LICENSES
%doc AUTHORS BUGS ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files bash-completion
%{_datadir}/bash-completion/completions/jp2a

%changelog
* Thu Jul 21 2022 zhullyb <zhullyb@outlook.com> - 1.1.1-1
- new version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jun 17 2017 Raphael Groner <projects.rg@smart.ms> - 1.0.7-1
- initial
