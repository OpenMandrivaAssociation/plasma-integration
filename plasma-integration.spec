%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary: Qt integration framework with Plasma
Name: plasma-integration
Version: 6.4.4
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-integration/-/archive/%{gitbranch}/plasma-integration-%{gitbranchd}.tar.bz2#/plasma-integration-%{git}.tar.bz2
%else
Source0: http://download.kde.org//%{stable}/plasma/%{plasmaver}/plasma-integration-%{version}.tar.xz
%endif
Patch0: plasma-integration-5.17.5-allow-configuring-button-order.patch
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Breeze)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(Wayland) >= 5.90.0
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: %mklibname -d -s qt5themesupport
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5Wayland)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: noto-sans-fonts
Requires: noto-sans-fonts
Requires: breeze
# Renamed after 6.0 2025-05-03
%rename plasma6-integration
# This package was empty even before
Obsoletes: plasma6-integration-devel < %{EVRD}
Obsoletes: plasma-integration-devel < %{EVRD}
Recommends: (%{name}-qt5 if %mklibname qt5gui5)

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DBUILD_QT5:BOOL=ON
BuildOption:	-DBUILD_QT6:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Framework Integration is a set of plugins responsible
for better integration of Qt applications when running
on a KDE Plasma workspace.

%package qt5
Summary:	Plasma integration for Qt 5.x applications
Group: 		System/Libraries

%description qt5
Plasma integration for Qt 5.x applications

%files -f %{name}.lang
%{_qtdir}/plugins/platformthemes/KDEPlasmaPlatformTheme6.so

%files qt5
%{_libdir}/qt5/plugins/platformthemes/KDEPlasmaPlatformTheme5.so
