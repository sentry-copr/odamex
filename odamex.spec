
Name:         odamex
Version:      11.1.1
Release:      1%{?dist}

Summary:      Online Multiplayer Doom port with a strong focus on the original gameplay while providing a breadth of enhancements.
License:      GPLv2 and MIT and LGPLv2+ with exceptions and zlib and BSD and GPLv2+
URL:          https://odamex.net/
Source0:      https://github.com/odamex/odamex/releases/download/%{version}/odamex-src-%{version}.tar.gz

BuildRequires: gcc-c++ cmake
BuildRequires: alsa-lib-devel
BuildRequires: libcurl-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: (wxGTK-devel or wxGTK3-devel)
BuildRequires: deutex
BuildRequires: pkgconfig(jsoncpp)
BuildRequires: SDL2-devel SDL2_mixer-devel
BuildRequires: portmidi-devel
BuildRequires: miniupnpc-devel

# The Launcher needs the client to function
Requires:      %{name}-client

# MIT
# not used but provided in the release tarball
Provides:     bundled(libcurl)
# LGPLv2+ with exceptions
Provides:     bundled(fltk)
# MIT
Provides:     bundled(jsoncpp)
# MIT
Provides:     bundled(libminiupnpc)
# zlib
# not used but provided in the release tarball
Provides:     bundled(libpng)
# MIT
# not used but provided in the release tarball
Provides:     bundled(portmidi)
# BSD
Provides:     bundled(protobuf)
# GPLv2+
Provides:     bundled(textscreen)
# zlib
# not used but provided in the release tarball
Provides:     bundled(zlib)

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

%package client
Summary:    Odamex Client
Requires:   %{name}-data

%description client
Odamex Client

%package server
Summary:    Odamex Server
Requires:   %{name}-data

%description server
Odamex Server

%package masterserver
Summary:    Odamex Master Server
Requires:   %{name}-data

%description masterserver
Odamex Master Server

%package data
Summary:    Odamex Data
BuildArch:  noarch

%description data
Odamex Data

%prep
%autosetup -n odamex-src-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
    -DUSE_INTERNAL_DEUTEX=0 \
    -DUSE_INTERNAL_ZLIB=0 \
    -DUSE_INTERNAL_PNG=0 \
    -DUSE_INTERNAL_CURL=0 \
    -DUSE_INTERNAL_JSONCPP=0 \
    -DUSE_INTERNAL_WXWIDGETS=0 \
    -DUSE_INTERNAL_MINIUPNP=0 \
    -DENABLE_PORTMIDI=1 \
    -DUSE_MINIUPNP=1 \
    -DBUILD_CLIENT=1 \
    -DBUILD_SERVER=1 \
    -DBUILD_MASTER=1 \
    -DBUILD_ODALAUNCH=1

%cmake_build

%install
%cmake_install

%files
%{_bindir}/odalaunch

%files client
%{_bindir}/odamex

%files server
%{_bindir}/odasrv

%files masterserver
%{_bindir}/odamast

%files data
%{_datadir}/%{name}

%changelog
* Wed Oct 29 2025 Jan200101 <sentrycraft123@gmail.com> - 11.1.1-1
- Update to 11.1.1

* Sun Jul 14 2024 Jan200101 <sentrycraft123@gmail.com> - 10.5.0-1
- Update to 10.5.0

* Sat Oct 28 2023 Jan Drögehoff <sentrycraft123@gmail.com> - 10.4.0-1
- Update to 10.4.0

* Wed Apr 19 2023 Jan Drögehoff <sentrycraft123@gmail.com> - 10.3.0-1
- Update to 10.3.0

* Sat Mar 26 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 10.0.0-1
- Update to 10.0.0

* Wed Oct 06 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Fri Jan 15 18:14:12 CET 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.3-1
- Initial spec


