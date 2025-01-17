%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: Qt integration framework with Plasma
Name: plasma-integration
Version: 5.27.12
Release: 1
Source0: http://download.kde.org//%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Patch0: plasma-integration-5.17.5-allow-configuring-button-order.patch
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Breeze)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5Wayland)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: %mklibname -d -s qt5themesupport
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: noto-sans-fonts
Requires: noto-sans-fonts
Requires: (breeze or plasma6-breeze)
Suggests: (plasma6-integration or %{name}-i18n)

%description
Framework Integration is a set of plugins responsible
for better integration of Qt applications when running
on a KDE Plasma workspace.

%package devel
Summary: Development files for plasma-integration
Group: Development/C++ and C
Requires: %{name} = %{EVRD}

%description devel
Development files for plasma-key-data.

%package i18n
Summary: Translations for plasma-integration
Group: Internationalization

%description i18n
Translations for plasma-integration (that conflict with
Plasma 6 integration)

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang plasmaintegration5 || touch plasmaintegration5.lang

%files
%doc README.md
%{_libdir}/qt5/plugins/platformthemes/KDEPlasmaPlatformTheme.so
%{_datadir}/kconf_update/*.upd
%{_datadir}/kconf_update/*.pl
%{_libdir}/qt5/plugins/platforminputcontexts/plasmaimplatforminputcontextplugin.so

%files i18n -f plasmaintegration5.lang

%files devel
%{_includedir}/PlasmaKeyData
%{_libdir}/pkgconfig/plasma-key-data.pc
