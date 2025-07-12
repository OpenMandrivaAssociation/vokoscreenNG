%undefine _debugsource_packages

Name:           vokoscreenNG
Version:        4.6.0
Release:        1
Summary:        Powerful screencast creator
Group:          Video/Editors
License:        GPLv2
URL:            https://github.com/vkohaupt/vokoscreenNG
Source0:        https://github.com/vkohaupt/vokoscreenNG/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  intltool
BuildRequires:  qmake-qt6
BuildRequires:  qt6-qtbase-tools
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
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
# Requires for Player x264
Requires:       gstreamer1.0-libav
# To run vokoscreenNG on Wayland session pipewire gstreamer is required.
Requires:      gstreamer1.0-pipewire
# Requires for more formats
Requires:      gstreamer-plugins-rs

Provides:       vokoscreenng = %{version}

%description
vokoscreenNG is a powerful screencast creator in 39 languages to record the screen, an area or a window (Linux only). 
Recording of audio from multiple sources is supported. With the built-in camera support, you can make your video more personal. 
Other tools such as magnifying glass, countdown, timer and systray support will help you do a good job.

%prep
%autosetup -p1

%build
cd src/
qmake-qt6 PREFIX=/usr
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
#doc README.md ToDo.txt INSTALL
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
