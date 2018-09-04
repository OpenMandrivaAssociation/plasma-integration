%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: Qt integration framework with Plasma
Name: plasma-integration
Version: 5.13.5
Release: 1
Source0: http://download.kde.org//%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
URL: http://kde.org/
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
BuildRequires: noto-sans-fonts
Requires: oxygen-fonts
Requires: noto-sans-fonts

%description
Framework Integration is a set of plugins responsible
for better integration of Qt applications when running
on a KDE Plasma workspace.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang plasmaintegration5 || touch plasmaintegration5.lang

%files -f plasmaintegration5.lang
%doc README.md
%{_libdir}/qt5/plugins/platformthemes/KDEPlasmaPlatformTheme.so
%{_datadir}/kconf_update/*.upd
%{_datadir}/kconf_update/*.pl
