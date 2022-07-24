%global debug_package %{nil}

Name:           hollywood
Version:        1.21
Release:        1%{?dist}
Summary:        Fill your console with Hollywood melodrama technobabble

License:        CC0
URL:            https://github.com/dustinkirkland/hollywood
Source0:        https://launchpad.net/hollywood/trunk/%{version}/+download/hollywood_%{version}.orig.tar.gz
Source1:        LICENSE

Requires:       apg
Requires:       bmon
Requires:       byobu
Requires:       ccze
Requires:       cmatrix
Requires:       coreutils
Requires:       gawk
Requires:       htop
Requires:       jp2a
Requires:       man-db
Requires:       mlocate
Requires:       moreutils
Requires:       openssh
Requires:       speedometer
Requires:       tree
Requires:       util-linux

%description
%{summary}.

%prep
%autosetup


%build
cp %{S:1} .

%install
install -dm0755 %{buildroot}{%{_bindir},%{_prefix}/lib/hollywood,%{_datadir}/hollywood,%{_mandir}/man1}
install -m 0755 bin/hollywood  %{buildroot}%{_bindir}
install -m 0755 lib/hollywood/* %{buildroot}%{_prefix}/lib/hollywood
install -m 0644 share/hollywood/*  %{buildroot}%{_datadir}/hollywood
install -m 0644 {README,ChangeLog}  %{buildroot}%{_datadir}/hollywood
install -m 0644 share/man/man1/*  %{buildroot}%{_mandir}/man1

%files
%license LICENSE
%{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*

%changelog
* Sun Jul 24 2022 zhullyb <zhullyb@outlook.com>
- First Version.
