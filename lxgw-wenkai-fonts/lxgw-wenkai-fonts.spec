Name:           lxgw-wenkai-fonts
Version:        1.233.2
Release:        1%{?dist}
Summary:        An open-source Chinese font derived from Fontworks' Klee One.
License:        OFL-1.1
Url:            https://github.com/lxgw/LxgwWenKai
Source0:        %{url}/releases/download/v%{version}/LXGWWenKai-Bold.ttf
Source1:        %{url}/releases/download/v%{version}/LXGWWenKai-Light.ttf
Source2:        %{url}/releases/download/v%{version}/LXGWWenKai-Regular.ttf
Source3:        %{url}/releases/download/v%{version}/LXGWWenKaiMono-Bold.ttf
Source4:        %{url}/releases/download/v%{version}/LXGWWenKaiMono-Light.ttf
Source5:        %{url}/releases/download/v%{version}/LXGWWenKaiMono-Regular.ttf
Source6:        https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/License.txt
BuildRequires:  fontpackages-devel
BuildArch:      noarch

%description
An open-source Chinese font derived from Fontworks' Klee One.

%prep
%define _ttfontsdir /usr/share/fonts/lxgw-wenkai/

%build
cp %{S:6} ./LICENSE

%install
install -d %{buildroot}%{_ttfontsdir}
install -m 644 %{S:0} %{buildroot}%{_ttfontsdir}
install -m 644 %{S:1} %{buildroot}%{_ttfontsdir}
install -m 644 %{S:2} %{buildroot}%{_ttfontsdir}
install -m 644 %{S:3} %{buildroot}%{_ttfontsdir}
install -m 644 %{S:4} %{buildroot}%{_ttfontsdir}
install -m 644 %{S:5} %{buildroot}%{_ttfontsdir}

%files
%license LICENSE
%{_ttfontsdir}/*.ttf
%dir %{_ttfontsdir}

%changelog
* Tue Apr 05 2022 zhullyb <zhullyb@outlook.com> - 1.233.2-1
- new version

* Mon Apr 04 2022 zhullyb <zhullyb@outlook.com> - 1.233.1-1
- new version

* Fri Apr 01 2022 zhullyb <zhullyb@outlook.com> - 1.233-1
- new version

* Thu Mar 31 2022 zhullyb <zhullyb@outlook.com> - 1.232-1
- new version

* Tue Mar 22 2022 zhullyb <zhullyb@outlook.com> - 1.230-1
- new version

* Thu Feb 24 2022 zhullyb <zhullyb@outlook.com> - 1.211-1
- new version

