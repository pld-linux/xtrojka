Summary: An X Window System falling blocks game.
Name: xtrojka
Version: 1.2.3
Release: 6
Copyright: distributable
Group: Amusements/Games
Source: ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/xtrojka123.tar.gz
Patch: xtrojka-1.2.3-make.patch
BuildRoot: /var/tmp/xtrojka-root

%description
The xtrojka game is an X Window System game of falling blocks, like
Xjewel or Tetris.

%prep
%setup -q -n xtrojka123
%patch -p1

%build
cp XTrojka.uk XTrojka
./resgen
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man6}
mkdir -p $RPM_BUILD_ROOT/var/lib/games

make	TARGET_DIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
	MANDIR=$RPM_BUILD_ROOT/usr/X11R6/man/man6 \
	HSFILE=$RPM_BUILD_ROOT/var/lib/games/xtrojka.score \
	install
##install -m 644 xtrojka.6 $RPM_BUILD_ROOT/usr/X11R6/man/man6/xtrojka.6
##cp /dev/null $RPM_BUILD_ROOT/var/lib/games/xtrojka.score
chmod 0666 $RPM_BUILD_ROOT/var/lib/games/xtrojka.score
strip $RPM_BUILD_ROOT/usr/X11R6/bin/xtrojka

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xtrojka <<EOF
xtrojka name "xtrojka"
xtrojka description "xtrojka"
xtrojka group Games/Video
xtrojka exec "xtrojka &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xtrojka
/usr/X11R6/man/man6/xtrojka.6
%config /var/lib/games/xtrojka.score
%config /etc/X11/wmconfig/xtrojka
