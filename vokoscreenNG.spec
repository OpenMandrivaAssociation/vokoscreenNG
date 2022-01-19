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
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5X11Extras)
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

%install
%make_install -C

%files
%doc COPYING
%doc README.md ToDo.txt INSTALL
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
