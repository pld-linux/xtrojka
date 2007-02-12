Summary:	An X Window System falling blocks game
Summary(de.UTF-8):	Spiel mit fallenden Steinen
Summary(fr.UTF-8):	Jeu de blocs qui tombent
Summary(pl.UTF-8):	Gra w spadające bloki pod X Window System
Summary(tr.UTF-8):	Düşen blokları yerleştirme oyunu
Name:		xtrojka
Version:	1.2.3
Release:	19
License:	distributable
Group:		X11/Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/%{name}123.tar.gz
# Source0-md5:	58f66c2e59205312af4dcd128a6a4040
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-make.patch
Patch1:		%{name}-errno.patch
BuildRequires:	Xaw3d-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xtrojka game is an X Window System game of falling blocks, like
Xjewel or Tetris.

%description -l de.UTF-8
Ähnlich wie bei xjewels oder tetris, müssen Sie in diesem Spiel die
Spielfläche von fallenden Blöcken freihalten.

Eine Variation des süchtigmachenden Klassikers.

%description -l fr.UTF-8
Ce jeu est similaire à xjewels ou tetris, il faut supprimer les blocs
qui tombent dans la surface de jeu.

Un variation du jeu classique.

%description -l pl.UTF-8
xtrojka jest grą pod X Window System ze spadającymi blokami, podobną
do Xjewel albo Tetrisa.

%description -l tr.UTF-8
xjewels ve tetris'e benzer şekilde, düşen blokları uygun şekilde
yerleştirmeye yönelik bir oyun.

%prep
%setup -q -n %{name}123
%patch0 -p1
%patch1 -p1

%build
cp -f XTrojka.uk XTrojka
./resgen
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DXPM -DLINUX -DSCOREFILE='\"/var/games/xtrojka.score\"'" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,/var/games}

%{__make} install \
	TARGET_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man6 \
	HSFILE=$RPM_BUILD_ROOT/var/games/xtrojka.score

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/xtrojka
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/xtrojka.score
%{_mandir}/man6/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
