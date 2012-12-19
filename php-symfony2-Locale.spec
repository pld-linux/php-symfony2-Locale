%define		status		stable
%define		pearname	Locale
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Symfony2 Locale Component
Name:		php-symfony2-Locale
Version:	2.1.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	33c740ad31510ce6187b6f11ea8a4e87
URL:		http://symfony.com/doc/current/components/locale.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Symfony2 Locale Component

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

# no packaging of tests
rm -r .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests
rm .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist

# fixups
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/CHANGELOG.md .
rm .%{php_pear_dir}/Symfony/Component/%{pearname}/.gitattributes
rm .%{php_pear_dir}/Symfony/Component/%{pearname}/.gitignore
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
%dir %{php_pear_dir}/Symfony/Component/Locale/Resources
%{php_pear_dir}/Symfony/Component/Locale/Resources/stubs
%dir %{php_pear_dir}/Symfony/Component/Locale/Resources/data
%dir %{php_pear_dir}/Symfony/Component/Locale/Resources/data/49
%dir %{php_pear_dir}/Symfony/Component/Locale/Resources/data/49/lang
%dir %{php_pear_dir}/Symfony/Component/Locale/Resources/data/49/locales
%dir %{php_pear_dir}/Symfony/Component/Locale/Resources/data/49/names
%dir %{php_pear_dir}/Symfony/Component/Locale/Resources/data/49/region

# XXX %lang tags
%{php_pear_dir}/Symfony/Component/Locale/Resources/data/49/lang/*.res
%{php_pear_dir}/Symfony/Component/Locale/Resources/data/49/locales/*.res
%{php_pear_dir}/Symfony/Component/Locale/Resources/data/49/names/*.res
%{php_pear_dir}/Symfony/Component/Locale/Resources/data/49/region/*.res
%{php_pear_dir}/Symfony/Component/Locale/Resources/data/49/stub
%{php_pear_dir}/Symfony/Component/Locale/Resources/data/49/svn-info.txt
%{php_pear_dir}/Symfony/Component/Locale/Resources/data/UPDATE.txt
%{php_pear_dir}/Symfony/Component/Locale/Resources/data/build-data.php
%{php_pear_dir}/Symfony/Component/Locale/Resources/data/icu.ini
