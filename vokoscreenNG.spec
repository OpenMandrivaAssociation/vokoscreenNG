%define _empty_manifest_terminate_build 0

Name:           vokoscreenNG
Version:        3.2.0
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
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)

# Required for vorbis and opus audio
Requires:       gstreamer1.0-plugins-base
# Required for mkv, avi, webm, mp4, vp8 video and flac audio
Requires:       gstreamer1.0-plugins-good
# Required for x265, av1, camera
Requires:       gstreamer1.0-plugins-bad
# Required for x264 and mp3lame
Requires:       gstreamer1.0-plugins-ugly

Provides:       vokoscreenng = %{version}

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
# Make install is broken here. Need install files manually.
#cd src/
##%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}/usr/bin/
cp src/%{name} %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/applications/
cp src/applications/%{name}.desktop %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/usr/share/pixmaps/
cp src/applications/%{name}.png %{buildroot}/usr/share/pixmaps/

%files
%doc COPYING
%doc README.md ToDo.txt INSTALL
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
