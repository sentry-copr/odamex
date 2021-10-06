
# stable release does not compile on Fedora
%global     commit 22ebdc2b52e0c8cd4c4445eb38cb2a0f24584aa1

Name:       odamex
Version:    0.8.5
Release:    1%{?dist}

Summary:    Online Multiplayer Doom port with a strong focus on the original gameplay while providing a breadth of enhancements. 
License:    GPLv2+
URL:        https://odamex.net/
Source0:    https://github.com/odamex/odamex/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit}.tar.gz

BuildRequires: gcc-c++ cmake make bzip2-devel
BuildRequires: alsa-lib-devel
BuildRequires: wxGTK3-devel
BuildRequires: SDL2-devel SDL2_mixer-devel
BuildRequires: deutex

%description
Odamex is a modification of DOOM to allow players to compete with each other over the
Internet using the client/server architecture. Thanks to the source code release of DOOM by
id Software in December 1997, there have been many modifications that enhanced DOOM
in various ways. These modifications are known as "source ports", as early modifications
mainly ported DOOM to other platforms and operating systems such as Windows and 
Macintosh.

Odamex is based on the CSDoom 0.62 source code originally created by Sergey Makovkin, 
which is based on the ZDoom 1.22 source code created by Randy Heit.

%prep
%autosetup -n %{name}-%{commit}

%build
OPT_FLAGS=`echo %{optflags}|sed -e 's/-Werror=format-security/-Wformat-security/g'`

CFLAGS=$OPT_FLAGS \
CXXFLAGS=$OPT_FLAGS \
FFLAGS=$OPT_FLAGS \
FCFLAGS=$OPT_FLAGS \
%cmake . \
       -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo\
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
* Wed Oct 06 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Fri Jan 15 18:14:12 CET 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.3-1
- Initial spec


