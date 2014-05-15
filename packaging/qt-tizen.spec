Name:           qt-tizen
Version:        0.0.0
Release:        0
License:        GPL-2.0
Summary:        meta package for tizen integration
Url:            https://gitorious.org/qt-tizen
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz

BuildRequires:  make
Requires: qt5-qtdeclarative-examples

%description
Add some links to launcher

%prep
%setup -q

%build
make %{?jobs:-j%jobs} V=1

%install
%make_install

#%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
/*
