#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Pegex
Version  : 0.75
Release  : 32
URL      : https://cpan.metacpan.org/authors/id/I/IN/INGY/Pegex-0.75.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IN/INGY/Pegex-0.75.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpegex-perl/libpegex-perl_0.75-1.debian.tar.xz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
tar xf %{_sourcedir}/libpegex-perl_0.75-1.debian.tar.xz
cd %{_builddir}/Pegex-0.75
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Pegex-0.75/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
cp %{_builddir}/Pegex-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Pegex/19d40da3bc981cec880a2112a7e2646d480cb6f4 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Pegex/7d9b99810f4848e0c25be6c12671cdeb96394b0c || :
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
/usr/share/package-licenses/perl-Pegex/7d9b99810f4848e0c25be6c12671cdeb96394b0c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
