Summary:	An X Window System falling blocks game
Summary(de):	Spiel mit fallenden Steinen
Summary(fr):	Jeu de blocs qui tombent
Summary(pl):	Gra w spadaj�ce bloki pod X Window System
Summary(tr):	D��en bloklar� yerle�tirme oyunu
Name:		xtrojka
Version:	1.2.3
Release:	16
License:	distributable
Group:		X11/Applications/Games
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
�hnlich wie bei xjewels oder tetris, m�ssen Sie in diesem Spiel die
Spielfl�che von fallenden Bl�cken freihalten.

Eine Variation des s�chtigmachenden Klassikers.

%description -l fr
Ce jeu est similaire � xjewels ou tetris, il faut supprimer les blocs
qui tombent dans la surface de jeu.

Un variation du jeu classique.

%description -l pl
xtrojka jest gr� pod X Window System ze spadaj�cymi blokami, podobn�
do Xjewel albo Tetrisa.

%description -l tr
xjewels ve tetris'e benzer �ekilde, d��en bloklar� uygun �ekilde
yerle�tirmeye y�nelik bir oyun.

%prep
%setup -q -n xtrojka123
%patch -p1

%build
cp -f XTrojka.uk XTrojka
./resgen
%{__make} CFLAGS="%{rpmcflags} -DXPM -DLINUX \
	-DSCOREFILE='\"/var/games/xtrojka.score\"' -L%%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_datadir}/pixmaps} \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,/var/games}

%{__make} install \
	TARGET_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man6 \
	HSFILE=$RPM_BUILD_ROOT/var/games/xtrojka.score

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/xtrojka
%attr(0664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/xtrojka.score
%{_mandir}/man6/*
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
