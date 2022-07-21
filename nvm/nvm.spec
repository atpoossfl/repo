Name:           nvm
Version:        0.39.1
Release:        1%{?dist}
Summary:        Node Version Manager

License:        MIT
URL:            https://github.com/nvm-sh/nvm
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        init-nvm.sh
Source2:        install-nvm-exec

%description
Simple bash script to manage multiple active node.js versions

%prep
%autosetup

%install
# convenience script
install -Dm644 %{S:1} -t %{buildroot}%{_datadir}/%{name}

# companion script which installs symlinks in NVM_DIR (see comment in script)
install -Dm644 %{S:2} -t %{buildroot}%{_datadir}/%{name}

# nvm itself
install -Dm644 nvm.sh -t %{buildroot}%{_datadir}/%{name}

# nvm-exec script for 'nvm exec' command
install -Dm755 nvm-exec -t %{buildroot}%{_datadir}/%{name}

# bash completion
install -Dm644 bash_completion %{buildroot}%{_datadir}/%{name}/bash_completion

%files
%license LICENSE.md
%{_datadir}/%{name}

%post
echo -e "\033[41;37m
You need to source nvm before you can use it. Do one of the following
or similar depending on your shell (and then restart your shell):

  echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.bashrc
  echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.zshrc

You can now install node.js versions (e.g. nvm install 10) and
activate them (e.g. nvm use 10).

init-nvm.sh is a convenience script which does the following:
\033[0m"
cat usr/share/nvm/init-nvm.sh
echo -e "\033[41;37m
You may wish to customize and put these lines directly in your
.bashrc (or similar) if, for example, you would like an NVM_DIR
other than ~/.nvm or you don't want bash completion.

See the nvm readme for more information: https://github.com/creationix/nvm
\033[0m"

%postun
if [ $1 = 0 ] ; then

echo -e "\033[41;37m
Don't forget to clean up any lines added to your shell's startup script!

For example, from your .bashrc (or .zshrc etc.), delete the line:

source /usr/share/nvm/init-nvm.sh
\033[0m"

fi

%changelog
* Thu Jul 21 2022 zhullyb <zhullyb@outlook.com> - 0.39.1-1
- First build.
