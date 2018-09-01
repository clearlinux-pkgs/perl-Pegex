#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Pegex
Version  : 0.66
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/I/IN/INGY/Pegex-0.66.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IN/INGY/Pegex-0.66.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpegex-perl/libpegex-perl_0.64-1.debian.tar.xz
Summary  : 'Acmeist PEG Parser Framework'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Pegex-license
BuildRequires : buildreq-cpan
BuildRequires : perl(File::ShareDir::Install)
BuildRequires : perl(YAML::XS)

%description
NAME
Pegex - Acmeist PEG Parser Framework
VERSION
This document describes Pegex version 0.66.

%package dev
Summary: dev components for the perl-Pegex package.
Group: Development
Provides: perl-Pegex-devel

%description dev
dev components for the perl-Pegex package.


%package license
Summary: license components for the perl-Pegex package.
Group: Default

%description license
license components for the perl-Pegex package.


%prep
%setup -q -n Pegex-0.66
cd ..
%setup -q -T -D -n Pegex-0.66 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Pegex-0.66/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Pegex
cp LICENSE %{buildroot}/usr/share/doc/perl-Pegex/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Pegex.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/API.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Base.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Bootstrap.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Bootstrap.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Compiler.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Compiler.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Grammar.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Grammar.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Grammar/Atoms.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Grammar/Atoms.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Input.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Input.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Miscellany.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Module.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Module.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Optimizer.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Overview.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Parser.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Parser.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Parser/Indent.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Pegex/AST.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Pegex/Grammar.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Pegex/Grammar.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Receiver.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Receiver.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Regex.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Regex.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Resources.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Syntax.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Tree.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Tree.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Tree/Wrap.pm
/usr/lib/perl5/site_perl/5.26.1/Pegex/Tree/Wrap.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Tutorial.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Tutorial/Calculator.pod
/usr/lib/perl5/site_perl/5.26.1/Pegex/Tutorial/JSON.pod
/usr/lib/perl5/site_perl/5.26.1/auto/share/dist/Pegex/pegex.pgx

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
%defattr(-,root,root,-)
/usr/share/doc/perl-Pegex/LICENSE
