Name:           fcitx5-pinyin-moegirl
Version:        20220514
Release:        1%{?dist}
Summary:        Fcitx 5 pinyin dictionary generator for MediaWiki instances. (Releases for demo dict of zh.moegirl.org.cn)
License:        Unlicense;CC-BY-NC-SA-3.0
Url:            https://github.com/outloudvi/mw2fcitx
Source0:        %{url}/releases/download/%{version}/moegirl.dict
Source1:        https://raw.githubusercontent.com/outloudvi/mw2fcitx/master/LICENSE
BuildArch:      noarch

Recommends:     fcitx5

%description
%{summary}.

%prep
%define BUILD_DIR %{_builddir}/%{name}-%{version}

%build
cp %{_sourcedir}/LICENSE %{_builddir}/LICENSE

%install
install -Dm644 %{SOURCE0} -t %{buildroot}%{_datadir}/fcitx5/pinyin/dictionaries/

%files
%license LICENSE
%{_datadir}/fcitx5/pinyin/dictionaries/moegirl.dict

%changelog
* Sat May 14 2022 zhullyb <zhullyb@outlook.com> - 20220514-1
- new version

* Fri Apr 15 2022 zhullyb <zhullyb@outlook.com> - 20220414-1
- new version

* Tue Mar 15 2022 zhullyb <zhullyb@outlook.com> - 20220314-1
- new version

* Fri Feb 18 2022 zhullyb <zhullyb@outlook.com> - 20220218-1
- new version

* Tue Jan 18 2022 zhullyb <zhullyb@outlook.com> - 20220114-1
- First build


