%global         debug_package           %{nil}

Name:           fcitx5-material-color
Version:        0.2.1
Release:        1%{?dist}
Summary:        Material color theme for fcitx5

License:        ASL 2.0
URL:            https://github.com/hosxy/Fcitx5-Material-Color
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

Requires:       fcitx5
BuildArch:	noarch

%description
%{summary}.

%prep
%autosetup -n Fcitx5-Material-Color-%{version}

%build

%install
install -Dm644 arrow.png radio.png -t %{buildroot}%{_datadir}/%{name}/
for _variant in black blue brown deepPurple indigo orange pink red sakuraPink teal; do
    _variant_name=Material-Color-${_variant^}
    install -dm755 %{buildroot}%{_datadir}/fcitx5/themes/$_variant_name/
    ln -s ../../../%{name}/arrow.png %{buildroot}%{_datadir}/fcitx5/themes/$_variant_name/
    ln -s ../../../%{name}/radio.png %{buildroot}%{_datadir}/fcitx5/themes/$_variant_name/
    install -Dm644 theme-$_variant.conf %{buildroot}%{_datadir}/fcitx5/themes/$_variant_name/theme.conf
    sed -i "s/^Name=.*/Name=$_variant_name/" %{buildroot}%{_datadir}/fcitx5/themes/$_variant_name/theme.conf
done


%files
%license LICENSE
%{_datadir}/fcitx5/themes/*/
%{_datadir}/%{name}/

%changelog
* Fri Apr 08 2022 zhullyb <zhullyb@outlook.com> - 0.2.1-1
- First build.
