Name:          vanilla-first-setup
Version:       1.7.2
Release:       1%{?dist}
Summary:       This utility is meant to be used in Vanilla OS as a first-setup wizard. It takes care of the user choices.
License:       GPL 3.0
URL:           https://github.com/Vanilla-OS/first-setup
Source:        https://github.com/Vanilla-OS/first-setup/archive/refs/tags/%{version}.tar.gz

BuildRequires: make
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: libadwaita-devel
BuildRequires: python3-devel
BuildRequires: gettext
BuildRequires: desktop-file-utils

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

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-processor
%{_datadir}/appdata/org.vanillaos.FirstSetup.appdata.xml
%{_datadir}/applications/org.vanillaos.FirstSetup.desktop
%{_datadir}/glib-2.0/schemas/org.vanillaos.FirstSetup.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/locale/*/LC_MESSAGES/vanilla-first-setup.mo
%{_datadir}/org.vanillaos.FirstSetup/*
