%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm_DHTMLRulesTableless
%define		_status		alpha
%define		_pearname	HTML_QuickForm_DHTMLRulesTableless

Summary:	%{_pearname} - DHTML replacement for the standard JavaScript alert window for client-side validation using the tableless renderer
Summary(pl):	%{_pearname} - zamiennik DHTML dla standardowego okna z ostrzeżeniem JavaScript dla sprawdzania poprawości po stronie klienta
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	45fc74c53f20dc37f58fa5579736db26
URL:		http://pear.php.net/package/HTML_QuickForm_DHTMLRulesTableless/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_QuickForm_Renderer_Tableless >= 0.3.0
Requires:	php-pear-PEAR >= 1:1.4.-0.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a DHTML replacement for the standard JavaScript alert window
for client-side validation of forms built with HTML_QuickForm when
using the HTML_QuickForm_Renderer_Tableless renderer.

In PEAR status of this package is: %{_status}.

%description -l pl
Jest to zamiennik DHTML dla standardowego okna z ostrzeżeniem
JavaScript dla sprawdzania po stronie klienta poprawności formularzy
zbudowanych za pomocą HTML_QuickForm przy użyciu renderera
HTML_QuickForm_Renderer_Tableless.

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
%doc install.log docs/%{_pearname}/docs/examples/contact_dhtmlrules.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/QuickForm/DHTMLRulesTableless.php
