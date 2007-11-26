%define name arka
%define version 0.11
%define release %mkrel 3

Summary: GUI for Genpak (gp) set of bioinformatics utilities
Name: %name
Version: %version
Release: %release
License: GPL
Group: Sciences/Chemistry
URL: http://www.bioinformatics.org/genpak
Source: %name-%version.tar.bz2
BuildRoot: %_tmppath/%name-root
BuildRequires: libgtk+-devel
Requires: gp

%description
Arka is a program that (1) serves as a graphical interface for any command line
driven programs, with the focus on the programs from the GP package (see
http://www.bioinformatics.org/genpak/) (2) has some nice funtions on it's one.
Main scope of the program is the manipulation and visualisation of DNA / RNA /
protein sequences.

The GP package contains many command-line utilities which fullfill a whole 
bunch of tasks (from DNA sequence searches to restriction analysis and 
determining the melting temperature of oligonucleotides). While those programs 
are convenient to use in batch processing and CGI scripts (which was the 
purpose of those programs), they lack a nice GUI. 

Arka remembers the options for the GP programs and knows what both the programs
and the options do. Besides, it has some gadgets on its own. It requires GTK+,
but doesn't need GNOME. Also, it is small and quick.

%prep
%setup -q

%build
%make

%install
mkdir -p $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
mkdir -p $RPM_BUILD_ROOT/etc
cp arka $RPM_BUILD_ROOT/%_bindir
cp icons/*.xpm $RPM_BUILD_ROOT/%_iconsdir
cp arka.1* $RPM_BUILD_ROOT/%_mandir/man1
cp arkarc $RPM_BUILD_ROOT/etc/arkarc

# menu
install -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="arka"\
needs="x11"\
section="Applications/Sciences/Chemistry"\
title="Arka"\
icon="chemistry_section.png"\
longtitle="GUI for Genpak"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.TXT LICENSE.TXT CHANGES.TXT TODO.TXT
%config(noreplace) /etc/arkarc
%_bindir/%name
%_iconsdir/%{name}*
%_mandir/man1/%{name}*
%_menudir/%name

