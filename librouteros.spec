%define		Werror_cflags %nil

Name:		librouteros
Version:	1.1.2
Release:	1
Summary:	Library for accessing MikroTik's RouterOS via its API
License:	GPLv2+
Group:		System/Libraries
Url:		http://verplant.org/librouteros
Source0:	http://verplant.org/librouteros/files/librouteros-%{version}.tar.bz2
Patch0:		disable_werror.patch

%description
librouteros (or libRouterOS) is a C library to communicate 
with network devices by MikroTik running their Linux-based 
operating system RouterOS.

#------------------------------------------------------

%define major 0
%define libname %mklibname routeros %{major}

%package -n %{libname}
Summary: Files for developing applications that use librouteros
Group: System/Libraries

%description -n %{libname}
librouteros (or libRouterOS) is a C library to communicate 
with network devices by MikroTik running their Linux-based operating system RouterOS.

%files -n %{libname}
%{_libdir}/*.so.%{major}*


%define develname %mklibname routeros -d

%package -n %{develname}
Summary:	Files for developing applications that use librouteros
Group:		Development/C
Provides:	routeros-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	routeros-devel < %{version}


%description -n %{develname}
The header files and libtool library for
developing applications that use librouteros.

#------------------------------------------------------

%prep
%setup -q
%patch0 -p0
autoreconf -fi

%build
%configure2_5x

%make

%install
%makeinstall_std
find %{buildroot} -type f -name '*.la' -exec rm -f {} \;


%files -n %{develname}
%doc README ChangeLog NEWS
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so


%files
%{_bindir}/ros
%{_mandir}/man1/ros.1.*
%{_mandir}/man3/librouteros.3.*
