# $Id$
# Authority: dag
# Upstream: Carson Harding <carson,harding$shaw,ca>

%define real_version 1.2g

Summary: Automatically restart SSH sessions and tunnels
Name: autossh
Version: 1.2
Release: 2.g
License: GPL
Group: Applications/Internet
URL: http://www.harding.motd.ca/autossh/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.harding.motd.ca/autossh/autossh-%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Autossh is a program to start a copy of ssh and monitor it, restarting
it as necessary should it die or stop passing traffic. The idea and
the mechanism are from rstunnel (Reliable SSH Tunnel), but implemented
in C. The author's view is that it is not as fiddly as rstunnel to get
to work. Connection monitoring using a loop of port forwardings. Backs
off on rate of connection attempts when experiencing rapid failures
such as connection refused.

%prep
%setup -n %{name}-%{real_version}

%build
%{__make} %{?_smp_mflags} -f Makefile.linux

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 autossh %{buildroot}%{_bindir}/autossh
%{__install} -D -m0644 autossh.1 %{buildroot}%{_mandir}/man1/autossh.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc autossh.host CHANGES README rscreen
%doc %{_mandir}/man1/autossh.1*
%{_bindir}/autossh

%changelog
* Fri Dec 10 2004 Dag Wieers <dag@wieers.com> - 1.2-2.g
- Fixed Group tag.

* Thu Dec 09 2004 Dag Wieers <dag@wieers.com> - 1.2-1.g
- Updated to release 1.2g.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 1.2-1.f
- Initial package. (using DAR)
