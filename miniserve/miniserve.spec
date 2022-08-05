%global debug_package %{nil}

%global forgeurl https://github.com/svenstaro/miniserve
Version:        0.20.0
%forgemeta

Name:           miniserve
Release:        1%{?dist}
Summary:        Tool to serve files via HTTP

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  rust
BuildRequires:  cargo

%description
%{summary}.

%prep
%forgeautosetup


%build
cargo build --release --locked


%install
install -Dm755 target/release/miniserve %{buildroot}%{_bindir}/miniserve

mkdir -p %{buildroot}%{_datadir}/{bash-completion/completions,zsh/site-functions,fish/vendor_completions.d}
target/release/miniserve --print-completions bash > %{buildroot}%{_datadir}/bash-completion/completions/miniserve
target/release/miniserve --print-completions zsh > %{buildroot}%{_datadir}/zsh/site-functions/_miniserve
target/release/miniserve --print-completions fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/miniserve.fish

mkdir -p %{buildroot}%{_mandir}/man1
target/release/miniserve --print-manpage | gzip > %{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/*/*/*

%changelog
* Fri Aug 05 2022 zhullyb <zhullyb@outlook.com>
- First version.
