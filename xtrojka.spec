Summary:	An X Window System falling blocks game
Summary(de):	Spiel mit fallenden Steinen
Summary(fr):	Jeu de blocs qui tombent
Summary(tr):	Düþen bloklarý yerleþtirme oyunu
Name:		xtrojka
Version:	1.2.3
Release:	14
License:	Distributable
Group:		X11/Applications/Games
Group(de):	X11/Aplikacje/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/%{name}123.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-make.patch
Icon:		xtrojka.xpm
BuildRequires:	Xaw3d-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The xtrojka game is an X Window System game of falling blocks, like
Xjewel or Tetris.

%description -l de
Ähnlich wie bei xjewels oder tetris, müssen Sie in diesem Spiel die
Spielfläche von fallenden Blöcken freihalten.

Eine Variation des süchtigmachenden Klassikers.

%description -l fr
Ce jeu est similaire à xjewels ou tetris, il faut supprimer les blocs
qui tombent dans la surface de jeu.

Un variation du jeu classique.

%description -l tr
xjewels ve tetris'e benzer þekilde, düþen bloklarý uygun þekilde
yerleþtirmeye yönelik bir oyun.

%prep
%setup -q -n xtrojka123
%patch -p1

%build
cp XTrojka.uk XTrojka
./resgen
%{__make} CFLAGS="%{rpmcflags} -DXPM -DLINUX \
	-DSCOREFILE='\"/var/lib/games/xtrojka.score\"' -L%%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_datadir}/pixmaps,%{_bindir},%{_mandir}/man6} \
	$RPM_BUILD_ROOT/var/lib/games

%{__make} install \
	TARGET_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man6 \
	HSFILE=$RPM_BUILD_ROOT/var/lib/games/xtrojka.score

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/xtrojka
%attr(0664,root,games) %config /var/lib/games/xtrojka.score
%{_mandir}/man6/*
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
