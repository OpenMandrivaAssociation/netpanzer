Name:		netpanzer
Version:	0.8.4
Release:	3
Summary:	An online multiplayer tactical warfare game
License:	GPLv2+
Group:		Games/Strategy
URL:		https://netpanzer.berlios.de/
Source0:	http://download.berlios.de/netpanzer/%{name}-%{version}.tar.bz2
Patch0:		netpanzer-0.8.4-gcc470.patch
Patch1:		netpanzer-0.8.4-optflags.patch
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	scons
BuildRequires:	physfs-devel
BuildRequires:	imagemagick

%description
netPanzer is an online multiplayer tactical warfare game designed for
play across the Internet and over LAN systems. One on one games are
possible via direct connect or modem. netPanzer is designed for FAST
ACTION combat -- it is not another resource management clone. In fact,
there aren't any resources at all. Each player will have many units of
different types at their disposal. Players can fight until their units
are destroyed -- then respawn and keep on going. The game is real-time,
but it's based on quick tactical action and unit management. Battles
progress quickly and constantly; in fact, they never let up. There is no
stop in the action because there is no waiting for resources to be
collected and converted into weaponry. Players can join or leave
multiplayer games at any time.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%scons datadir=%{_gamesdatadir}/%{name}

%install
install -D -m 755 %{name} %{buildroot}%{_gamesbindir}/%{name}

mkdir -p %{buildroot}%{_gamesdatadir}/%{name}
cp -pr cache/ %{buildroot}%{_gamesdatadir}/%{name}/
cp -pr maps/ %{buildroot}%{_gamesdatadir}/%{name}/
cp -pr pics/ %{buildroot}%{_gamesdatadir}/%{name}/
cp -pr powerups/ %{buildroot}%{_gamesdatadir}/%{name}/
cp -pr scripts/ %{buildroot}%{_gamesdatadir}/%{name}/
cp -pr units/ %{buildroot}%{_gamesdatadir}/%{name}/
cp -pr wads/ %{buildroot}%{_gamesdatadir}/%{name}/
cp -pr sound/ %{buildroot}%{_gamesdatadir}/%{name}/

install -D -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

for N in 16 32 48 64 128; do convert %{name}.png -resize ${N}x${N} $N.png; done
install -D -m 644 16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -D -m 644 32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -D -m 644 48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -D -m 644 64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D -m 644 128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

install -D -m 644 docs/%{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6

%files
%doc COPYING README *.txt docs/*.txt
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*

%changelog
* Fri Apr 27 2012 Andrey Bondrov <abondrov@mandriva.org> 0.8.4-1mdv2011.0
+ Revision: 794108
- New version 0.8.4, switch from jam to scons, update BuildRequires

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.8.2-3mdv2010.0
+ Revision: 440324
- rebuild

* Mon Apr 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-2mdv2009.1
+ Revision: 366801
- fix build
- fix missing files
- fix crash on x86_64
- spec cleanup

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Oct 24 2007 Jérôme Soyer <saispo@mandriva.org> 0.8.2-1mdv2008.1
+ Revision: 101788
- New release


* Tue Sep 12 2006 Emmanuel Andry <eandry@mandriva.org> 0.8-2mdv2007.0
- %%mkrel
- xdg menu
- build with jam instead of boost-jam (doesn't compile)
- add P0 from fedora to fix build
- add P1 and P2 from fedora for cve-2005-2295 and cve-2006-2575

* Thu Feb 03 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.8-1mdk
- 0.8

* Tue Jan 11 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2.0-0.rc4.1mdk
- 0.2.0rc4

* Wed Nov 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2.0-0.rc3.1mdk
- 0.2.0rc3
- don't quit on minor error during install

* Tue Oct 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2.0-0.rc2.1mdk
- 0.2.0rc2

* Fri Mar 05 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.5-1mdk
- 0.1.5
- drop own icons, use icons shipped with source

* Tue Mar 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.4-2mdk
- buildrequires
- do parallel build

* Fri Feb 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.4-1mdk
- 0.1.4

* Thu Jan 08 2004 Olivier Blin <blino@mandrake.org> 0.1.3-2mdk
- BuildRequires (clean, libxml2-devel)

* Tue Jan 06 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.3-1mdk
- 0.1.3

* Wed Nov 12 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.2-1mdk
- 0.1.2

* Thu Oct 16 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.1-1mdk
- initial mdk release

