%{?!python3_pkgversion:%global python3_pkgversion 3}

%global debug_package %{nil}

Name:           nvchecker
Version:        2.9
Release:        1%{?dist}
Summary:        New version checker for software releases
License:        MIT
URL:            https://github.com/lilydjwg/nvchecker
Source0:        https://github.com/lilydjwg/nvchecker/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	make
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python3-docutils

%{?python_enable_dependency_generator}

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%py3_build
make -C docs man

%install
%py3_install
%{__install} -Dm644 docs/_build/man/nvchecker.1 -t %{buildroot}%{_datadir}/man/man1/
%{__install} -Dm644 scripts/nvtake.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/nvtake


%files
%license LICENSE
%doc docs/usage.rst
%doc sample_config.toml
%{_bindir}/{nvchecker,nvchecker-ini2toml,nvchecker-notify,nvcmp,nvtake}
%{python3_sitelib}/*
%{_datadir}/man/man1/nvchecker.1.gz
%{_datadir}/bash-completion/completions/nvtake


%changelog
* Thu Jul 14 2022 zhullyb <zhullyb@outlook.com>
- new version.
- remove python3-pygments from buildrequires.

* Sun Feb 27 2022 zhullyb <zhullyb@outlook.com> - 2.7-2
- Add make into buildrequires

* Sat Feb 26 2022 zhullyb <zhullyb@outlook.com> - 2.7-1
- new version
