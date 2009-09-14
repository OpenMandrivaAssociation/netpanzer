%define	name	netpanzer
%define	version	0.8.2
%define release	%mkrel 3
%define	Summary	An online multiplayer tactical warfare game

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Strategy
Summary:	%{Summary}
URL:		http://netpanzer.berlios.de/
Source0:  	http://download.berlios.de/netpanzer/%{name}-%{version}.tar.bz2
Patch3:		netpanzer-0.8.2-fix-format-errors.patch
Patch4:		netpanzer-0.8.2-fix-stdc++-includes.patch
Patch5:		netpanzer-0.8.2-fix-crash-x86_64.patch
#Source10:	%{name}-16x16.png
#Source11:	%{name}-32x32.png
#Source12:	%{name}-48x48.png
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	jam
BuildRequires:	libwxgtk-devel
BuildRequires:	physfs-devel
BuildRequires:	libxml2-devel
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%patch3 -p 1
%patch4 -p 1
%patch5 -p 1

%build
CXXFLAGS="$RPM_OPT_FLAGS -O3" \
%configure2_5x	--datadir=%{_gamesdatadir} \
		--bindir=%{_gamesbindir}
perl -pi -e "s#-g3##g" Jamrules
jam -d2 %_smp_mflags

%install
%{__rm} -rf %{buildroot}
jam \
    -s libdir=%{buildroot}%{_libdir} \
    -s bindir=%{buildroot}%{_gamesbindir} \
    -s datadir=%{buildroot}%{_gamesdatadir} \
    -s mandir=%{buildroot}%{_mandir} \
    -s icondir=%{buildroot}%{_datadir}/pixmaps \
    -s appdocdir=docdir \
    -s applicationsdir=%{buildroot}%{_datadir}/applications/ install
cp docs/*.html -f docdir

mv %{buildroot}%{_gamesdatadir}/pixmaps %{buildroot}%{_datadir}/pixmaps


desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Game;StrategyGame" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Strategy" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#%{__install} %{SOURCE10} -D %{buildroot}%{_miconsdir}/%{name}.png
#%{__install} %{SOURCE11} -D %{buildroot}%{_iconsdir}/%{name}.png
#%{__install} %{SOURCE12} -D %{buildroot}%{_liconsdir}/%{name}.png

%{__install} -d %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert %{name}.png -size 16x16 %{buildroot}%{_miconsdir}/%{name}.png
convert %{name}.png -size 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert %{name}.png -size 48x48 %{buildroot}%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docdir/*
%{_datadir}/pixmaps/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_gamesbindir}/*

