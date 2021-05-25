#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sereal-Encoder
Version  : 4.018
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/Y/YV/YVES/Sereal-Encoder-4.018.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Y/YV/YVES/Sereal-Encoder-4.018.tar.gz
Summary  : 'Fast, compact, powerful binary serialization'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Sereal-Encoder-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sereal::Decoder)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Differences)
BuildRequires : perl(Test::LongString)
BuildRequires : perl(Test::Warn)
BuildRequires : pkgconfig(libzstd)

%description
No detailed description available

%package dev
Summary: dev components for the perl-Sereal-Encoder package.
Group: Development
Provides: perl-Sereal-Encoder-devel = %{version}-%{release}
Requires: perl-Sereal-Encoder = %{version}-%{release}

%description dev
dev components for the perl-Sereal-Encoder package.


%package perl
Summary: perl components for the perl-Sereal-Encoder package.
Group: Default
Requires: perl-Sereal-Encoder = %{version}-%{release}

%description perl
perl components for the perl-Sereal-Encoder package.


%prep
%setup -q -n Sereal-Encoder-4.018
cd %{_builddir}/Sereal-Encoder-4.018

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
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
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
/usr/share/man/man3/Sereal::Encoder.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Sereal/Encoder.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Sereal/Encoder/Constants.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Sereal/Encoder/Encoder.so
