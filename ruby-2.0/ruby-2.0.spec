# To build:
# 
# sudo yum -y install rpmdevtools && rpmdev-setuptree
#
#
# sudo yum -y install readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libffi-devel
# 
# wget https://raw.github.com/nmilford/specfiles/master/ruby-2.0/ruby-2.0.spec -O ~/rpmbuild/SPECS/ruby-2.0.spec
# wget http://ftp.ruby-lang.org/pub/ruby/2.0/ruby-2.0.0-rc1.tar.gz -O ~/rpmbuild/SOURCES/ruby-2.0.0-rc1.tar.gz
# 
# rpmbuild -bb ~/rpmbuild/SPECS/ruby-2.0.spec

%define rubyver         2.0.0
%define rubyminorver    rc1

Name:           ruby
Version:        %{rubyver}_%{rubyminorver}
Release:        1%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libffi-devel
Requires:       libyaml
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}-%{rubyminorver}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Provides: ruby(abi) = 2.0
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: rubygems
Obsoletes: ruby
Obsoletes: ruby-libs
Obsoletes: ruby-irb
Obsoletes: ruby-rdoc
Obsoletes: ruby-devel
Obsoletes: rubygems

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}-%{rubyminorver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}
%{_includedir}
%{_datadir}
%{_libdir}

%changelog
* Mon Jan 7 2013 Nathan Milford <nathan@milford.io> - 2.0.0-rc1
- Initial 2.0.0 release candidate.
* Sun Nov 25 2012 Gareth Jones <me@gazj.co.uk> - 1.9.3-p327
- Update for Ruby 1.9.3-p327 release.
* Wed Apr 25 2012 mathew <meta@pobox.com> - 1.9.3-p194-1
- Update for Ruby 1.9.3-p194 release.
* Sat Feb 24 2012 Ian Meyer <ianmmeyer@gmail.com> - 1.9.3-p125-1
- Spec to replace system ruby with 1.9.3-p125
