
Name:         odamex
Version:      10.0.0
Release:      1%{?dist}

Summary:      Online Multiplayer Doom port with a strong focus on the original gameplay while providing a breadth of enhancements.
License:      GPLv2 and MIT and LGPLv2+ with exceptions and zlib and BSD and GPLv2+
URL:          https://odamex.net/
Source0:      https://nav.dl.sourceforge.net/project/odamex/Odamex/%{version}/odamex-src-%{version}.tar.gz
Patch0:       0001-Merge-pull-request-626-from-chewi-master-std.patch

BuildRequires: gcc-c++ cmake
BuildRequires: alsa-lib-devel
BuildRequires: libcurl-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: wxGTK3-devel
BuildRequires: deutex
BuildRequires: SDL2-devel SDL2_mixer-devel
BuildRequires: deutex

# MIT
# not used but provided in the release tarball
Provides:     bundled(libcurl) = 7.71.1
# LGPLv2+ with exceptions
Provides:     bundled(fltk)
# MIT
Provides:     bundled(jsoncpp)
# MIT
Provides:     bundled(libminiupnpc) = 1.9.20140401
# zlib
# not used but provided in the release tarball
Provides:     bundled(libpng) = 1.6.37
# MIT
Provides:     bundled(portmidi)
# BSD
Provides:     bundled(protobuf)
# GPLv2+
Provides:     bundled(textscreen)
# zlib
# not used but provided in the release tarball
Provides:     bundled(zlib) = 1.2.11

%description
Odamex is a modification of DOOM to allow players to compete with each
other over theInternet using a client/server architecture.
Thanks to the source code release of DOOM by id Software in December 1997,
there have been many modifications that enhanced DOOM in various ways.
These modifications are known as "source ports", as early modifications
mainly ported DOOM to other platforms and operating systems such as
Windows and Macintosh.

Odamex is based on the CSDoom 0.62 source code originally created by
Sergey Makovkin, which is based on the ZDoom 1.22 source code created
by Marisa Heit.

%prep
%autosetup -n odamex-src-%{version} -p1

%build

%cmake -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo\
       -DBUILD_CLIENT=1 \
       -DBUILD_SERVER=1 \
       -DBUILD_MASTER=1 \
       -DBUILD_ODALAUNCH=1

%cmake_build

%install
%cmake_install

%files
%{_bindir}/odalaunch
%{_bindir}/odamast
%{_bindir}/odamex
%{_bindir}/odasrv
%{_datadir}/%{name}

%changelog
* Sat Mar 26 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 10.0.0-1
- Update to 10.0.0

* Wed Oct 06 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Fri Jan 15 18:14:12 CET 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.3-1
- Initial spec


