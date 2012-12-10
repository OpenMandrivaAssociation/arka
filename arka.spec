%define name arka
%define version 0.11
%define release %mkrel 5

Summary: GUI for Genpak (gp) set of bioinformatics utilities
Name: %name
Version: %version
Release: %release
License: GPLv2
Group: Sciences/Chemistry
URL: http://www.bioinformatics.org/genpak
Source: %name-%version.tar.bz2
Patch0: %{name}-0.11-fix-overlinking.patch.bz2
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
%patch0 -p1

%build
%make LIBDIR=%{_libdir}

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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=arka
Categories=Science;Chemistry;
Name=Arka
Icon=chemistry_section
Comment=GUI for Genpak
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.TXT LICENSE.TXT CHANGES.TXT TODO.TXT
%config(noreplace) /etc/arkarc
%_bindir/%name
%_iconsdir/%{name}*
%_mandir/man1/%{name}*
%{_datadir}/applications/mandriva-%name.desktop



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11-5mdv2011.0
+ Revision: 616603
- the mass rebuild of 2010.0 packages

* Tue May 19 2009 Jérôme Brenier <incubusss@mandriva.org> 0.11-4mdv2010.0
+ Revision: 377637
+ rebuild (emptylog)

* Tue May 19 2009 Jérôme Brenier <incubusss@mandriva.org> 0.11-3mdv2010.0
+ Revision: 377634
- fix license (GPLv2)
- fix overlinking (patch added)

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.11-3mdv2009.0
+ Revision: 218430
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.11-3mdv2008.1
+ Revision: 132148
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import arka


* Thu Jan 05 2005 Lenny Cartier <lenny@mandriva.com> 0.11-3mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.11-2mdk
- rebuild

* Wed Jan 08 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.11-1mdk
- from Austin Acton <aacton@yorku.ca> :
	- initial package for Mandrake 9
