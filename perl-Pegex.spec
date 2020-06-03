#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Pegex
Version  : 0.75
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/I/IN/INGY/Pegex-0.75.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IN/INGY/Pegex-0.75.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpegex-perl/libpegex-perl_0.67-2.debian.tar.xz
Summary  : 'Acmeist PEG Parser Framework'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Pegex-license = %{version}-%{release}
Requires: perl-Pegex-perl = %{version}-%{release}
Requires: perl(JSON::PP)
Requires: perl(YAML::PP)
BuildRequires : buildreq-cpan
BuildRequires : perl(File::ShareDir::Install)
BuildRequires : perl(Test::Pod)
BuildRequires : perl(Tie::IxHash)
BuildRequires : perl(YAML::PP)

%description
NAME
Pegex - Acmeist PEG Parser Framework
VERSION
This document describes Pegex version 0.75.

%package dev
Summary: dev components for the perl-Pegex package.
Group: Development
Provides: perl-Pegex-devel = %{version}-%{release}
Requires: perl-Pegex = %{version}-%{release}

%description dev
dev components for the perl-Pegex package.


%package license
Summary: license components for the perl-Pegex package.
Group: Default

%description license
license components for the perl-Pegex package.


%package perl
Summary: perl components for the perl-Pegex package.
Group: Default
Requires: perl-Pegex = %{version}-%{release}

%description perl
perl components for the perl-Pegex package.


%prep
%setup -q -n Pegex-0.75
cd %{_builddir}
tar xf %{_sourcedir}/libpegex-perl_0.67-2.debian.tar.xz
cd %{_builddir}/Pegex-0.75
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Pegex-0.75/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Pegex
cp %{_builddir}/Pegex-0.75/LICENSE %{buildroot}/usr/share/package-licenses/perl-Pegex/19d40da3bc981cec880a2112a7e2646d480cb6f4
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Pegex.3
/usr/share/man/man3/Pegex::API.3
/usr/share/man/man3/Pegex::Bootstrap.3
/usr/share/man/man3/Pegex::Compiler.3
/usr/share/man/man3/Pegex::Grammar.3
/usr/share/man/man3/Pegex::Grammar::Atoms.3
/usr/share/man/man3/Pegex::Input.3
/usr/share/man/man3/Pegex::Miscellany.3
/usr/share/man/man3/Pegex::Module.3
/usr/share/man/man3/Pegex::Overview.3
/usr/share/man/man3/Pegex::Parser.3
/usr/share/man/man3/Pegex::Pegex::Grammar.3
/usr/share/man/man3/Pegex::Receiver.3
/usr/share/man/man3/Pegex::Regex.3
/usr/share/man/man3/Pegex::Resources.3
/usr/share/man/man3/Pegex::Syntax.3
/usr/share/man/man3/Pegex::Tree.3
/usr/share/man/man3/Pegex::Tree::Wrap.3
/usr/share/man/man3/Pegex::Tutorial.3
/usr/share/man/man3/Pegex::Tutorial::Calculator.3
/usr/share/man/man3/Pegex::Tutorial::JSON.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Pegex/19d40da3bc981cec880a2112a7e2646d480cb6f4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Pegex.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/API.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Base.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Bootstrap.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Bootstrap.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Compiler.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Compiler.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Grammar.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Grammar.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Grammar/Atoms.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Grammar/Atoms.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Input.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Input.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Miscellany.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Module.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Module.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Optimizer.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Overview.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Parser.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Parser.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Parser/Indent.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Pegex/AST.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Pegex/Grammar.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Pegex/Grammar.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Receiver.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Receiver.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Regex.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Regex.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Resources.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Syntax.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Tree.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Tree.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Tree/Wrap.pm
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Tree/Wrap.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Tutorial.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Tutorial/Calculator.pod
/usr/lib/perl5/vendor_perl/5.30.3/Pegex/Tutorial/JSON.pod
/usr/lib/perl5/vendor_perl/5.30.3/auto/share/dist/Pegex/pegex.pgx
