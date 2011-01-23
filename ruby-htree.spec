Summary:	An HTML parser
Summary(pl.UTF-8):	Analizator HTML-a
Name:		ruby-htree
Version:	0.4
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://cvs.m17n.org/viewcvs/ruby/htree.tar.gz
# Source0-md5:	8f9b47308463d267753a91e901b68c32
URL:		http://cvs.m17n.org/~akr/htree/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.3.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
htree provides a tree data structure which represent HTML and XML
data.

%description -l pl.UTF-8
htree udostępnia drzewiastą strukturę danych reprezentującą dane HTML
i XML.

%prep
%setup -q -n htree
cp %{_datadir}/setup.rb .

%build
mkdir lib
mv htree.rb htree lib/
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

# rdoc crashes on _why's craaazy code.
#rdoc --op rdoc lib
#rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

#cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc rdoc
%{ruby_rubylibdir}/htree*
#%{ruby_ridir}/*
