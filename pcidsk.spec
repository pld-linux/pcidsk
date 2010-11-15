Summary:	PCIDSK SDK - read/write library for the PCI PCIDSK (.pix) file format
Summary(pl.UTF-8):	PCIDSK SDK - biblioteka odczytu i zapisu plików w formacie PCI PCIDSK (.pix)
Name:		pcidsk
Version:	0.3
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://home.gdal.org/projects/pcidsk/download/%{name}-%{version}.tar.gz
# Source0-md5:	5d8eb542eed79b85d3a49cdd87a1d963
Patch0:		%{name}-c++.patch
URL:		http://home.gdal.org/projects/pcidsk/
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PCIDSK SDK is a C++ Library for reading and writing the PCIDSK
(.pix) geospatial file format used as the primary format of the
Geomatica and related software from PCI Geomatics.

%description -l pl.UTF-8
PCIDSK SDK to biblioteka C++ do odczytu i zapisu plików danych
geoprzestrzennych w formacie PCIDSK (.pix), używanych jako główny
format przez oprogramowanie Geomatica i podobne firmy PCI Geomatics.

%package devel
Summary:	Header files for pcidsk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki pcidsk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for pcidsk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki pcidsk.

%package static
Summary:	Static pcidsk library
Summary(pl.UTF-8):	Statyczna biblioteka pcidsk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pcidsk library.

%description static -l pl.UTF-8
Statyczna biblioteka pcidsk.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C src \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -Wall -fPIC -I. -DHAVE_LIBJPEG" \
	CPPFLAGS="%{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/pcidsk}

install src/libpcidsk.so $RPM_BUILD_ROOT%{_libdir}
install src/pcidsk.a $RPM_BUILD_ROOT%{_libdir}/libpcidsk.a
cp -p src/pcidsk*.h $RPM_BUILD_ROOT%{_includedir}/pcidsk

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcidsk.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/pcidsk

%files static
%defattr(644,root,root,755)
%{_libdir}/libpcidsk.a
