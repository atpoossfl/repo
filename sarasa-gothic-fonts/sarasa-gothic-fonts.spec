Name:           sarasa-gothic-fonts
Version:        0.36.2
Release:        1%{?dist}
Summary:        SARASA GOTHIC, a CJK programing font based on Iosevka, Inter and Source Han Sans
License:        OFL-1.1
Url:            https://github.com/be5invis/Sarasa-Gothic
Source0:        %{url}/releases/download/v%{version}/sarasa-gothic-ttc-%{version}.7z
Source1:        https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/master/LICENSE
BuildRequires:  fontpackages-devel
BuildRequires:  p7zip
BuildArch:      noarch

%description
%{summary}.

%prep
%setup -qcn %{name}-%{version}
cp %{S:1} ./
%define _ttfontsdir /usr/share/fonts/sarasa-gothic

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -m 644 *.ttc %{buildroot}%{_ttfontsdir}

%files
%license LICENSE
%{_ttfontsdir}/*.ttc
%dir %{_ttfontsdir}

%changelog
* Sun Apr 03 2022 zhullyb <zhullyb@outlook.com> - 0.36.2-1
- new version

* Tue Mar 22 2022 zhullyb <zhullyb@outlook.com> - 0.36.1-1
- new version

