Name:		netpanzer
Version:	0.8.4
Release:	%mkrel 1
Summary:	An online multiplayer tactical warfare game
License:	GPLv2+
Group:		Games/Strategy
URL:		http://netpanzer.berlios.de/
Source0:  	http://download.berlios.de/netpanzer/%{name}-%{version}.tar.bz2
Patch1:		netpanzer-0.8.4-optflags.patch
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_mixer-devel
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
%patch1 -p 1

%build
%scons datadir=%{_gamesdatadir}/%{name}

%install
%__rm -rf %{buildroot}

%__install -D -m 755 %{name} %{buildroot}%{_gamesbindir}/%{name}

%__mkdir_p %{buildroot}%{_gamesdatadir}/%{name}
%__cp -pr cache/ %{buildroot}%{_gamesdatadir}/%{name}/
%__cp -pr maps/ %{buildroot}%{_gamesdatadir}/%{name}/
%__cp -pr pics/ %{buildroot}%{_gamesdatadir}/%{name}/
%__cp -pr powerups/ %{buildroot}%{_gamesdatadir}/%{name}/
%__cp -pr scripts/ %{buildroot}%{_gamesdatadir}/%{name}/
%__cp -pr units/ %{buildroot}%{_gamesdatadir}/%{name}/
%__cp -pr wads/ %{buildroot}%{_gamesdatadir}/%{name}/
%__cp -pr sound/ %{buildroot}%{_gamesdatadir}/%{name}/

%__install -D -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

for N in 16 32 48 64 128; do convert %{name}.png -resize ${N}x${N} $N.png; done
%__install -D -m 644 16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D -m 644 32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -D -m 644 48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%__install -D -m 644 64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D -m 644 128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

%__install -D -m 644 docs/%{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6


%clean
%__rm -rf %{buildroot}

%files
%doc COPYING README *.txt docs/*.txt
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*

