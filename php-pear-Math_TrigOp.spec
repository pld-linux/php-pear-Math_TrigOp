%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	TrigOp
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Supplementary trigonometric functions
Summary(pl):	%{_class}_%{_subclass} - uzupe³niaj±ce funkcje trygonometryczne
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	98262560108abc7fea62bd7491d65984
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Static class with methods that implement supplementary trigonometric,
inverse trigonometric, hyperbolic, and inverse hyperbolic functions.

This class has in PEAR status: %{_status}.

%description -l pl
Statyczna klasa z metodami bêd±cymi implementacj± funkcji
trygonometrycznych uzupe³niaj±cych, odwrotnych, hiperbolicznych oraz
odwrotnych hiperbolicznych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
