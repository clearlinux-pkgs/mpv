#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mpv
Version  : 0.33.0
Release  : 21
URL      : https://github.com/mpv-player/mpv/archive/v0.33.0/mpv-0.33.0.tar.gz
Source0  : https://github.com/mpv-player/mpv/archive/v0.33.0/mpv-0.33.0.tar.gz
Summary  : mpv media player client library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: mpv-bin = %{version}-%{release}
Requires: mpv-data = %{version}-%{release}
Requires: mpv-lib = %{version}-%{release}
Requires: mpv-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : libX11-dev
BuildRequires : libva-dev
BuildRequires : mesa-dev
BuildRequires : not-ffmpeg-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(libass)
BuildRequires : pkgconfig(libplacebo)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libva-x11)
BuildRequires : pkgconfig(luajit)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xscrnsaver)
BuildRequires : zlib-dev
Patch1: 0001-waf-add-waf-as-a-patch-for-ClearLinux.patch
Patch2: 0002-Makefile-quick-wrapper-for-waf.patch
Patch3: 0003-vo_gpu-placebo-update-for-upstream-API-changes.patch
Patch4: 0004-vo_gpu-libplacebo-require-v2.72.0.patch
Patch5: 0005-vo_gpu-placebo-keep-track-of-texture-sample-mode.patch

%description
TA ("Tree Allocator") is a wrapper around malloc() and related functions,
adding features like automatically freeing sub-trees of memory allocations if
a parent allocation is freed.

%package bin
Summary: bin components for the mpv package.
Group: Binaries
Requires: mpv-data = %{version}-%{release}
Requires: mpv-license = %{version}-%{release}

%description bin
bin components for the mpv package.


%package data
Summary: data components for the mpv package.
Group: Data

%description data
data components for the mpv package.


%package dev
Summary: dev components for the mpv package.
Group: Development
Requires: mpv-lib = %{version}-%{release}
Requires: mpv-bin = %{version}-%{release}
Requires: mpv-data = %{version}-%{release}
Provides: mpv-devel = %{version}-%{release}
Requires: mpv = %{version}-%{release}

%description dev
dev components for the mpv package.


%package doc
Summary: doc components for the mpv package.
Group: Documentation

%description doc
doc components for the mpv package.


%package lib
Summary: lib components for the mpv package.
Group: Libraries
Requires: mpv-data = %{version}-%{release}
Requires: mpv-license = %{version}-%{release}

%description lib
lib components for the mpv package.


%package license
Summary: license components for the mpv package.
Group: Default

%description license
license components for the mpv package.


%prep
%setup -q -n mpv-0.33.0
cd %{_builddir}/mpv-0.33.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617570475
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1617570475
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mpv
cp %{_builddir}/mpv-0.33.0/LICENSE.GPL %{buildroot}/usr/share/package-licenses/mpv/c76a43b337cf9290dfcc982c1e51d6561900793a
cp %{_builddir}/mpv-0.33.0/LICENSE.LGPL %{buildroot}/usr/share/package-licenses/mpv/3704f4680301a60004b20f94e0b5b8c7ff1484a9
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/etc/mpv/encoding-profiles.conf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mpv

%files data
%defattr(-,root,root,-)
/usr/share/applications/mpv.desktop
/usr/share/bash-completion/completions/mpv
/usr/share/icons/hicolor/128x128/apps/mpv.png
/usr/share/icons/hicolor/16x16/apps/mpv.png
/usr/share/icons/hicolor/32x32/apps/mpv.png
/usr/share/icons/hicolor/64x64/apps/mpv.png
/usr/share/icons/hicolor/scalable/apps/mpv.svg
/usr/share/icons/hicolor/symbolic/apps/mpv-symbolic.svg
/usr/share/zsh/site-functions/_mpv

%files dev
%defattr(-,root,root,-)
/usr/include/mpv/client.h
/usr/include/mpv/opengl_cb.h
/usr/include/mpv/render.h
/usr/include/mpv/render_gl.h
/usr/include/mpv/stream_cb.h
/usr/lib64/libmpv.so
/usr/lib64/pkgconfig/mpv.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/mpv/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmpv.so.1
/usr/lib64/libmpv.so.1.109.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mpv/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/mpv/c76a43b337cf9290dfcc982c1e51d6561900793a
