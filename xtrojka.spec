Summary:	An X Window System falling blocks game.
Name:		xtrojka
Version:	1.2.3
Release:	6
Copyright:	distributable
Group:		Amusements/Games
Source:		ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/%{name}123.tar.gz
Patch:		xtrojka-1.2.3-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
The xtrojka game is an X Window System game of falling blocks, like
Xjewel or Tetris.

%prep
%setup -q -n xtrojka123
%patch -p1

%build
cp XTrojka.uk XTrojka
./resgen
make CFLAGS="$RPM_OPT_FLAGS -DXPM -DLINUX -DSCOREFILE='\"/var/state/games/xtrojka.scores\"' -L/usr/X11/lib"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6}
install -d $RPM_BUILD_ROOT/var/state/games

make	TARGET_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man6 \
	HSFILE=$RPM_BUILD_ROOT/var/state/games/xtrojka.score \
	install

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/xtrojka

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man6/xtrojka.6

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xtrojka <<EOF
xtrojka name "xtrojka"
xtrojka description "xtrojka"
xtrojka group Games/Video
xtrojka exec "xtrojka &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xtrojka
%{_mandir}/man6/xtrojka.6.gz
%config /var/state/games/xtrojka.score
%config /etc/X11/wmconfig/xtrojka
