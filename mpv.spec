#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v20
# autospec commit: 4d029647d79e
#
Name     : mpv
Version  : 0.38.0
Release  : 118
URL      : https://github.com/mpv-player/mpv/archive/v0.38.0/mpv-0.38.0.tar.gz
Source0  : https://github.com/mpv-player/mpv/archive/v0.38.0/mpv-0.38.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: mpv-bin = %{version}-%{release}
Requires: mpv-data = %{version}-%{release}
Requires: mpv-lib = %{version}-%{release}
Requires: mpv-license = %{version}-%{release}
Requires: mpv-man = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : libX11-dev
BuildRequires : libarchive-dev
BuildRequires : libva-dev
BuildRequires : libvdpau-dev
BuildRequires : lua-dev
BuildRequires : mesa-dev
BuildRequires : not-ffmpeg-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(ffnvcodec)
BuildRequires : pkgconfig(jack)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libass)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libplacebo)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libva-x11)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(luajit)
BuildRequires : pkgconfig(sndio)
BuildRequires : pkgconfig(uchardet)
BuildRequires : pkgconfig(vapoursynth)
BuildRequires : pkgconfig(vapoursynth-script)
BuildRequires : pkgconfig(vdpau)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xpresent)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xscrnsaver)
BuildRequires : pkgconfig(xv)
BuildRequires : pkgconfig(zimg)
BuildRequires : pypi-docutils
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-waf-add-waf-as-a-patch-for-ClearLinux.patch
Patch2: 0002-Makefile-quick-wrapper-for-waf.patch

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
Requires: mpv-man = %{version}-%{release}

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


%package man
Summary: man components for the mpv package.
Group: Default

%description man
man components for the mpv package.


%prep
%setup -q -n mpv-0.38.0
cd %{_builddir}/mpv-0.38.0
%patch -P 1 -p1
%patch -P 2 -p1
pushd ..
cp -a mpv-0.38.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728611717
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -D libmpv=true  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -D libmpv=true  builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/mpv
cp %{_builddir}/mpv-%{version}/LICENSE.GPL %{buildroot}/usr/share/package-licenses/mpv/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/mpv-%{version}/LICENSE.LGPL %{buildroot}/usr/share/package-licenses/mpv/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
## Remove excluded files
rm -f %{buildroot}*/usr/etc/mpv/encoding-profiles.conf
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/mpv
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
/usr/share/metainfo/mpv.metainfo.xml
/usr/share/zsh/site-functions/_mpv

%files dev
%defattr(-,root,root,-)
/usr/include/mpv/client.h
/usr/include/mpv/render.h
/usr/include/mpv/render_gl.h
/usr/include/mpv/stream_cb.h
/usr/lib64/libmpv.so
/usr/lib64/pkgconfig/mpv.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/mpv/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libmpv.so.2.3.0
/usr/lib64/libmpv.so.2
/usr/lib64/libmpv.so.2.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mpv/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/mpv/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mpv.1
