#
# TODO:	
#	- add R: rails and RubyGems
#	- resolve runtime problem with loading ruby modules (rex)
#	  (move stuff to %{ruby_rubylibdir} ?)
#	- fix double marking files 
#	- some docs redundant
#
Summary:	The Metasploit Framework - a powerful tool for penetration testing
Summary(pl.UTF-8):	Metasploit Framework - narzędzie wspomagające testy penetracyjne
Name:		metasploit3
Version:	3.0
Release:	0.5
License:	MFL v1.2+
Group:		Applications
Source0:	http://framework-mirrors.metasploit.com/msf/downloader/framework-%{version}.tar.gz
# Source0-md5:	ab98f0a09b371f9638c7f49f1b83f5c4
URL:		http://www.metasploit.com/projects/Framework/
Requires:	ruby
#Requires:	rails
#Requires:	ruby-RubyGems
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Metasploit Framework 3.0 is an advanced open-source platform for
developing, testing, and using exploit code. This project initially
started off as a portable network game and has evolved into a
powerful tool for penetration testing, exploit development, and
vulnerability research.

FYI: not all exploit modules are ported to ruby based 3.0 version,
so it is not a full replacement for perl based Metasploit Framework 
2.7.

%description -l pl.UTF-8
Metasploit Framework 3.0 to zaawansowana platforma do tworzenia,
testowania i wykorzystywania kodu exploitów. Projekt ten początkowo
maił być przenośną grą sieciową, a wyewoluował do potężnego narzędzia
do testów penetracyjnych, tworzenia exploitów i wyszukiwania luk.

INFO: Dla wykorzystującej język ruby wersji 3.0 nie przeniesiono 
jeszcze wszystkich exploitów. Nie jest to pełny zamiennik perlowego 
Metasploit Framework 2.7. 

%prep
%setup -q -n framework-%{version}

%install
rm -rf $RPM_BUILD_ROOT
find . -name .svn -type d -print0 | xargs -0 rm -rf

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/metasploit3

# test if we can hardlink -- %{_builddir} and $RPM_BUILD_ROOT on same partition
l=''
if cp -al README $RPM_BUILD_ROOT/README 2>/dev/null; then
	l=l
	rm -f $RPM_BUILD_ROOT/README
fi
                                                                                                                                                                                                  
cp -a$l * $RPM_BUILD_ROOT%{_libdir}/metasploit3

cp -a$l documentation/COPYING COPYING
cp -a$l documentation/LICENSE LICENSE
cp -a$l documentation/ChangeLog ChangeLog

cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/metasploit3/msf* ./

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING LICENSE ChangeLog
%attr(755,root,root) %{_bindir}/msf*
%dir %{_libdir}/metasploit3
%attr(755,root,root) %{_libdir}/metasploit3/msf*

