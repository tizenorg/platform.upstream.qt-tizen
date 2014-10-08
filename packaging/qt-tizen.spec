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
Requires: qt5-qtwayland
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
Requires: qt5-plugin-accessible-widgets
Requires: qt5-plugin-imageformat-gif
Requires: qt5-plugin-imageformat-ico
Requires: qt5-plugin-imageformat-jpeg
Requires: qt5-plugin-platform-minimal
Requires: qt5-qtdeclarative-devel-tools
Requires: qt5-qtdeclarative-examples
Requires: qt5-qtdeclarative-import-folderlistmodel
Requires: qt5-qtdeclarative-import-localstorageplugin
Requires: qt5-qtdeclarative-import-multimedia
Requires: qt5-qtdeclarative-import-particles2
Requires: qt5-qtdeclarative-import-qtquick2plugin
Requires: qt5-qtdeclarative-import-qttest
Requires: qt5-qtdeclarative-import-sensors
Requires: qt5-qtdeclarative-import-settings
Requires: qt5-qtdeclarative-qtquick-widgets
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtmultimedia
Requires: qt5-qtmultimedia-plugin-audio-alsa
Requires: qt5-qtmultimedia-plugin-mediaservice-gstmediaplayer
Requires: qt5-qtquickcontrols
Requires: qt5-tools
Requires: qt5-qttools-qtdesigner
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

%__make %{?_smp_mflags}


%install
%make_install

#%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files

%files full

%files demo
%defattr(-,root,root)
/home/*/.applications/desktop/*
/home/*/*.qml
/opt/share/widget_demo/*
%{_bindir}/*.sh
