Name:		perl-CPAN-Changes
Summary:	Read and write Changes files
Version:	0.20
Release:	2%{?dist}
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/CPAN-Changes/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BR/BRICAS/CPAN-Changes-%{version}.tar.gz 
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
BuildArch:	noarch
BuildRequires:	perl >= 4:5.10.0
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
BuildRequires:	perl(Text::Wrap)
BuildRequires:	perl(version) >= 0.79

%description
It is standard practice to include a Changes file in your distribution. The
purpose of the Changes file is to help a user figure out what has changed
since the last release.

People have devised many ways to write the Changes file. A preliminary
specification has been created (CPAN::Changes::Spec) to encourage module
authors to write clear and concise Changes.

This module will help users programmatically read and write Changes files
that conform to the specification.

%prep
%setup -q -n CPAN-Changes-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
make test
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"

%files
%doc Changes README
%{_bindir}/tidy_changelog
%{perl_vendorlib}/CPAN/
%{perl_vendorlib}/Test/
%{_mandir}/man1/tidy_changelog.1*
%{_mandir}/man3/CPAN::Changes.3pm*
%{_mandir}/man3/CPAN::Changes::Release.3pm*
%{_mandir}/man3/CPAN::Changes::Spec.3pm*
%{_mandir}/man3/Test::CPAN::Changes.3pm*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20-2
- Mass rebuild 2013-12-27

* Thu May  2 2013 Paul Howarth <paul@city-fan.org> - 0.20-1
- Update to 0.20:
  - 'delete_empty_groups' shouldn't erronously delete default group
  - Add tidy_changelog utility script
  - Minor pod fix
- Bump Test::More version requirement to 0.96 (CPAN RT#84994)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-4
- Update dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.19-2
- Perl 5.16 rebuild

* Tue May  1 2012 Paul Howarth <paul@city-fan.org> - 0.19-1
- Update to 0.19:
  - Test::CPAN::Changes now accepts version entries ending in '-TRIAL'
    (CPAN RT#76882)
  - releases() in CPAN::Changes also accepts entries ending in '-TRIAL'
- Don't need to remove empty directories from buildroot
- Drop %%defattr, redundant since rpm 4.4

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> - 0.18-2
- Fedora 17 mass rebuild

* Tue Oct 18 2011 Paul Howarth <paul@city-fan.org> - 0.18-1
- Update to 0.18:
  - Expand changes_file_ok() to accept arguments so that a specific version may
    be checked
  - Add $VERSION to Test::CPAN::Changes so it plays nice with the toolchain
    e.g. Module::Install::AuthorRequires

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.17-2
- Perl mass rebuild

* Thu Apr 21 2011 Paul Howarth <paul@city-fan.org> - 0.17-1
- Update to 0.17:
  - Eliminate extra whitespace when release data is not defined (CPAN RT#67441)
  - Require version.pm 0.79, which introduced the $LAX regexp (CPAN RT#67613)
  - Add the option to sort groups

* Wed Apr 20 2011 Paul Howarth <paul@city-fan.org> - 0.16-1
- Initial RPM version
