Summary:	A simple music player for GNOME
Summary(pl):	Prosty odtwarzacz muzyczny dla GNOME
Name:		lindele
Version:	0.1.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.gna.org/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6d5387fd607fe0516bcc3ddd84dc4a77
Patch0:		%{name}-desktop.patch
URL:		http://projects.subpop.net/lindele/
BuildRequires:	gstreamer-GConf-devel >= 0.8.0
BuildRequires:	gstreamer-plugins-devel >= 0.8.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	taglib-devel = 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lindele is a music player for GNOME, designed to be simply a player,
and not much more. It uses GStreamer for blayback, so supports any
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

%description -l pl
Lindele to prosty odtwarzacz muzyczny dla GNOME, zaprojektowany aby
byæ poprostu odtwarzaczem i niczym wiêcej. U¿ywa GStreamer'a do
odtwarzania, wiêc wspiera wszystkie pliki, które GStreamer odtwarza.
U¿ywa TagLib do edycji znaczników.
Mo¿liwo¶ci:
- odczyt i zapis playlist PLS
- odczyt i czê¶æiowy zapis playlist M3U
- losowe odtwarzanie i powtarzanie
- przechwytywanie klawiszy multimedialnych
- ikona w obszarze powiadamiania
- sortowanie playlist
- przeszukiwanie playlist
- ustawienia

%prep
%setup -q
%patch0 -p1

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
%{_datadir}/%{name}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
