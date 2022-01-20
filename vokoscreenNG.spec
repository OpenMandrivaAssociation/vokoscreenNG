%define _empty_manifest_terminate_build 0

Name:           vokoscreenNG
Version:        3.1.0
Release:        1
Summary:        Powerful screencast creator
Group:          Video/Editors
License:        GPLv2
URL:            https://github.com/vkohaupt/vokoscreenNG
Source0:        https://github.com/vkohaupt/vokoscreenNG/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  intltool
BuildRequires:  qmake5
BuildRequires:  qt5-qtbase-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)

%description
vokoscreenNG is a powerful screencast creator in 39 languages to record the screen, an area or a window (Linux only). 
Recording of audio from multiple sources is supported. With the built-in camera support, you can make your video more personal. 
Other tools such as magnifying glass, countdown, timer and systray support will help you do a good job.

%prep
%autosetup -p1

%build
cd src/
%qmake_qt5 PREFIX=/usr
cd ..
%make_build -C src/
cd ..
%install
cd src/
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}/usr/bin/
cp src/%{name} %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/applications/
cp src/applications/%{name}.desktop %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/usr/share/pixmaps/
cp src/applications/%{name}.png %{buildroot}/usr/share/pixmaps/

%files
%doc COPYING
%doc README.md ToDo.txt INSTALL
#{_bindir}/%{name}
#{_datadir}/applications/*.desktop
#{_datadir}/pixmaps/*.png
