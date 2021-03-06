# NOTE:
# The Locale component is deprecated since version 2.3 and will be removed in
# Symfony 3.0. You should use the more capable Intl component instead.
%define		package	Locale
%define		php_min_version 5.3.9
Summary:	Symfony2 Locale Component
Name:		php-symfony2-Locale
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	dfa4df9bfdc21e3edfaf4200d1dbebf8
URL:		http://symfony.com/doc/2.2/components/locale.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(spl)
Requires:	php-dirs >= 1.6
Requires:	php-symfony2-Intl >= 2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale component provides fallback code to handle cases when the intl
extension is missing. Additionally it extends the implementation of a
native Locale class with several handy methods.

The Locale component is deprecated since version 2.3 and will be
removed in Symfony 3.0. You should use the more capable Intl component
instead.

%prep
%setup -q -n locale-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/Locale
%{php_data_dir}/Symfony/Component/Locale/*.php
%{php_data_dir}/Symfony/Component/Locale/Stub
%{php_data_dir}/Symfony/Component/Locale/Exception
