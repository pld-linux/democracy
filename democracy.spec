# TODO
# - make /usr/lib64/python2.4/site-packages/democracy/MozillaBrowser.so
#   to be linked with RPATH /usr/lib64/xulrunner. actually to fix as setuputils
#   passes -R which is not accepted by compiler (should be -Wl,-rpath,/usr/lib64/xulrunner).
#   until then start program with 'LD_LIBRARY_PATH=/usr/lib64/xulrunner democracy'
Summary:	Internet television application
Summary(pl.UTF-8):	Aplikacja do telewizji internetowej
Name:		democracy
Version:	0.9.2.2
Release:	0.2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.osuosl.org/pub/pculture.org/democracy/src/Democracy-%{version}.tar.gz
# Source0-md5:	0b92aa3efb2a93e7c066152137fcf9fa
Patch0:		%{name}-lib64.patch
URL:		http://www.getdemocracy.com/
BuildRequires:	boost-python-devel
BuildRequires:	libfame
BuildRequires:	python-Pyrex
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygtk-devel
BuildRequires:	xine-lib-devel
BuildRequires:	xulrunner-devel
Requires:	gstreamer-imagesink-x
Requires:	python-dbus
Requires:	python-gnome-extras-mozilla
Requires:	python-gnome-vfs
Requires:	python-gstreamer
Requires:	python-pygtk-glade
Requires:	shared-mime-info
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Democracy Player (also known as Democracy and DTV) is an Internet
television application developed by the Participatory Culture
Foundation (PCF). It can automatically download videos from RSS-based
"channels", as well as managing and playing the videos collected from
these channels.

Democracy Player integrates an RSS aggregator, a BitTorrent client,
and VLC media player (or Xine Media Player under GNU/Linux).

%description -l pl.UTF-8
Democracy Player (znany także jako Democracy albo DTV) to aplikacja do
telewizji internetowej stworzona przez fundację Participatory Culture
Foundation (PCF). Potrafi automatycznie ściągać filmy z "kanałów"
opartych o RSS, a także zarządzać i odtwarzać filmy uzyskane z tych
kanałów.

Democracy Player integruje się z agregatorem RSS, klientem BitTorrenta
oraz odtwarzaczem multimedialnym VLC (lub Xine Media Playerem pod
Linuksem).

%prep
%setup -q -n Democracy-%{version}
%if "%{_lib}" != "lib"
%patch0 -p1
%endif

mv platform/gtk-x11/README README.gtk-x11

%build
cd platform/gtk-x11

CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

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
