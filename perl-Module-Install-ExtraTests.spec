%define upstream_name    Module-Install-ExtraTests
%define upstream_version 0.008
Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	4

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://git.codesimply.com/Module-Install-ExtraTests
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Module-Install-ExtraTests-0.008.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
%{upstream_name} perl module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.7.0-2mdv2011.0
+ Revision: 657792
- rebuild for updated spec-helper

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 607097
- import perl-Module-Install-ExtraTests


