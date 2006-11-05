#
# TODO
#	- simplify spec
#	- prepare init script for web interface
#
%include	/usr/lib/rpm/macros.perl
Summary:	The Metasploit Framework - a powerful tool for penetration testing
Summary(pl):	Metasploit Framework - narzêdzie wspomagaj±ce testy penetracyjne
Name:		metasploit
Version:	2.7
Release:	0.1
License:	GPL v2 / Artistic
Group:		Applications
Source0:	http://www.metasploit.com/tools/framework-%{version}.tar.gz
# Source0-md5:	ea592cfb006e1b2510b533cece4ecb18
Patch0:		%{name}-false.patch
URL:		http://www.metasploit.com/projects/Framework/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Term-ReadLine-Gnu
Requires:	perl-base >= 1:5.8.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Metasploit Framework is an advanced open-source platform for
developing, testing, and using exploit code. This project initially
started off as a portable network game and has evolved into a
powerful tool for penetration testing, exploit development, and
vulnerability research.

%description -l pl
Metasploit Framework to zaawansowana platforma do tworzenia,
testowania i wykorzystywania kodu exploitów. Projekt ten pocz±tkowo
mai³ byæ przeno¶n± gr± sieciow±, a wyewoluowa³ do potê¿nego narzêdzia
do testów penetracyjnych, tworzenia exploitów i wyszukiwania luk.

%prep
%setup -q -n framework-%{version}
%patch0 -p1 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit

install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/tools
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/t
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/payloads
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/payloads/external
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/nops
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/exploits
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/encoders
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/data/passivex
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfweb/themes
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfweb/themes/gwhite
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfweb/themes/gblack
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfweb/themes/default
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfweb/icons
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfpescan
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfpayload
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/data/meterpreter
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/data
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit/lib

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Digest/Perl
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Msf/Encoder
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Msf/Nop
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/BSD/ia32
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/BSDi/ia32
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/Linux/ia32
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/OSX/ppc
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/Windows/ia32
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Msf/Socket
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/NetPacket
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Encoding
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Meterpreter/Crypto
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Meterpreter/Extension/Client
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Nasm
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Poly/BlockMaster
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Socket

install msf*					$RPM_BUILD_ROOT%{_libdir}/metasploit

