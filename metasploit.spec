# TODO:
# - add R: rails and RubyGems (msfweb)
# - some docs redundant
Summary:	The Metasploit Framework - a powerful tool for penetration testing
Summary(pl.UTF-8):	Metasploit Framework - narzędzie wspomagające testy penetracyjne
Name:		metasploit3
Version:	3.1
Release:	0.7
License:	MFL v1.2+
Group:		Applications
Source0:	http://spool.metasploit.com/releases/framework-%{version}.tar.gz
# Source0-md5:	5858d5af28933dcc22a0e22831c2f511
Patch0:		%{name}-datadir.patch
URL:		http://www.metasploit.com/framework/
BuildRequires:	sed >= 4.0
#Requires:	rails
Requires:	ruby
#Requires:	ruby-RubyGems
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Shellcode templates for various arches
%define		_noautostrip	.*%{_datadir}/metasploit3/data/templates
# blah, disable stripping, the above didn't work
%define		no_install_post_strip 1
%define		_enable_debug_packages	0

%description
The Metasploit Framework 3.1 is an advanced open-source platform for
developing, testing, and using exploit code. This project initially
started off as a portable network game and has evolved into a powerful
tool for penetration testing, exploit development, and vulnerability
research.

FYI: not all exploit modules are ported to ruby based 3.1 version, so
it is not a full replacement for Perl based Metasploit Framework 2.7.

%description -l pl.UTF-8
Metasploit Framework 3.1 to zaawansowana platforma do tworzenia,
testowania i wykorzystywania kodu exploitów. Projekt ten początkowo
maił być przenośną grą sieciową, a wyewoluował do potężnego narzędzia
do testów penetracyjnych, tworzenia exploitów i wyszukiwania luk.

INFO: Dla wykorzystującej język ruby wersji 3.1 nie przeniesiono
jeszcze wszystkich exploitów. Nie jest to pełny zamiennik Perlowego
Metasploit Framework 2.7.

%prep
%setup -q -n framework-%{version}
find -name .svn -type d -print0 | xargs -0 rm -rf
egrep -rl '/usr/local/bin/ruby|/''usr/bin/env' . | xargs %{__sed} -i -e '
	1s,#!.*/bin/ruby,#!/''usr/bin/ruby,
	1s,#!/''usr/bin/env ruby,#!/''usr/bin/ruby,
'
%patch0 -p1

# cleanup backups after patching
find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

# win32 binary with source
rm -rf tools/memdump

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

# test if we can hardlink -- %{_builddir} and $RPM_BUILD_ROOT on same partition
l=''
if cp -al README $RPM_BUILD_ROOT/README 2>/dev/null; then
	l=l
	rm -f $RPM_BUILD_ROOT/README
fi

cp -a$l . $RPM_BUILD_ROOT%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/msf* $RPM_BUILD_ROOT%{_bindir}
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README documentation/{COPYING,LICENSE,ChangeLog}
%attr(755,root,root) %{_bindir}/msfcli
%attr(755,root,root) %{_bindir}/msfconsole
%attr(755,root,root) %{_bindir}/msfd
%attr(755,root,root) %{_bindir}/msfencode
%attr(755,root,root) %{_bindir}/msfgui
%attr(755,root,root) %{_bindir}/msfopcode
%attr(755,root,root) %{_bindir}/msfpayload
%attr(755,root,root) %{_bindir}/msfpescan
%attr(755,root,root) %{_bindir}/msfweb
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_datadir}/%{name}/documentation
%{_datadir}/%{name}/external
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/modules
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/tools
