%define	name		tinyca 
%define	realname	%{name}2
%define version		0.7.5
%define release		%mkrel 1

%define localedir	%{_datadir}/locale

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{realname}-%{version}.tar.bz2
URL:		http://tinyca.sm-zone.net/
Group:		System/Servers
License:	GPL
Summary:	Small Certification Authority (CA) manager 
BuildRoot:	%{_tmppath}/%{name}-%{version}-buidroot
Requires:	zip
Obsoletes:    	TinyCA
Provides:	TinyCA
BuildArch:	noarch

%description 
TinyCA is a simple graphical user interface written in Perl/Gtk to manage
a small CA (Certification Authority). TinyCA works as a frontend for
openssl.

%prep
%setup -q -n %{realname}-%{version}
cd $RPM_BUILD_DIR/%{realname}-%{version}
%{__ln_s} %{realname} %{name}

# Configure pristine source
%{__perl} -pi -e 's:./lib:%{_libdir}/%{name}/lib:g' %{realname}
%{__perl} -pi -e 's:./templates:%{_libdir}/%{name}/templates:g' %{realname}
%{__perl} -pi -e 's:./locale:%{localedir}:g' %{realname}

%build
%install
%{__rm} -rf %buildroot
%{__mkdir_p} $RPM_BUILD_ROOT%{_libdir}/%{name}/{lib,templates}
%{__mkdir_p} $RPM_BUILD_ROOT%{_libdir}/%{name}/lib/GUI
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}/
%{__mkdir_p} $RPM_BUILD_ROOT%{localedir}/cs/LC_MESSAGES/
%{__mkdir_p} $RPM_BUILD_ROOT%{localedir}/de/LC_MESSAGES/
%{__mkdir_p} $RPM_BUILD_ROOT%{localedir}/es/LC_MESSAGES/

%{__install} -m 444 lib/*.pm $RPM_BUILD_ROOT%{_libdir}/%{name}/lib/
%{__install} -m 444 lib/GUI/*.pm $RPM_BUILD_ROOT%{_libdir}/%{name}/lib/GUI/
%{__install} -m 644 templates/openssl.cnf $RPM_BUILD_ROOT%{_libdir}/%{name}/templates/
%{__install} -m 755 %{realname} $RPM_BUILD_ROOT%{_bindir}/%{realname}
%{__mv} %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__install} -m 644 po/cs.mo $RPM_BUILD_ROOT%{localedir}/cs/LC_MESSAGES/
%{__install} -m 644 po/de.mo $RPM_BUILD_ROOT%{localedir}/de/LC_MESSAGES/
%{__install} -m 644 po/es.mo $RPM_BUILD_ROOT%{localedir}/es/LC_MESSAGES/

%find_lang %name

%clean
%{__rm} -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc CHANGES INSTALL
%{_bindir}/*
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/lib/GUI/
%dir %{_libdir}/%{name}/templates/
%lang(cs) %{localedir}/cs/LC_MESSAGES/*
%lang(de) %{localedir}/de/LC_MESSAGES/*
%lang(es) %{localedir}/es/LC_MESSAGES/*
%{_libdir}/%{name}/templates/openssl.cnf
%{_libdir}/%{name}/lib


