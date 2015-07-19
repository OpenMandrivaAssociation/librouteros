%define major	0
%define libname %mklibname routeros %{major}
%define devname %mklibname routeros -d

Summary:	Library for accessing MikroTik's RouterOS via its API
Name:		librouteros
Version:	1.1.2
Release:	10
License:	GPLv2+
Group:		System/Libraries
Url:		http://verplant.org/librouteros
Source0:	http://verplant.org/librouteros/files/%{name}-%{version}.tar.bz2
Patch0:		disable_werror.patch
BuildRequires:	pkgconfig(libgcrypt)

%description
librouteros (or libRouterOS) is a C library to communicate 
with network devices by MikroTik running their Linux-based 
operating system RouterOS.

%package -n %{libname}
Summary:	Files for developing applications that use librouteros
Group:		System/Libraries

%description -n %{libname}
librouteros (or libRouterOS) is a C library to communicate 
with network devices by MikroTik running their Linux-based
operating system RouterOS.

%package -n %{devname}
Summary:	Files for developing applications that use librouteros
Group:		Development/C
Provides:	routeros-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
The header files and libtool library for
developing applications that use librouteros.

%prep
%setup -q
%patch0 -p0
autoreconf -fi

%build
%configure2_5x --disable-static

%make

%install
%makeinstall_std

%files
%{_bindir}/ros
%{_mandir}/man1/ros.1.*

%files -n %{libname}
%{_libdir}/librouteros.so.%{major}*

%files -n %{devname}
%doc README ChangeLog NEWS
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/librouteros.3.*

