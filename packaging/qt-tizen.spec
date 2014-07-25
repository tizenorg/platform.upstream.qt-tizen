%bcond_with wayland
%bcond_with x

Name:           qt-tizen
Version:        0.0.1
Release:        0
License:        GPL-2.0
Summary:        meta package for tizen integration
Url:            https://gitorious.org/qt-tizen
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch


%if %{with wayland}
Requires: qtwayland
%endif

%if %{with x}
Requires: qt5-plugin-platform-xcb
%endif

%description
Meta package for tizen platform.
Used to abstract different setup.


%package full
Summary:  All Qt packages supported on Tizen.
Requires: qt-tizen = %{version}-%{release}
Requires: qt5-plugin-imageformat-jpeg
Requires: qt5-qtdeclarative-examples
Requires: qt5-qtdeclarative-import-folderlistmodel
Requires: qt5-qtdeclarative-import-multimedia
Requires: qt5-qtdeclarative-import-particles2
Requires: qt5-qtdeclarative-import-qtquick2plugin
Requires: qt5-tools
Requires: qt5-qtdeclarative-devel-tools
BuildArch:  noarch

%description full
All needed packages for tizen.


%package demo
Summary:        Specific tizen files for demos.
BuildRequires:  make
Requires: qt-tizen = %{version}-%{release}
BuildArch:  noarch

%description demo
Add some links to launcher


%prep
%setup -q

%build
make %{?_smp_mflags}


%install
%make_install

#%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files

%files full

%files demo
%defattr(-,root,root)
/*
