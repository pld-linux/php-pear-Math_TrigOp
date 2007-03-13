%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	TrigOp
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Supplementary trigonometric functions
Summary(pl.UTF-8):	%{_class}_%{_subclass} - uzupełniające funkcje trygonometryczne
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	98262560108abc7fea62bd7491d65984
URL:		http://pear.php.net/package/Math_TrigOp/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Static class with methods that implement supplementary trigonometric,
inverse trigonometric, hyperbolic, and inverse hyperbolic functions.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Statyczna klasa z metodami będącymi implementacją funkcji
trygonometrycznych uzupełniających, odwrotnych, hiperbolicznych oraz
odwrotnych hiperbolicznych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