%dir %{_libdir}/metasploit3/lib
%dir %{_libdir}/metasploit3/lib/msf
%dir %{_libdir}/metasploit3/lib/msf/ui
%dir %{_libdir}/metasploit3/lib/msf/ui/web
%dir %{_libdir}/metasploit3/lib/msf/ui/gtk2
%dir %{_libdir}/metasploit3/lib/msf/ui/console
%dir %{_libdir}/metasploit3/lib/msf/ui/console/command_dispatcher
%dir %{_libdir}/metasploit3/lib/msf/base
%dir %{_libdir}/metasploit3/lib/msf/base/persistent_storage
%dir %{_libdir}/metasploit3/lib/msf/base/serializer
%dir %{_libdir}/metasploit3/lib/msf/base/simple
%dir %{_libdir}/metasploit3/lib/msf/base/sessions
%dir %{_libdir}/metasploit3/lib/msf/core
%dir %{_libdir}/metasploit3/lib/msf/core/session
%dir %{_libdir}/metasploit3/lib/msf/core/session/provider
%dir %{_libdir}/metasploit3/lib/msf/core/auxiliary
%dir %{_libdir}/metasploit3/lib/msf/core/encoder
%dir %{_libdir}/metasploit3/lib/msf/core/encoding
%dir %{_libdir}/metasploit3/lib/msf/core/exploit
%dir %{_libdir}/metasploit3/lib/msf/core/handler
%dir %{_libdir}/metasploit3/lib/msf/core/module
%dir %{_libdir}/metasploit3/lib/msf/core/payload
%dir %{_libdir}/metasploit3/lib/msf/core/payload/windows
%dir %{_libdir}/metasploit3/lib/ole
%dir %{_libdir}/metasploit3/lib/rex
%dir %{_libdir}/metasploit3/lib/rex/io
%dir %{_libdir}/metasploit3/lib/rex/ui
%dir %{_libdir}/metasploit3/lib/rex/ui/text
%dir %{_libdir}/metasploit3/lib/rex/ui/text/input
%dir %{_libdir}/metasploit3/lib/rex/ui/text/output
%dir %{_libdir}/metasploit3/lib/rex/ui/output
%dir %{_libdir}/metasploit3/lib/rex/nop
%dir %{_libdir}/metasploit3/lib/rex/arch
%dir %{_libdir}/metasploit3/lib/rex/poly
%dir %{_libdir}/metasploit3/lib/rex/poly/register
%dir %{_libdir}/metasploit3/lib/rex/post
%dir %{_libdir}/metasploit3/lib/rex/post/dispatch_ninja
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/ui
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/ui/console
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/ui/console/command_dispatcher
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/ui/console/command_dispatcher/priv
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/ui/console/command_dispatcher/stdapi
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/channels
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/channels/pools
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/channels/streams
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/priv
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/fs
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/net
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/net/socket_subsystem
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/sys
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/sys/registry_subsystem
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/sys/event_log_subsystem
%dir %{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/sys/process_subsystem
%dir %{_libdir}/metasploit3/lib/rex/sync
%dir %{_libdir}/metasploit3/lib/rex/proto
%dir %{_libdir}/metasploit3/lib/rex/proto/smb
%dir %{_libdir}/metasploit3/lib/rex/proto/http
%dir %{_libdir}/metasploit3/lib/rex/proto/http/handler
%dir %{_libdir}/metasploit3/lib/rex/proto/dcerpc
%dir %{_libdir}/metasploit3/lib/rex/proto/sunrpc
%dir %{_libdir}/metasploit3/lib/rex/platforms
%dir %{_libdir}/metasploit3/lib/rex/encoder
%dir %{_libdir}/metasploit3/lib/rex/encoder/xor
%dir %{_libdir}/metasploit3/lib/rex/encoder/alpha2
%dir %{_libdir}/metasploit3/lib/rex/logging
%dir %{_libdir}/metasploit3/lib/rex/logging/sinks
%dir %{_libdir}/metasploit3/lib/rex/encoders
%dir %{_libdir}/metasploit3/lib/rex/encoding
%dir %{_libdir}/metasploit3/lib/rex/encoding/xor
%dir %{_libdir}/metasploit3/lib/rex/struct2
%dir %{_libdir}/metasploit3/lib/rex/payloads
%dir %{_libdir}/metasploit3/lib/rex/payloads/win32
%dir %{_libdir}/metasploit3/lib/rex/payloads/win32/kernel
%dir %{_libdir}/metasploit3/lib/rex/parser
%dir %{_libdir}/metasploit3/lib/rex/pescan
%dir %{_libdir}/metasploit3/lib/rex/socket
%dir %{_libdir}/metasploit3/lib/rex/socket/comm
%dir %{_libdir}/metasploit3/lib/rex/services
%dir %{_libdir}/metasploit3/lib/rex/exploitation
%dir %{_libdir}/metasploit3/lib/rex/peparsey
%dir %{_libdir}/metasploit3/lib/rex/peparsey/image_source
%dir %{_libdir}/metasploit3/lib/rex/assembly
%dir %{_libdir}/metasploit3/data
%dir %{_libdir}/metasploit3/data/sql
%dir %{_libdir}/metasploit3/data/exploits
%dir %{_libdir}/metasploit3/data/msfpescan
%dir %{_libdir}/metasploit3/data/passivex
%dir %{_libdir}/metasploit3/data/msfgui
%dir %{_libdir}/metasploit3/data/msfgui/pix
%dir %{_libdir}/metasploit3/data/msfgui/style
%dir %{_libdir}/metasploit3/data/msfweb
%dir %{_libdir}/metasploit3/data/msfweb/app
%dir %{_libdir}/metasploit3/data/msfweb/app/views
%dir %{_libdir}/metasploit3/data/msfweb/app/views/ide
%dir %{_libdir}/metasploit3/data/msfweb/app/views/msf
%dir %{_libdir}/metasploit3/data/msfweb/app/views/jobs
%dir %{_libdir}/metasploit3/data/msfweb/app/views/nops
%dir %{_libdir}/metasploit3/data/msfweb/app/views/exploits
%dir %{_libdir}/metasploit3/data/msfweb/app/views/console
%dir %{_libdir}/metasploit3/data/msfweb/app/views/layouts
%dir %{_libdir}/metasploit3/data/msfweb/app/views/encoders
%dir %{_libdir}/metasploit3/data/msfweb/app/views/payloads
%dir %{_libdir}/metasploit3/data/msfweb/app/views/sessions
%dir %{_libdir}/metasploit3/data/msfweb/app/views/auxiliaries
%dir %{_libdir}/metasploit3/data/msfweb/app/controllers
%dir %{_libdir}/metasploit3/data/msfweb/app/models
%dir %{_libdir}/metasploit3/data/msfweb/app/helpers
%dir %{_libdir}/metasploit3/data/msfweb/doc
%dir %{_libdir}/metasploit3/data/msfweb/lib
%dir %{_libdir}/metasploit3/data/msfweb/lib/tasks
%dir %{_libdir}/metasploit3/data/msfweb/log
%dir %{_libdir}/metasploit3/data/msfweb/tmp
%dir %{_libdir}/metasploit3/data/msfweb/tmp/cache
%dir %{_libdir}/metasploit3/data/msfweb/tmp/sockets
%dir %{_libdir}/metasploit3/data/msfweb/tmp/sessions
%dir %{_libdir}/metasploit3/data/msfweb/components
%dir %{_libdir}/metasploit3/data/msfweb/config
%dir %{_libdir}/metasploit3/data/msfweb/config/environments
%dir %{_libdir}/metasploit3/data/msfweb/public
%dir %{_libdir}/metasploit3/data/msfweb/public/stylesheets
%dir %{_libdir}/metasploit3/data/msfweb/public/stylesheets/window-themes
%dir %{_libdir}/metasploit3/data/msfweb/public/stylesheets/window-themes/default
%dir %{_libdir}/metasploit3/data/msfweb/public/stylesheets/window-themes/metasploit
%dir %{_libdir}/metasploit3/data/msfweb/public/javascripts
%dir %{_libdir}/metasploit3/data/msfweb/public/images
%dir %{_libdir}/metasploit3/data/msfweb/public/images/ide
%dir %{_libdir}/metasploit3/data/msfweb/public/images/platform-icons
%dir %{_libdir}/metasploit3/data/msfweb/script
%dir %{_libdir}/metasploit3/data/msfweb/script/process
%dir %{_libdir}/metasploit3/data/msfweb/script/performance
%dir %{_libdir}/metasploit3/data/msfweb/vendor
%dir %{_libdir}/metasploit3/data/msfweb/vendor/plugins
%dir %{_libdir}/metasploit3/data/meterpreter
%dir %{_libdir}/metasploit3/data/templates
%dir %{_libdir}/metasploit3/external
%dir %{_libdir}/metasploit3/external/ruby-lorcon
%dir %{_libdir}/metasploit3/external/ruby-pcapx
%dir %{_libdir}/metasploit3/external/ruby-pcapx/doc
%dir %{_libdir}/metasploit3/external/ruby-pcapx/lib
%dir %{_libdir}/metasploit3/external/ruby-pcapx/doc-ja
%dir %{_libdir}/metasploit3/external/ruby-pcapx/examples
%dir %{_libdir}/metasploit3/external/source
%dir %{_libdir}/metasploit3/external/source/passivex
%dir %{_libdir}/metasploit3/external/source/vncdll
%dir %{_libdir}/metasploit3/external/source/vncdll/rdr
%dir %{_libdir}/metasploit3/external/source/vncdll/rfb
%dir %{_libdir}/metasploit3/external/source/vncdll/zlib
%dir %{_libdir}/metasploit3/external/source/vncdll/Xregion
%dir %{_libdir}/metasploit3/external/source/vncdll/winvnc
%dir %{_libdir}/metasploit3/external/source/vncdll/winvnc/vnchooks
%dir %{_libdir}/metasploit3/external/source/vncdll/winvnc/vncdll
%dir %{_libdir}/metasploit3/external/source/vncdll/winvnc/winvnc
%dir %{_libdir}/metasploit3/external/source/vncdll/winvnc/winvnc/res
%dir %{_libdir}/metasploit3/external/source/vncdll/winvnc/omnithread
%dir %{_libdir}/metasploit3/external/source/vncdll/winvnc/omnithread/omnithread
%dir %{_libdir}/metasploit3/external/source/dllinject
%dir %{_libdir}/metasploit3/external/source/meterpreter
%dir %{_libdir}/metasploit3/external/source/meterpreter/workspace
%dir %{_libdir}/metasploit3/external/source/meterpreter/workspace/common
%dir %{_libdir}/metasploit3/external/source/meterpreter/workspace/metcli
%dir %{_libdir}/metasploit3/external/source/meterpreter/workspace/metsrv
%dir %{_libdir}/metasploit3/external/source/meterpreter/workspace/ext_server_stdapi
%dir %{_libdir}/metasploit3/external/source/meterpreter/workspace/ext_server_priv
%dir %{_libdir}/metasploit3/external/source/meterpreter/output
%dir %{_libdir}/metasploit3/external/source/meterpreter/output/client
%dir %{_libdir}/metasploit3/external/source/meterpreter/output/server
%dir %{_libdir}/metasploit3/external/source/meterpreter/output/extensions
%dir %{_libdir}/metasploit3/external/source/meterpreter/source
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/client
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/common
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/common/crypto
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/server
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/priv
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/priv/server
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/boiler
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/boiler/client
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/boiler/server
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/fs
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/ui
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/net
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/net/config
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/net/socket
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys/power
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys/config
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys/eventlog
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys/process
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys/registry
%dir %{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/resource
%dir %{_libdir}/metasploit3/tools
%dir %{_libdir}/metasploit3/tools/memdump
%dir %{_libdir}/metasploit3/scripts
%dir %{_libdir}/metasploit3/scripts/meterpreter
%dir %{_libdir}/metasploit3/modules
%dir %{_libdir}/metasploit3/modules/nops
%dir %{_libdir}/metasploit3/modules/nops/php
%dir %{_libdir}/metasploit3/modules/nops/ppc
%dir %{_libdir}/metasploit3/modules/nops/x86
%dir %{_libdir}/metasploit3/modules/nops/sparc
%dir %{_libdir}/metasploit3/modules/exploits
%dir %{_libdir}/metasploit3/modules/exploits/osx
%dir %{_libdir}/metasploit3/modules/exploits/osx/afp
%dir %{_libdir}/metasploit3/modules/exploits/osx/ftp
%dir %{_libdir}/metasploit3/modules/exploits/osx/samba
%dir %{_libdir}/metasploit3/modules/exploits/osx/arkeia
%dir %{_libdir}/metasploit3/modules/exploits/osx/browser
%dir %{_libdir}/metasploit3/modules/exploits/bsdi
%dir %{_libdir}/metasploit3/modules/exploits/bsdi/softcart
%dir %{_libdir}/metasploit3/modules/exploits/hpux
%dir %{_libdir}/metasploit3/modules/exploits/hpux/lpd
%dir %{_libdir}/metasploit3/modules/exploits/irix
%dir %{_libdir}/metasploit3/modules/exploits/irix/lpd
%dir %{_libdir}/metasploit3/modules/exploits/test
%dir %{_libdir}/metasploit3/modules/exploits/unix
%dir %{_libdir}/metasploit3/modules/exploits/unix/http
%dir %{_libdir}/metasploit3/modules/exploits/unix/misc
%dir %{_libdir}/metasploit3/modules/exploits/unix/webapp
%dir %{_libdir}/metasploit3/modules/exploits/linux
%dir %{_libdir}/metasploit3/modules/exploits/linux/ids
%dir %{_libdir}/metasploit3/modules/exploits/linux/http
%dir %{_libdir}/metasploit3/modules/exploits/linux/pptp
%dir %{_libdir}/metasploit3/modules/exploits/linux/games
%dir %{_libdir}/metasploit3/modules/exploits/linux/proxy
%dir %{_libdir}/metasploit3/modules/exploits/multi
%dir %{_libdir}/metasploit3/modules/exploits/multi/ftp
%dir %{_libdir}/metasploit3/modules/exploits/multi/php
%dir %{_libdir}/metasploit3/modules/exploits/multi/svn
%dir %{_libdir}/metasploit3/modules/exploits/multi/samba
%dir %{_libdir}/metasploit3/modules/exploits/multi/realserver
%dir %{_libdir}/metasploit3/modules/exploits/multi/browser
%dir %{_libdir}/metasploit3/modules/exploits/solaris
%dir %{_libdir}/metasploit3/modules/exploits/solaris/lpd
%dir %{_libdir}/metasploit3/modules/exploits/solaris/samba
%dir %{_libdir}/metasploit3/modules/exploits/solaris/dtspcd
%dir %{_libdir}/metasploit3/modules/exploits/solaris/telnet
%dir %{_libdir}/metasploit3/modules/exploits/solaris/sunrpc
%dir %{_libdir}/metasploit3/modules/exploits/windows
%dir %{_libdir}/metasploit3/modules/exploits/windows/ftp
%dir %{_libdir}/metasploit3/modules/exploits/windows/iis
%dir %{_libdir}/metasploit3/modules/exploits/windows/lpd
%dir %{_libdir}/metasploit3/modules/exploits/windows/sip
%dir %{_libdir}/metasploit3/modules/exploits/windows/smb
%dir %{_libdir}/metasploit3/modules/exploits/windows/ssh
%dir %{_libdir}/metasploit3/modules/exploits/windows/ssl
%dir %{_libdir}/metasploit3/modules/exploits/windows/vnc
%dir %{_libdir}/metasploit3/modules/exploits/windows/http
%dir %{_libdir}/metasploit3/modules/exploits/windows/imap
%dir %{_libdir}/metasploit3/modules/exploits/windows/ldap
%dir %{_libdir}/metasploit3/modules/exploits/windows/misc
%dir %{_libdir}/metasploit3/modules/exploits/windows/nntp
%dir %{_libdir}/metasploit3/modules/exploits/windows/pop3
%dir %{_libdir}/metasploit3/modules/exploits/windows/smtp
%dir %{_libdir}/metasploit3/modules/exploits/windows/tftp
%dir %{_libdir}/metasploit3/modules/exploits/windows/wins
%dir %{_libdir}/metasploit3/modules/exploits/windows/games
%dir %{_libdir}/metasploit3/modules/exploits/windows/brightstor
%dir %{_libdir}/metasploit3/modules/exploits/windows/isapi
%dir %{_libdir}/metasploit3/modules/exploits/windows/mssql
%dir %{_libdir}/metasploit3/modules/exploits/windows/proxy
%dir %{_libdir}/metasploit3/modules/exploits/windows/unicenter
%dir %{_libdir}/metasploit3/modules/exploits/windows/license
%dir %{_libdir}/metasploit3/modules/exploits/windows/antivirus
%dir %{_libdir}/metasploit3/modules/exploits/windows/arkeia
%dir %{_libdir}/metasploit3/modules/exploits/windows/firewall
%dir %{_libdir}/metasploit3/modules/exploits/windows/dcerpc
%dir %{_libdir}/metasploit3/modules/exploits/windows/driver
%dir %{_libdir}/metasploit3/modules/exploits/windows/backupexec
%dir %{_libdir}/metasploit3/modules/exploits/windows/novell
%dir %{_libdir}/metasploit3/modules/exploits/windows/browser
%dir %{_libdir}/metasploit3/modules/auxiliary
%dir %{_libdir}/metasploit3/modules/auxiliary/dos
%dir %{_libdir}/metasploit3/modules/auxiliary/dos/solaris
%dir %{_libdir}/metasploit3/modules/auxiliary/dos/solaris/lpd
%dir %{_libdir}/metasploit3/modules/auxiliary/dos/freebsd
%dir %{_libdir}/metasploit3/modules/auxiliary/dos/freebsd/nfsd
%dir %{_libdir}/metasploit3/modules/auxiliary/dos/wireless
%dir %{_libdir}/metasploit3/modules/auxiliary/dos/windows
%dir %{_libdir}/metasploit3/modules/auxiliary/dos/windows/nat
%dir %{_libdir}/metasploit3/modules/auxiliary/dos/windows/smb
%dir %{_libdir}/metasploit3/modules/auxiliary/voip
%dir %{_libdir}/metasploit3/modules/auxiliary/admin
%dir %{_libdir}/metasploit3/modules/auxiliary/admin/backupexec
%dir %{_libdir}/metasploit3/modules/auxiliary/scanner
%dir %{_libdir}/metasploit3/modules/auxiliary/scanner/smb
%dir %{_libdir}/metasploit3/modules/auxiliary/scanner/mssql
%dir %{_libdir}/metasploit3/modules/auxiliary/scanner/discovery
%dir %{_libdir}/metasploit3/modules/encoders
%dir %{_libdir}/metasploit3/modules/encoders/cmd
%dir %{_libdir}/metasploit3/modules/encoders/ppc
%dir %{_libdir}/metasploit3/modules/encoders/x86
%dir %{_libdir}/metasploit3/modules/encoders/sparc
%dir %{_libdir}/metasploit3/modules/encoders/generic
%dir %{_libdir}/metasploit3/modules/payloads
%dir %{_libdir}/metasploit3/modules/payloads/singles
%dir %{_libdir}/metasploit3/modules/payloads/singles/bsd
%dir %{_libdir}/metasploit3/modules/payloads/singles/bsd/x86
%dir %{_libdir}/metasploit3/modules/payloads/singles/bsd/sparc
%dir %{_libdir}/metasploit3/modules/payloads/singles/cmd
%dir %{_libdir}/metasploit3/modules/payloads/singles/cmd/unix
%dir %{_libdir}/metasploit3/modules/payloads/singles/php
%dir %{_libdir}/metasploit3/modules/payloads/singles/osx
%dir %{_libdir}/metasploit3/modules/payloads/singles/osx/ppc
%dir %{_libdir}/metasploit3/modules/payloads/singles/osx/x86
%dir %{_libdir}/metasploit3/modules/payloads/singles/bsdi
%dir %{_libdir}/metasploit3/modules/payloads/singles/bsdi/x86
%dir %{_libdir}/metasploit3/modules/payloads/singles/linux
%dir %{_libdir}/metasploit3/modules/payloads/singles/linux/x86
%dir %{_libdir}/metasploit3/modules/payloads/singles/solaris
%dir %{_libdir}/metasploit3/modules/payloads/singles/solaris/x86
%dir %{_libdir}/metasploit3/modules/payloads/singles/solaris/sparc
%dir %{_libdir}/metasploit3/modules/payloads/singles/generic
%dir %{_libdir}/metasploit3/modules/payloads/singles/windows
%dir %{_libdir}/metasploit3/modules/payloads/stagers
%dir %{_libdir}/metasploit3/modules/payloads/stagers/bsd
%dir %{_libdir}/metasploit3/modules/payloads/stagers/bsd/x86
%dir %{_libdir}/metasploit3/modules/payloads/stagers/osx
%dir %{_libdir}/metasploit3/modules/payloads/stagers/osx/ppc
%dir %{_libdir}/metasploit3/modules/payloads/stagers/bsdi
%dir %{_libdir}/metasploit3/modules/payloads/stagers/bsdi/x86
%dir %{_libdir}/metasploit3/modules/payloads/stagers/linux
%dir %{_libdir}/metasploit3/modules/payloads/stagers/linux/x86
%dir %{_libdir}/metasploit3/modules/payloads/stagers/windows
%dir %{_libdir}/metasploit3/modules/payloads/stages
%dir %{_libdir}/metasploit3/modules/payloads/stages/bsd
%dir %{_libdir}/metasploit3/modules/payloads/stages/bsd/x86
%dir %{_libdir}/metasploit3/modules/payloads/stages/osx
%dir %{_libdir}/metasploit3/modules/payloads/stages/osx/ppc
%dir %{_libdir}/metasploit3/modules/payloads/stages/bsdi
%dir %{_libdir}/metasploit3/modules/payloads/stages/bsdi/x86
%dir %{_libdir}/metasploit3/modules/payloads/stages/linux
%dir %{_libdir}/metasploit3/modules/payloads/stages/linux/x86
%dir %{_libdir}/metasploit3/modules/payloads/stages/windows
%dir %{_libdir}/metasploit3/documentation
%dir %{_libdir}/metasploit3/documentation/samples
%dir %{_libdir}/metasploit3/documentation/samples/framework
%dir %{_libdir}/metasploit3/documentation/samples/modules
%dir %{_libdir}/metasploit3/documentation/samples/modules/nops
%dir %{_libdir}/metasploit3/documentation/samples/modules/exploits
%dir %{_libdir}/metasploit3/documentation/samples/modules/auxiliary
%dir %{_libdir}/metasploit3/documentation/samples/modules/encoders
%dir %{_libdir}/metasploit3/documentation/samples/modules/payloads
%dir %{_libdir}/metasploit3/documentation/samples/modules/payloads/singles
%dir %{_libdir}/metasploit3/documentation/metasploit2
%dir %{_libdir}/metasploit3/plugins

%{_libdir}/metasploit3/lib/*.rb
%{_libdir}/metasploit3/lib/msf/*
%{_libdir}/metasploit3/lib/msf/ui/*
%{_libdir}/metasploit3/lib/msf/ui/web/*
%{_libdir}/metasploit3/lib/msf/ui/gtk2/*
%{_libdir}/metasploit3/lib/msf/ui/console/*
%{_libdir}/metasploit3/lib/msf/ui/console/command_dispatcher/*
%{_libdir}/metasploit3/lib/msf/base/*
%{_libdir}/metasploit3/lib/msf/base/persistent_storage/*
%{_libdir}/metasploit3/lib/msf/base/serializer/*
%{_libdir}/metasploit3/lib/msf/base/simple/*
%{_libdir}/metasploit3/lib/msf/base/sessions/*
%{_libdir}/metasploit3/lib/msf/core/*
%{_libdir}/metasploit3/lib/msf/core/session/*
%{_libdir}/metasploit3/lib/msf/core/session/provider/*
%{_libdir}/metasploit3/lib/msf/core/auxiliary/*
%{_libdir}/metasploit3/lib/msf/core/encoder/*
%{_libdir}/metasploit3/lib/msf/core/encoding/*
%{_libdir}/metasploit3/lib/msf/core/exploit/*
%{_libdir}/metasploit3/lib/msf/core/handler/*
%{_libdir}/metasploit3/lib/msf/core/module/*
%{_libdir}/metasploit3/lib/msf/core/payload/*
%{_libdir}/metasploit3/lib/msf/core/payload/windows/*
%{_libdir}/metasploit3/lib/ole/*
%{_libdir}/metasploit3/lib/rex/*
%{_libdir}/metasploit3/lib/rex/io/*
%{_libdir}/metasploit3/lib/rex/ui/*
%{_libdir}/metasploit3/lib/rex/ui/text/*
%{_libdir}/metasploit3/lib/rex/ui/text/input/*
%{_libdir}/metasploit3/lib/rex/ui/text/output/*
%{_libdir}/metasploit3/lib/rex/ui/output/*
%{_libdir}/metasploit3/lib/rex/nop/*
%{_libdir}/metasploit3/lib/rex/arch/*
%{_libdir}/metasploit3/lib/rex/poly/*
%{_libdir}/metasploit3/lib/rex/poly/register/*
%{_libdir}/metasploit3/lib/rex/post/*
%{_libdir}/metasploit3/lib/rex/post/dispatch_ninja/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/ui/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/ui/console/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/ui/console/command_dispatcher/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/ui/console/command_dispatcher/priv/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/ui/console/command_dispatcher/stdapi/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/channels/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/channels/pools/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/priv/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/fs/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/net/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/net/socket_subsystem/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/sys/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/sys/registry_subsystem/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/sys/event_log_subsystem/*
%{_libdir}/metasploit3/lib/rex/post/meterpreter/extensions/stdapi/sys/process_subsystem/*
%{_libdir}/metasploit3/lib/rex/sync/*
%{_libdir}/metasploit3/lib/rex/proto/*
%{_libdir}/metasploit3/lib/rex/proto/smb/*
%{_libdir}/metasploit3/lib/rex/proto/http/*
%{_libdir}/metasploit3/lib/rex/proto/http/handler/*
%{_libdir}/metasploit3/lib/rex/proto/dcerpc/*
%{_libdir}/metasploit3/lib/rex/proto/sunrpc/*
%{_libdir}/metasploit3/lib/rex/platforms/*
%{_libdir}/metasploit3/lib/rex/encoder/*
%{_libdir}/metasploit3/lib/rex/encoder/xor/*
%{_libdir}/metasploit3/lib/rex/encoder/alpha2/*
%{_libdir}/metasploit3/lib/rex/logging/*
%{_libdir}/metasploit3/lib/rex/logging/sinks/*
%{_libdir}/metasploit3/lib/rex/encoders/*
%{_libdir}/metasploit3/lib/rex/encoding/*
%{_libdir}/metasploit3/lib/rex/encoding/xor/*
%{_libdir}/metasploit3/lib/rex/struct2/*
%{_libdir}/metasploit3/lib/rex/payloads/*
%{_libdir}/metasploit3/lib/rex/payloads/win32/*
%{_libdir}/metasploit3/lib/rex/payloads/win32/kernel/*
%{_libdir}/metasploit3/lib/rex/parser/*
%{_libdir}/metasploit3/lib/rex/pescan/*
%{_libdir}/metasploit3/lib/rex/socket/*
%{_libdir}/metasploit3/lib/rex/socket/comm/*
%{_libdir}/metasploit3/lib/rex/services/*
%{_libdir}/metasploit3/lib/rex/exploitation/*
%{_libdir}/metasploit3/lib/rex/peparsey/*
%{_libdir}/metasploit3/lib/rex/peparsey/image_source/*
%{_libdir}/metasploit3/lib/rex/assembly/*
%{_libdir}/metasploit3/data/*
%{_libdir}/metasploit3/data/sql/*
%{_libdir}/metasploit3/data/exploits/*
%{_libdir}/metasploit3/data/msfpescan/*
%{_libdir}/metasploit3/data/passivex/*
%{_libdir}/metasploit3/data/msfgui/*
%{_libdir}/metasploit3/data/msfgui/pix/*
%{_libdir}/metasploit3/data/msfgui/style/*
%{_libdir}/metasploit3/data/msfweb/*
%{_libdir}/metasploit3/data/msfweb/app/*
%{_libdir}/metasploit3/data/msfweb/app/views/*
%{_libdir}/metasploit3/data/msfweb/app/views/ide/*
%{_libdir}/metasploit3/data/msfweb/app/views/msf/*
%{_libdir}/metasploit3/data/msfweb/app/views/jobs/*
%{_libdir}/metasploit3/data/msfweb/app/views/nops/*
%{_libdir}/metasploit3/data/msfweb/app/views/exploits/*
%{_libdir}/metasploit3/data/msfweb/app/views/console/*
%{_libdir}/metasploit3/data/msfweb/app/views/layouts/*
%{_libdir}/metasploit3/data/msfweb/app/views/encoders/*
%{_libdir}/metasploit3/data/msfweb/app/views/payloads/*
%{_libdir}/metasploit3/data/msfweb/app/views/sessions/*
%{_libdir}/metasploit3/data/msfweb/app/views/auxiliaries/*
%{_libdir}/metasploit3/data/msfweb/app/controllers/*
%{_libdir}/metasploit3/data/msfweb/app/models/*
%{_libdir}/metasploit3/data/msfweb/app/helpers/*
%{_libdir}/metasploit3/data/msfweb/doc/*
%{_libdir}/metasploit3/data/msfweb/lib/*
%{_libdir}/metasploit3/data/msfweb/tmp/*
%{_libdir}/metasploit3/data/msfweb/config/*
%{_libdir}/metasploit3/data/msfweb/config/environments/*
%{_libdir}/metasploit3/data/msfweb/public/*
%{_libdir}/metasploit3/data/msfweb/public/stylesheets/*
%{_libdir}/metasploit3/data/msfweb/public/stylesheets/window-themes/*
%{_libdir}/metasploit3/data/msfweb/public/stylesheets/window-themes/default/*
%{_libdir}/metasploit3/data/msfweb/public/stylesheets/window-themes/metasploit/*
%{_libdir}/metasploit3/data/msfweb/public/javascripts/*
%{_libdir}/metasploit3/data/msfweb/public/images/*
%{_libdir}/metasploit3/data/msfweb/public/images/ide/*
%{_libdir}/metasploit3/data/msfweb/public/images/platform-icons/*
%{_libdir}/metasploit3/data/msfweb/script/*
%{_libdir}/metasploit3/data/msfweb/script/process/*
%{_libdir}/metasploit3/data/msfweb/script/performance/*
%{_libdir}/metasploit3/data/msfweb/vendor/*
%{_libdir}/metasploit3/data/meterpreter/*
%{_libdir}/metasploit3/data/templates/*
%{_libdir}/metasploit3/external/*
%{_libdir}/metasploit3/external/ruby-lorcon/*
%{_libdir}/metasploit3/external/ruby-pcapx/*
%{_libdir}/metasploit3/external/ruby-pcapx/doc/*
%{_libdir}/metasploit3/external/ruby-pcapx/lib/*
%{_libdir}/metasploit3/external/ruby-pcapx/doc-ja/*
%{_libdir}/metasploit3/external/ruby-pcapx/examples/*
%{_libdir}/metasploit3/external/source/*
%{_libdir}/metasploit3/external/source/passivex/*
%{_libdir}/metasploit3/external/source/vncdll/*
%{_libdir}/metasploit3/external/source/vncdll/rdr/*
%{_libdir}/metasploit3/external/source/vncdll/rfb/*
%{_libdir}/metasploit3/external/source/vncdll/zlib/*
%{_libdir}/metasploit3/external/source/vncdll/Xregion/*
%{_libdir}/metasploit3/external/source/vncdll/winvnc/*
%{_libdir}/metasploit3/external/source/vncdll/winvnc/vnchooks/*
%{_libdir}/metasploit3/external/source/vncdll/winvnc/vncdll/*
%{_libdir}/metasploit3/external/source/vncdll/winvnc/winvnc/*
%{_libdir}/metasploit3/external/source/vncdll/winvnc/winvnc/res/*
%{_libdir}/metasploit3/external/source/vncdll/winvnc/omnithread/*
%{_libdir}/metasploit3/external/source/vncdll/winvnc/omnithread/omnithread/*
%{_libdir}/metasploit3/external/source/dllinject/*
%{_libdir}/metasploit3/external/source/meterpreter/*
%{_libdir}/metasploit3/external/source/meterpreter/workspace/*
%{_libdir}/metasploit3/external/source/meterpreter/workspace/common/*
%{_libdir}/metasploit3/external/source/meterpreter/workspace/metcli/*
%{_libdir}/metasploit3/external/source/meterpreter/workspace/metsrv/*
%{_libdir}/metasploit3/external/source/meterpreter/workspace/ext_server_stdapi/*
%{_libdir}/metasploit3/external/source/meterpreter/workspace/ext_server_priv/*
%{_libdir}/metasploit3/external/source/meterpreter/output/*
%{_libdir}/metasploit3/external/source/meterpreter/output/client/*
%{_libdir}/metasploit3/external/source/meterpreter/output/server/*
%{_libdir}/metasploit3/external/source/meterpreter/output/extensions/*
%{_libdir}/metasploit3/external/source/meterpreter/source/*
%{_libdir}/metasploit3/external/source/meterpreter/source/client/*
%{_libdir}/metasploit3/external/source/meterpreter/source/common/*
%{_libdir}/metasploit3/external/source/meterpreter/source/common/crypto/*
%{_libdir}/metasploit3/external/source/meterpreter/source/server/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/priv/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/priv/server/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/boiler/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/boiler/client/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/boiler/server/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/fs/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/ui/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/net/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/net/config/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/net/socket/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys/power/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys/config/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys/eventlog/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys/process/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/sys/registry/*
%{_libdir}/metasploit3/external/source/meterpreter/source/extensions/stdapi/server/resource/*
%{_libdir}/metasploit3/tools/*
%{_libdir}/metasploit3/tools/memdump/*
%{_libdir}/metasploit3/scripts/*
%{_libdir}/metasploit3/scripts/meterpreter/*
%{_libdir}/metasploit3/modules/*
%{_libdir}/metasploit3/modules/nops/*
%{_libdir}/metasploit3/modules/nops/php/*
%{_libdir}/metasploit3/modules/nops/ppc/*
%{_libdir}/metasploit3/modules/nops/x86/*
%{_libdir}/metasploit3/modules/nops/sparc/*
%{_libdir}/metasploit3/modules/exploits/*
%{_libdir}/metasploit3/modules/exploits/osx/*
%{_libdir}/metasploit3/modules/exploits/osx/afp/*
%{_libdir}/metasploit3/modules/exploits/osx/ftp/*
%{_libdir}/metasploit3/modules/exploits/osx/samba/*
%{_libdir}/metasploit3/modules/exploits/osx/arkeia/*
%{_libdir}/metasploit3/modules/exploits/osx/browser/*
%{_libdir}/metasploit3/modules/exploits/bsdi/*
%{_libdir}/metasploit3/modules/exploits/bsdi/softcart/*
%{_libdir}/metasploit3/modules/exploits/hpux/*
%{_libdir}/metasploit3/modules/exploits/hpux/lpd/*
%{_libdir}/metasploit3/modules/exploits/irix/*
%{_libdir}/metasploit3/modules/exploits/irix/lpd/*
%{_libdir}/metasploit3/modules/exploits/test/*
%{_libdir}/metasploit3/modules/exploits/unix/*
%{_libdir}/metasploit3/modules/exploits/unix/misc/*
%{_libdir}/metasploit3/modules/exploits/unix/webapp/*
%{_libdir}/metasploit3/modules/exploits/linux/*
%{_libdir}/metasploit3/modules/exploits/linux/ids/*
%{_libdir}/metasploit3/modules/exploits/linux/http/*
%{_libdir}/metasploit3/modules/exploits/linux/pptp/*
%{_libdir}/metasploit3/modules/exploits/linux/games/*
%{_libdir}/metasploit3/modules/exploits/linux/proxy/*
%{_libdir}/metasploit3/modules/exploits/multi/*
%{_libdir}/metasploit3/modules/exploits/multi/ftp/*
%{_libdir}/metasploit3/modules/exploits/multi/php/*
%{_libdir}/metasploit3/modules/exploits/multi/svn/*
%{_libdir}/metasploit3/modules/exploits/multi/realserver/*
%{_libdir}/metasploit3/modules/exploits/multi/browser/*
%{_libdir}/metasploit3/modules/exploits/solaris/*
%{_libdir}/metasploit3/modules/exploits/solaris/lpd/*
%{_libdir}/metasploit3/modules/exploits/solaris/samba/*
%{_libdir}/metasploit3/modules/exploits/solaris/dtspcd/*
%{_libdir}/metasploit3/modules/exploits/solaris/telnet/*
%{_libdir}/metasploit3/modules/exploits/solaris/sunrpc/*
%{_libdir}/metasploit3/modules/exploits/windows/*
%{_libdir}/metasploit3/modules/exploits/windows/ftp/*
%{_libdir}/metasploit3/modules/exploits/windows/iis/*
%{_libdir}/metasploit3/modules/exploits/windows/lpd/*
%{_libdir}/metasploit3/modules/exploits/windows/sip/*
%{_libdir}/metasploit3/modules/exploits/windows/smb/*
%{_libdir}/metasploit3/modules/exploits/windows/ssh/*
%{_libdir}/metasploit3/modules/exploits/windows/ssl/*
%{_libdir}/metasploit3/modules/exploits/windows/vnc/*
%{_libdir}/metasploit3/modules/exploits/windows/http/*
%{_libdir}/metasploit3/modules/exploits/windows/imap/*
%{_libdir}/metasploit3/modules/exploits/windows/ldap/*
%{_libdir}/metasploit3/modules/exploits/windows/misc/*
%{_libdir}/metasploit3/modules/exploits/windows/nntp/*
%{_libdir}/metasploit3/modules/exploits/windows/pop3/*
%{_libdir}/metasploit3/modules/exploits/windows/smtp/*
%{_libdir}/metasploit3/modules/exploits/windows/tftp/*
%{_libdir}/metasploit3/modules/exploits/windows/wins/*
%{_libdir}/metasploit3/modules/exploits/windows/games/*
%{_libdir}/metasploit3/modules/exploits/windows/brightstor/*
%{_libdir}/metasploit3/modules/exploits/windows/isapi/*
%{_libdir}/metasploit3/modules/exploits/windows/mssql/*
%{_libdir}/metasploit3/modules/exploits/windows/proxy/*
%{_libdir}/metasploit3/modules/exploits/windows/unicenter/*
%{_libdir}/metasploit3/modules/exploits/windows/license/*
%{_libdir}/metasploit3/modules/exploits/windows/antivirus/*
%{_libdir}/metasploit3/modules/exploits/windows/arkeia/*
%{_libdir}/metasploit3/modules/exploits/windows/firewall/*
%{_libdir}/metasploit3/modules/exploits/windows/dcerpc/*
%{_libdir}/metasploit3/modules/exploits/windows/driver/*
%{_libdir}/metasploit3/modules/exploits/windows/backupexec/*
%{_libdir}/metasploit3/modules/exploits/windows/novell/*
%{_libdir}/metasploit3/modules/exploits/windows/browser/*
%{_libdir}/metasploit3/modules/auxiliary/*
%{_libdir}/metasploit3/modules/auxiliary/dos/*
%{_libdir}/metasploit3/modules/auxiliary/dos/solaris/*
%{_libdir}/metasploit3/modules/auxiliary/dos/solaris/lpd/*
%{_libdir}/metasploit3/modules/auxiliary/dos/freebsd/*
%{_libdir}/metasploit3/modules/auxiliary/dos/freebsd/nfsd/*
%{_libdir}/metasploit3/modules/auxiliary/dos/wireless/*
%{_libdir}/metasploit3/modules/auxiliary/dos/windows/*
%{_libdir}/metasploit3/modules/auxiliary/dos/windows/nat/*
%{_libdir}/metasploit3/modules/auxiliary/dos/windows/smb/*
%{_libdir}/metasploit3/modules/auxiliary/voip/*
%{_libdir}/metasploit3/modules/auxiliary/admin/*
%{_libdir}/metasploit3/modules/auxiliary/admin/backupexec/*
%{_libdir}/metasploit3/modules/auxiliary/scanner/*
%{_libdir}/metasploit3/modules/auxiliary/scanner/smb/*
%{_libdir}/metasploit3/modules/auxiliary/scanner/mssql/*
%{_libdir}/metasploit3/modules/auxiliary/scanner/discovery/*
%{_libdir}/metasploit3/modules/encoders/*
%{_libdir}/metasploit3/modules/encoders/cmd/*
%{_libdir}/metasploit3/modules/encoders/ppc/*
%{_libdir}/metasploit3/modules/encoders/x86/*
%{_libdir}/metasploit3/modules/encoders/sparc/*
%{_libdir}/metasploit3/modules/encoders/generic/*
%{_libdir}/metasploit3/modules/payloads/*
%{_libdir}/metasploit3/modules/payloads/singles/*
%{_libdir}/metasploit3/modules/payloads/singles/bsd/*
%{_libdir}/metasploit3/modules/payloads/singles/bsd/x86/*
%{_libdir}/metasploit3/modules/payloads/singles/bsd/sparc/*
%{_libdir}/metasploit3/modules/payloads/singles/cmd/*
%{_libdir}/metasploit3/modules/payloads/singles/cmd/unix/*
%{_libdir}/metasploit3/modules/payloads/singles/php/*
%{_libdir}/metasploit3/modules/payloads/singles/osx/*
%{_libdir}/metasploit3/modules/payloads/singles/osx/ppc/*
%{_libdir}/metasploit3/modules/payloads/singles/osx/x86/*
%{_libdir}/metasploit3/modules/payloads/singles/bsdi/*
%{_libdir}/metasploit3/modules/payloads/singles/bsdi/x86/*
%{_libdir}/metasploit3/modules/payloads/singles/linux/*
%{_libdir}/metasploit3/modules/payloads/singles/linux/x86/*
%{_libdir}/metasploit3/modules/payloads/singles/solaris/*
%{_libdir}/metasploit3/modules/payloads/singles/solaris/x86/*
%{_libdir}/metasploit3/modules/payloads/singles/solaris/sparc/*
%{_libdir}/metasploit3/modules/payloads/singles/generic/*
%{_libdir}/metasploit3/modules/payloads/singles/windows/*
%{_libdir}/metasploit3/modules/payloads/stagers/*
%{_libdir}/metasploit3/modules/payloads/stagers/bsd/*
%{_libdir}/metasploit3/modules/payloads/stagers/bsd/x86/*
%{_libdir}/metasploit3/modules/payloads/stagers/osx/*
%{_libdir}/metasploit3/modules/payloads/stagers/osx/ppc/*
%{_libdir}/metasploit3/modules/payloads/stagers/bsdi/*
%{_libdir}/metasploit3/modules/payloads/stagers/bsdi/x86/*
%{_libdir}/metasploit3/modules/payloads/stagers/linux/*
%{_libdir}/metasploit3/modules/payloads/stagers/linux/x86/*
%{_libdir}/metasploit3/modules/payloads/stagers/windows/*
%{_libdir}/metasploit3/modules/payloads/stages/*
%{_libdir}/metasploit3/modules/payloads/stages/bsd/*
%{_libdir}/metasploit3/modules/payloads/stages/bsd/x86/*
%{_libdir}/metasploit3/modules/payloads/stages/osx/*
%{_libdir}/metasploit3/modules/payloads/stages/osx/ppc/*
%{_libdir}/metasploit3/modules/payloads/stages/bsdi/*
%{_libdir}/metasploit3/modules/payloads/stages/bsdi/x86/*
%{_libdir}/metasploit3/modules/payloads/stages/linux/*
%{_libdir}/metasploit3/modules/payloads/stages/linux/x86/*
%{_libdir}/metasploit3/modules/payloads/stages/windows/*
%{_libdir}/metasploit3/documentation/*
%{_libdir}/metasploit3/documentation/samples/*
%{_libdir}/metasploit3/documentation/samples/framework/*
%{_libdir}/metasploit3/documentation/samples/modules/*
%{_libdir}/metasploit3/documentation/samples/modules/nops/*
%{_libdir}/metasploit3/documentation/samples/modules/exploits/*
%{_libdir}/metasploit3/documentation/samples/modules/auxiliary/*
%{_libdir}/metasploit3/documentation/samples/modules/encoders/*
%{_libdir}/metasploit3/documentation/samples/modules/payloads/*
%{_libdir}/metasploit3/documentation/samples/modules/payloads/singles/*
%{_libdir}/metasploit3/documentation/metasploit2/*
%{_libdir}/metasploit3/plugins/*
