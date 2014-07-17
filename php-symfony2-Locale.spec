# NOTE:
# The Locale component is deprecated since version 2.3 and will be removed in
# Symfony 3.0. You should use the more capable Intl component instead.
%define		pearname	Locale
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Locale Component
Name:		php-symfony2-Locale
Version:	2.4.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	85a8b718baa02f0506a187ad420f0644
URL:		http://symfony.com/doc/2.2/components/locale.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(spl)
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Requires:	php-symfony2-Intl >= 2.3
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
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests .
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist .

# fixups
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/Locale
%{php_pear_dir}/Symfony/Component/Locale/*.php
%{php_pear_dir}/Symfony/Component/Locale/Stub
%{php_pear_dir}/Symfony/Component/Locale/Exception
