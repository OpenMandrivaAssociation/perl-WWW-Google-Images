%define module  WWW-Google-Images
%define name    perl-%{module}
%define version 0.6.5
%define release %mkrel 4

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Google Images Agent
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/WWW/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildrequires:  perl(Test::URI)
Buildrequires:  perl(WWW::Mechanize)
Buildrequires:  perl(Image::Info)
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module may be used search images on Google. Its interface is heavily
inspired from WWW::Google::Groups.

%prep
%setup -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/WWW
%{_mandir}/*/*
%{_bindir}/*

