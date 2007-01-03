Summary:	Internet television application
Name:		democracy
Version:	0.9.2.2
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	ftp://ftp.osuosl.org/pub/pculture.org/democracy/src/Democracy-%{version}.tar.gz
# Source0-md5:	0b92aa3efb2a93e7c066152137fcf9fa
URL:		http://www.getdemocracy.com/
BuildRequires:	boost-python-devel
BuildRequires:	libfame
BuildRequires:	mozilla-firefox-devel
BuildRequires:	python-Pyrex
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygtk-devel
BuildRequires:	xine-lib-devel
Requires:	python-dbus
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Democracy Player (also known as Democracy and DTV) is an Internet
television application developed by the Participatory Culture
Foundation (PCF). It can automatically download videos from RSS-based
"channels", as well as managing and playing the videos collected from
these channels.

Democracy Player integrates an RSS aggregator, a BitTorrent client,
and VLC media player (or Xine Media Player under GNU/Linux).

%prep
%setup -q -n Democracy-%{version}

mv platform/gtk-x11/README README.gtk-x11

%build
cd platform/gtk-x11

CFLAGS="%{rpmcflags}" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

cd platform/gtk-x11
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
cd ../..

%py_postclean $RPM_BUILD_ROOT%{py_sitedir}/democracy

%find_lang democracyplayer

%clean
rm -rf $RPM_BUILD_ROOT

%files -f democracyplayer.lang
%defattr(644,root,root,755)
%doc CREDITS README README.gtk-x11
%attr(755,root,root) %{_bindir}/democracyplayer

%dir %{py_sitedir}/democracy
%{py_sitedir}/democracy/*.py[co]
%dir %{py_sitedir}/democracy/BitTorrent
%{py_sitedir}/democracy/BitTorrent/*.py[co]
%dir %{py_sitedir}/democracy/compiled_templates
%{py_sitedir}/democracy/compiled_templates/*.py[co]
%dir %{py_sitedir}/democracy/compiled_templates/unittest
%{py_sitedir}/democracy/compiled_templates/unittest/*.py[co]
%dir %{py_sitedir}/democracy/dl_daemon
%{py_sitedir}/democracy/dl_daemon/*.py[co]
%dir %{py_sitedir}/democracy/dl_daemon/private
%{py_sitedir}/democracy/dl_daemon/private/*.py[co]
%dir %{py_sitedir}/democracy/frontend_implementation
%{py_sitedir}/democracy/frontend_implementation/*.py[co]
%dir %{py_sitedir}/democracy/test
%{py_sitedir}/democracy/test/*.py[co]
%attr(755,root,root) %{py_sitedir}/democracy/MozillaBrowser.so
%attr(755,root,root) %{py_sitedir}/democracy/database.so
%attr(755,root,root) %{py_sitedir}/democracy/fasttypes.so
%attr(755,root,root) %{py_sitedir}/democracy/sorts.so
%attr(755,root,root) %{py_sitedir}/democracy/xine.so
%attr(755,root,root) %{py_sitedir}/democracy/xlibhelper.so

%{_desktopdir}/democracyplayer.desktop
%{_datadir}/democracy
%{_mandir}/man1/democracyplayer.1*
%{_datadir}/mime/packages/democracy.xml
%{_pixmapsdir}/democracyplayer-*.png
