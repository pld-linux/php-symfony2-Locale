# NOTE:
# The Locale component is deprecated since version 2.3 and will be removed in
# Symfony 3.0. You should use the more capable Intl component instead.
%define		pearname	Locale
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Locale Component
Name:		php-symfony2-Locale
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{pearname}/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	e1177388b6f3b4f16afef67b58d48726
URL:		http://symfony.com/doc/2.2/components/locale.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(spl)
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
%setup -q -n %{pearname}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Tests


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/Locale
%{php_pear_dir}/Symfony/Component/Locale/*.php
%{php_pear_dir}/Symfony/Component/Locale/Stub
%{php_pear_dir}/Symfony/Component/Locale/Exception
