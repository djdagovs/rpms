# $Id$
# Authority: shuff
# Upstream: Portland (http://portland.freedesktop.org/)

### EL6 ships with xdg-utils-1.0.2-15.20091016cvs.el6
# ExclusiveDist: el3 el4 el5

Summary: Freedesktop.org desktop integration tools
Name: xdg-utils
Version: 1.0.2
Release: 2%{?dist}
License: MIT
Group: System Environment/Base
URL: http://portland.freedesktop.org/wiki/XdgUtils

Source: http://portland.freedesktop.org/download/xdg-utils-%{version}.tgz
Patch1: xdg-utils-1.0-mimeopen.patch
Patch2: xdg-utils-1.0.1-typo.patch
Patch3: xdg-utils-1.0.1-htmlview.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: coreutils
BuildRequires: gawk
Requires: coreutils
Requires: desktop-file-utils
Requires: which

%description
Xdg-utils is a set of command line tools that assist applications with a
variety of desktop integration tasks. About half of the tools focus on tasks
commonly required during the installation of a desktop application and the
other half focuses on integration with the desktop environment while the
application is running. Even if the desktop components of your application are
limited to an installer, configuration or management tool, Xdg-utils provides
you with an easy way to enhance the usage experience of your customers by
improving the integration of these components in the user's environment. Best
of all, Xdg-utils is provided as open source and free of charge. 

%prep
%setup -n %{name}-%{version}%{?beta}
%patch1 -p1 -b .mimeopen
%patch2 -p1 -b .typo
%patch3 -p1 -b .htmlview

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE README RELEASE_NOTES TODO
%doc %{_mandir}/man1/xdg-desktop-icon.1*
%doc %{_mandir}/man1/xdg-desktop-menu.1*
%doc %{_mandir}/man1/xdg-email.1*
%doc %{_mandir}/man1/xdg-icon-resource.1*
%doc %{_mandir}/man1/xdg-mime.1*
%doc %{_mandir}/man1/xdg-open.1*
%doc %{_mandir}/man1/xdg-screensaver.1*
%{_bindir}/xdg-desktop-icon
%{_bindir}/xdg-desktop-menu
%{_bindir}/xdg-email
%{_bindir}/xdg-icon-resource
%{_bindir}/xdg-mime
%{_bindir}/xdg-open
%{_bindir}/xdg-screensaver

%changelog
* Sun Jan 10 2010 Steve Huff <shuff@vecna.org>
- man pages should be %doc
- why mess with globs that work?

* Sun Jan 10 2010 Yury V. Zaytsev <yury@shurup.com> - 1.0.2-2
- Synced the SPEC with CentOS Extras.

* Tue Jan 05 2010 Steve Huff <shuff@vecna.org> - 1.0.2-1
- Initial package.
