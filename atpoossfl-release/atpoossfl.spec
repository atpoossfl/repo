Name:       atpoossfl-release
Version:    1.1
Release:    1%{?dist}
Summary:    Another Thirdpary-Owned Open-source Software Source for Fedora Linux
License:    MIT
Group:      System Environment/Base
URL:        https://github.com/atpoossfl/repo
Source0:    atpoossfl.repo
Source1:    atpoossfl.mirrorlist
BuildArch:  noarch

%description
%{summary}.

%prep

%build

%install
install -Dm644 %{S:0} -t %{buildroot}%{_sysconfdir}/yum.repos.d/
install -Dm644 %{S:1} -t %{buildroot}%{_sysconfdir}/yum.repos.d/

%files
%defattr(-,root,root,-)
%dir /etc/yum.repos.d
%config(noreplace) %{_sysconfdir}/yum.repos.d/atpoossfl*

%changelog
* Mon Apr 04 2022 zhullyb <zhullyb@outlook.com> - 1-1
- First build.

