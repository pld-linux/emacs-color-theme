Summary:	Themes for Emacs
Summary(pl):	Zestaw tematów dla Emacsa
Name:		emacs-color-theme
Version:	6.5.4
Release:	0.1
License:	GPL v2
Group:		Applications/Editors/Emacs
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	229d1ba05debc0b697ed5cc788645d96
Requires:	emacs >= 21.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Themes for Emacs.

%description -l pl
Zestaw tematów dla Emacsa.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
install *.el	$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/emacs/site-lisp/*.el
