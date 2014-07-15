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

Requires: qt5-qtdeclarative-examples
Requires: qt5-tools

%if %{with wayland}
Requires: qtwayland
%endif

%if %{with x}
Requires: qt5-plugin-platform-xcb
%endif

%description
Meta package for tizen platform.
Used to abstract different setup.


%package -n demo
Summary:        Specific tizen files for demos.
BuildRequires:  make

%description -n demo
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


%files -n demo
%defattr(-,root,root)
/*
