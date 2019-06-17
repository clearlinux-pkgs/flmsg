#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flmsg
Version  : 4.0.9
Release  : 11
URL      : https://sourceforge.net/projects/fldigi/files/flmsg/flmsg-4.0.9.tar.gz
Source0  : https://sourceforge.net/projects/fldigi/files/flmsg/flmsg-4.0.9.tar.gz
Summary  : Forms management editor for Amateur Radio standard message formats
Group    : Development/Tools
License  : GPL-3.0
Requires: flmsg-bin = %{version}-%{release}
Requires: flmsg-data = %{version}-%{release}
Requires: flmsg-license = %{version}-%{release}
BuildRequires : fltk-dev
BuildRequires : fontconfig-dev
BuildRequires : libXcursor-dev
BuildRequires : libXft-dev
BuildRequires : libXrender-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev

%description
flmsg is a editor / file management tool for ics213 forms which form the
basis for emergency communications data transfers.

%package bin
Summary: bin components for the flmsg package.
Group: Binaries
Requires: flmsg-data = %{version}-%{release}
Requires: flmsg-license = %{version}-%{release}

%description bin
bin components for the flmsg package.


%package data
Summary: data components for the flmsg package.
Group: Data

%description data
data components for the flmsg package.


%package license
Summary: license components for the flmsg package.
Group: Default

%description license
license components for the flmsg package.


%prep
%setup -q -n flmsg-4.0.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560779069
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1560779069
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flmsg
cp COPYING %{buildroot}/usr/share/package-licenses/flmsg/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flmsg

%files data
%defattr(-,root,root,-)
/usr/share/applications/flmsg.desktop
/usr/share/pixmaps/flmsg.xpm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flmsg/COPYING
