%define upstream_name       WWW-Google-Images
%define upstream_version    0.6.5

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1
Summary:        Google Images Agent
License:        GPL or Artistic
Group:          Development/Perl
Url:            https://search.cpan.org/dist/%{upstream_name}
Source:         http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:         WWW-Google-Images-0.6.5-fix-tests.patch
Patch1:         WWW-Google-Images-0.6.5-fix-mechanize-error-handling.patch
Buildrequires:  perl(Test::URI)
Buildrequires:  perl(WWW::Mechanize)
Buildrequires:  perl(Image::Info)
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module may be used search images on Google. Its interface is heavily
inspired from WWW::Google::Groups.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
%patch0 -p 1
%patch1 -p 1

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

