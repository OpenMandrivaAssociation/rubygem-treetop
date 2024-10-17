%define gemname treetop
Summary:	A Ruby-based text parsing and interpretation DSL
Name:		rubygem-%{gemname}
Version:	1.4.10
Release:	5
Source0:	http://rubygems.org/downloads/%{gemname}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		https://www.rubyonrails.org/
BuildRoot:	%{_tmppath}/%{gemname}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-RubyGems
Provides:       rubygem(%{gemname}) = %{version}

%description
A Ruby-based text parsing and interpretation DSL.

%prep
%setup -c

%build

%install
rm -rf $RPM_BUILD_ROOT

gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/tt
%{ruby_gemdir}/gems/%{gemname}-%{version}
%{ruby_gemdir}/specifications/%{gemname}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{gemname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.4.10-4
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 1.4.10-3
+ Revision: 769824
- Fix file list

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 1.4.10-2
+ Revision: 769774
- Manual provides

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 1.4.10-1
+ Revision: 769769
- First mdv package
- Created package structure for 'rubygem-treetop'.

