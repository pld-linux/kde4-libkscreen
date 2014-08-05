%define         _state          stable
%define		orgname		libkscreen
%define         qtver           4.8.3

Summary:	Kscreen library
Name:		kde4-libkscreen
Version:	1.0.5
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{orgname}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	b1cc2805cd5ff468d534d75cbab69426
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libxcb-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-renderutil-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE's screen management software.

%package devel
Summary:	Header files for libkscreen development
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libkscreen development.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DQT_QMAKE_EXECUTABLE="qmake-qt4" \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkscreen.so.?
%attr(755,root,root) %{_libdir}/libkscreen.so.*.*.*
%dir %{_libdir}/kde4/plugins/kscreen
%attr(755,root,root) %{_libdir}/kde4/plugins/kscreen/KSC_Fake.so
%attr(755,root,root) %{_libdir}/kde4/plugins/kscreen/KSC_XRandR.so
%attr(755,root,root) %{_libdir}/kde4/plugins/kscreen/KSC_XRandR11.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkscreen.so
%{_includedir}/kscreen
%{_libdir}/cmake/LibKScreen
%{_pkgconfigdir}/kscreen.pc
