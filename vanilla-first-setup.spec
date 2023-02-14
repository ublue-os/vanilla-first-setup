Name:          vanilla-first-setup
Version:       1.7.2
Release:       1%{?dist}
Summary:       This utility is meant to be used in Vanilla OS as a first-setup wizard. It takes care of the user choices.
License:       GPL 3.0
URL:           https://github.com/Vanilla-OS/first-setup
Source:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: gettext
BuildRequires: desktop-file-utils
	
BuildRequires: pkgconfig(libadwaita-1) >= 1.1.99

%description
This utility is meant to be used in Vanilla OS as a first-setup wizard. It's purpose is to help the user to configure the system to their needs, e.g. by configuring snap, flatpak, flathub, etc.

# Disable debug packages
%define debug_package %{nil}

%prep
%autosetup -p 0 -n first-setup-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%files -f %{name}.lang
%license LICENSE
%doc README.md
%attr(755, root, root) %{_bindir}/%{name}
%attr(755, root, root) %{_bindir}/%{name}-processor
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/org.vanillaos.FirstSetup/*