install tools/* 				$RPM_BUILD_ROOT%{_libdir}/metasploit/tools
install	t/dcerpc.pl 				$RPM_BUILD_ROOT%{_libdir}/metasploit/t
install	payloads/*.pm				$RPM_BUILD_ROOT%{_libdir}/metasploit/payloads
install	payloads/external/*.py			$RPM_BUILD_ROOT%{_libdir}/metasploit/payloads/external
install	nops/*.pm				$RPM_BUILD_ROOT%{_libdir}/metasploit/nops
install	exploits/*.pm				$RPM_BUILD_ROOT%{_libdir}/metasploit/exploits
install	encoders/*.pm				$RPM_BUILD_ROOT%{_libdir}/metasploit/encoders
install	data/passivex/passivex.dll		$RPM_BUILD_ROOT%{_libdir}/metasploit/data/passivex
install	data/msfweb/themes/gwhite/*		$RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfweb/themes/gwhite
install	data/msfweb/themes/gblack/*		$RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfweb/themes/gblack
install	data/msfweb/themes/default/*		$RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfweb/themes/default
install	data/msfweb/icons/*.gif			$RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfweb/icons
install	data/msfpescan/identify.txt		$RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfpescan
install	data/msfpayload/template.exe		$RPM_BUILD_ROOT%{_libdir}/metasploit/data/msfpayload
install	data/meterpreter/ext_server_*.dll	$RPM_BUILD_ROOT%{_libdir}/metasploit/data/meterpreter
install	data/dce_errors.txt			$RPM_BUILD_ROOT%{_libdir}/metasploit/data
install	data/rpc_names				$RPM_BUILD_ROOT%{_libdir}/metasploit/data
install	data/shelldemo				$RPM_BUILD_ROOT%{_libdir}/metasploit/data
install	data/smb_errors.txt			$RPM_BUILD_ROOT%{_libdir}/metasploit/data
install	data/vncdll.dll				$RPM_BUILD_ROOT%{_libdir}/metasploit/data

install lib/*.pm 				$RPM_BUILD_ROOT%{perl_vendorlib}
install lib/Digest/*.pm 			$RPM_BUILD_ROOT%{perl_vendorlib}/Digest
install lib/Digest/Perl/*.pm			$RPM_BUILD_ROOT%{perl_vendorlib}/Digest/Perl
install lib/Msf/*.pm 				$RPM_BUILD_ROOT%{perl_vendorlib}/Msf
install lib/Msf/Encoder/*.pm 			$RPM_BUILD_ROOT%{perl_vendorlib}/Msf/Encoder
install lib/Msf/Nop/*.pm 			$RPM_BUILD_ROOT%{perl_vendorlib}/Msf/Nop
install lib/Msf/PayloadComponent/*.pm 		$RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent
install lib/Msf/PayloadComponent/BSD/*.pm 	$RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/BSD
install lib/Msf/PayloadComponent/BSD/ia32/*.pm 	$RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/BSD/ia32
install lib/Msf/PayloadComponent/BSDi/*.pm 	$RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/BSDi
install lib/Msf/PayloadComponent/BSDi/ia32/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/BSDi/ia32
install lib/Msf/PayloadComponent/Linux/*.pm 	$RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/Linux
install lib/Msf/PayloadComponent/Linux/ia32/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/Linux/ia32
install lib/Msf/PayloadComponent/OSX/*.pm 	$RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/OSX
install lib/Msf/PayloadComponent/OSX/ppc/*.pm 	$RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/OSX/ppc
install lib/Msf/PayloadComponent/Windows/*.pm 	$RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/Windows
install lib/Msf/PayloadComponent/Windows/ia32/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Msf/PayloadComponent/Windows/ia32
install lib/Msf/Socket/*.pm 			$RPM_BUILD_ROOT%{perl_vendorlib}/Msf/Socket
install lib/NetPacket/*.pm 			$RPM_BUILD_ROOT%{perl_vendorlib}/NetPacket
install lib/Pex/*.pm 				$RPM_BUILD_ROOT%{perl_vendorlib}/Pex
install lib/Pex/Encoding/*.pm 			$RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Encoding
install lib/Pex/Meterpreter/*.pm 		$RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Meterpreter
install lib/Pex/Meterpreter/Crypto/*.pm 	$RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Meterpreter/Crypto
install lib/Pex/Meterpreter/Extension/Client/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Meterpreter/Extension/Client
install lib/Pex/Nasm/*.pm 			$RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Nasm
install lib/Pex/Poly/*.pm 			$RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Poly
install lib/Pex/Poly/BlockMaster/*.pm 		$RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Poly/BlockMaster
install lib/Pex/Socket/*.pm 			$RPM_BUILD_ROOT%{perl_vendorlib}/Pex/Socket

cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/metasploit/msf* ./

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/msf*
%dir %{_libdir}/metasploit
%attr(755,root,root) %{_libdir}/metasploit/msf*

%dir %{perl_vendorlib}/Digest
%dir %{perl_vendorlib}/Digest/Perl
%dir %{perl_vendorlib}/Msf
%dir %{perl_vendorlib}/Msf/Encoder
%dir %{perl_vendorlib}/Msf/Nop
%dir %{perl_vendorlib}/Msf/PayloadComponent
%dir %{perl_vendorlib}/Msf/PayloadComponent/BSD
%dir %{perl_vendorlib}/Msf/PayloadComponent/BSD/ia32
%dir %{perl_vendorlib}/Msf/PayloadComponent/BSDi
%dir %{perl_vendorlib}/Msf/PayloadComponent/BSDi/ia32
%dir %{perl_vendorlib}/Msf/PayloadComponent/Linux
%dir %{perl_vendorlib}/Msf/PayloadComponent/Linux/ia32
%dir %{perl_vendorlib}/Msf/PayloadComponent/OSX
%dir %{perl_vendorlib}/Msf/PayloadComponent/OSX/ppc
%dir %{perl_vendorlib}/Msf/PayloadComponent/Windows
%dir %{perl_vendorlib}/Msf/PayloadComponent/Windows/ia32
%dir %{perl_vendorlib}/Msf/Socket
%dir %{perl_vendorlib}/NetPacket
%dir %{perl_vendorlib}/Pex
%dir %{perl_vendorlib}/Pex/Encoding
%dir %{perl_vendorlib}/Pex/Meterpreter
%dir %{perl_vendorlib}/Pex/Meterpreter/Crypto
%dir %{perl_vendorlib}/Pex/Meterpreter/Extension
%dir %{perl_vendorlib}/Pex/Meterpreter/Extension/Client
%dir %{perl_vendorlib}/Pex/Nasm
%dir %{perl_vendorlib}/Pex/Poly
%dir %{perl_vendorlib}/Pex/Poly/BlockMaster
%dir %{perl_vendorlib}/Pex/Socket

%dir %{_libdir}/metasploit/tools
%dir %{_libdir}/metasploit/t
%dir %{_libdir}/metasploit/payloads
%dir %{_libdir}/metasploit/payloads/external
%dir %{_libdir}/metasploit/nops
%dir %{_libdir}/metasploit/exploits
%dir %{_libdir}/metasploit/encoders
%dir %{_libdir}/metasploit/data/passivex
%dir %{_libdir}/metasploit/data/msfweb/themes
%dir %{_libdir}/metasploit/data/msfweb/themes/gwhite
%dir %{_libdir}/metasploit/data/msfweb/themes/gblack
%dir %{_libdir}/metasploit/data/msfweb/themes/default
%dir %{_libdir}/metasploit/data/msfweb/icons
%dir %{_libdir}/metasploit/data/msfpescan
%dir %{_libdir}/metasploit/data/msfpayload
%dir %{_libdir}/metasploit/data/meterpreter
%dir %{_libdir}/metasploit/data

%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Digest/*.pm
%{perl_vendorlib}/Digest/Perl/*.pm
%{perl_vendorlib}/Msf/*.pm
%{perl_vendorlib}/Msf/Encoder/*.pm
%{perl_vendorlib}/Msf/Nop/*.pm
%{perl_vendorlib}/Msf/PayloadComponent/*.pm
%{perl_vendorlib}/Msf/PayloadComponent/BSD/*.pm
%{perl_vendorlib}/Msf/PayloadComponent/BSD/ia32/*.pm
%{perl_vendorlib}/Msf/PayloadComponent/BSDi/*.pm
%{perl_vendorlib}/Msf/PayloadComponent/BSDi/ia32/*.pm
%{perl_vendorlib}/Msf/PayloadComponent/Linux/*.pm
%{perl_vendorlib}/Msf/PayloadComponent/Linux/ia32/*.pm
%{perl_vendorlib}/Msf/PayloadComponent/OSX/*.pm
%{perl_vendorlib}/Msf/PayloadComponent/OSX/ppc/*.pm
%{perl_vendorlib}/Msf/PayloadComponent/Windows/*.pm
%{perl_vendorlib}/Msf/PayloadComponent/Windows/ia32/*.pm
%{perl_vendorlib}/Msf/Socket/*.pm
%{perl_vendorlib}/NetPacket/*.pm
%{perl_vendorlib}/Pex/*.pm
%{perl_vendorlib}/Pex/Encoding/*.pm
%{perl_vendorlib}/Pex/Meterpreter/*.pm
%{perl_vendorlib}/Pex/Meterpreter/Crypto/*.pm
%{perl_vendorlib}/Pex/Meterpreter/Extension/Client/*.pm
%{perl_vendorlib}/Pex/Nasm/*.pm
%{perl_vendorlib}/Pex/Poly/*.pm
%{perl_vendorlib}/Pex/Poly/BlockMaster/*.pm
%{perl_vendorlib}/Pex/Socket/*.pm

%{_libdir}/metasploit/tools/*
%{_libdir}/metasploit/t/dcerpc.pl
%{_libdir}/metasploit/payloads/*.pm
%{_libdir}/metasploit/payloads/external/*.py
%{_libdir}/metasploit/nops/*.pm
%{_libdir}/metasploit/exploits/*.pm
%{_libdir}/metasploit/encoders/*.pm
%{_libdir}/metasploit/data/passivex/passivex.dll
%{_libdir}/metasploit/data/msfweb/themes/gwhite/*
%{_libdir}/metasploit/data/msfweb/themes/gblack/*
%{_libdir}/metasploit/data/msfweb/themes/default/*
%{_libdir}/metasploit/data/msfweb/icons/*.gif
%{_libdir}/metasploit/data/msfpescan/identify.txt
%{_libdir}/metasploit/data/msfpayload/template.exe
%{_libdir}/metasploit/data/meterpreter/ext_server_*.dll
%{_libdir}/metasploit/data/dce_errors.txt
%{_libdir}/metasploit/data/rpc_names
%{_libdir}/metasploit/data/shelldemo
%{_libdir}/metasploit/data/smb_errors.txt
%{_libdir}/metasploit/data/vncdll.dll
