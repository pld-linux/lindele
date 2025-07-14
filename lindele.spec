Summary:	A simple music player for GNOME
Summary(pl.UTF-8):	Prosty odtwarzacz muzyczny dla GNOME
Name:		lindele
Version:	0.1.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.gna.org/lindele/%{name}-%{version}.tar.gz
# Source0-md5:	6d5387fd607fe0516bcc3ddd84dc4a77
Patch0:		%{name}-desktop.patch
URL:		http://projects.subpop.net/lindele/
BuildRequires:	gstreamer-GConf-devel >= 0.8.0
BuildRequires:	gstreamer-plugins-devel >= 0.8.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	taglib-devel >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lindele is a music player for GNOME, designed to be simply a player,
and not much more. It uses GStreamer for playback, so supports any
file GStreamer plays. And it uses TagLib for tag reading.
Features:
- read & write PLS playlists
- read & limited write M3U playlists
- random & repeat
- capture multimedia keys
- notification area icon
- playlist sorting
- playlist searching
- preferences.

%description -l pl.UTF-8
Lindele to prosty odtwarzacz muzyczny dla GNOME, zaprojektowany aby
być poprostu odtwarzaczem i niczym więcej. Używa GStreamera do
odtwarzania, więc obsługuje wszystkie pliki, które GStreamer odtwarza.
Używa TagLib do edycji znaczników.
Możliwości:
- odczyt i zapis playlist PLS
- odczyt i częśćiowy zapis playlist M3U
- losowe odtwarzanie i powtarzanie
- przechwytywanie klawiszy multimedialnych
- ikona w obszarze powiadamiania
- sortowanie playlist
- przeszukiwanie playlist
- ustawienia

%prep
%setup -q
%patch -P0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
