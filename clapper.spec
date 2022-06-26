
%define libname %mklibname clapper
%define girname %mklibname clapper-gir
%define devname %mklibname clapper -d

Name:           clapper
Version:        0.5.2
Release:        1
Summary:        A GNOME media player built using GJS with GTK4
License:        GPL-3.0
URL:            https://github.com/Rafostar/clapper
Source:         https://github.com/Rafostar/clapper/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:	gjs
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.18.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

Requires:	%{girname} = %{version}-%{release}
Requires:       %{libname} = %{version}

Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-ugly
# For new va hardware decoding
Requires:	gstreamer1.0-plugins-bad
# For old vaapi hardware decoding
Requires:	gstreamer1.0-vaapi

%description
A GNOME media player built using GJS with GTK4 toolkit and powered by GStreamer with OpenGL rendering.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       %{libname} = %{version}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
Development files for Clapper.

%package -n %{girname}
Summary:        Clapper library typelib

%description  -n %{girname}
%{summary}.

%package -n %{libname}
Summary:	A GTK4 library to fir Ckaooer
Group:		System/Libraries
Requires:	%{name} = %{version}

%description -n %{libname}
This package provides the shared library for Clapper.


%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%find_lang com.github.rafostar.Clapper

%files -f com.github.rafostar.Clapper.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/com.github.rafostar.Clapper
%{_datadir}/com.github.rafostar.Clapper
%{_datadir}/glib-2.0/schemas/com.github.rafostar.Clapper.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/com.github.rafostar.Clapper.metainfo.xml
%{_datadir}/mime/packages/com.github.rafostar.Clapper.xml
%{_datadir}/applications/com.github.rafostar.Clapper.desktop
%{_datadir}/dbus-1/services/com.github.rafostar.Clapper.service
%dir %{_libdir}/clapper-1.0
%dir %{_libdir}/clapper-1.0/gst
%dir %{_libdir}/clapper-1.0/gst/plugin
%dir %{_libdir}/clapper-1.0/gst/plugin/importers
%{_libdir}/clapper-1.0/gst/plugin/importers/*.so
%dir %{_libdir}/gstreamer-1.0
%{_libdir}/gstreamer-1.0/*.so

%files -n %{libname}
%dir %{_libdir}/com.github.rafostar.Clapper
%{_libdir}/com.github.rafostar.Clapper/*.so.*
%{_libdir}/libgstclapperglbaseimporter.so.*

%files -n %{girname}
%dir %{_libdir}/com.github.rafostar.Clapper/girepository-1.0
%{_libdir}/com.github.rafostar.Clapper/girepository-1.0/GstClapper-1.0.typelib

%files -n %{devname}
%{_libdir}/com.github.rafostar.Clapper/*.so
%{_libdir}/*.so
%{_datadir}/gir-1.0/GstClapper-1.0.gir
