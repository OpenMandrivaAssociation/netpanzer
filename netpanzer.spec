%define	name	netpanzer
%define	version	0.8.2
%define release	%mkrel 3
%define	Summary	An online multiplayer tactical warfare game

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://netpanzer.berlios.de/
Source0:  	http://download.berlios.de/netpanzer/%{name}-%{version}.tar.bz2
Patch0:		netpanzer-gcc-4.1-extra-qualification.patch
Patch1:		netpanzer-cve-2005-2295.patch
Patch2:		netpanzer-cve-2006-2575.patch
#Source10:	%{name}-16x16.png
#Source11:	%{name}-32x32.png
#Source12:	%{name}-48x48.png
License:	GPL
Group:		Games/Strategy
Summary:	%{Summary}
BuildRequires:	SDL_net-devel SDL_mixer-devel SDL_image-devel SDL_ttf-devel
BuildRequires:	jam libwxgtk-devel physfs-devel libxml2-devel
BuildRequires:	imagemagick desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%build
CXXFLAGS="$RPM_OPT_FLAGS -O3" \
%configure2_5x	--datadir=%{_gamesdatadir} \
		--bindir=%{_gamesbindir}
perl -pi -e "s#-g3##g" Jamrules
jam -d2 %_smp_mflags

%install
%{__rm} -rf $RPM_BUILD_ROOT
(jam -s libdir=$RPM_BUILD_ROOT%{_libdir} -s bindir=$RPM_BUILD_ROOT%{_gamesbindir} -s mandir=$RPM_BUILD_ROOT%{_mandir} -s icondir=$RPM_BUILD_ROOT%{_datadir}/pixmaps/ -s appdocdir=docdir -s applicationsdir=$RPM_BUILD_ROOT%{_datadir}/applications/ install)
cp docs/*.html -f docdir


desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Game;StrategyGame" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Strategy" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#%{__install} %{SOURCE10} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
#%{__install} %{SOURCE11} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
#%{__install} %{SOURCE12} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%{__install} -d $RPM_BUILD_ROOT{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert %{name}.png -size 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert %{name}.png -size 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert %{name}.png -size 48x48 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,games,755)
%doc docdir/*
#%{_datadir}/pixmaps/*
#%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%defattr(755,root,games,755)
%{_gamesbindir}/*

