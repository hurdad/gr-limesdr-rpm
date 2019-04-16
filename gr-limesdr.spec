Name:           gr-limesdr
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        GNU Radio LimeSDR Support
Group:          System Environment/Libraries
License:        GNU
URL:            https://github.com/epiqsolutions/gr-sidekiq
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gnuradio-devel
BuildRequires:  LimeSuite-devel
BuildRequires:  boost-devel
BuildRequires:  swig
BuildRequires:  cmake3

%description
Package includes GNU Radio blocks for various LimeSDR boards.

%prep
%setup -n %{name}-%{version}
%build
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{_libdir}/libgnuradio-limesdr.so
%{_libdir}/python2.7/site-packages/limesdr
%{_libdir}/cmake/limesdr/*
%{_datadir}/gnuradio/grc/blocks/limesdr*.xml
%{_datadir}/doc/gr-limesdr*
%{_includedir}/limesdr/*

%changelog
