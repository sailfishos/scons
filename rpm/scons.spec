Name:           scons
Version:        4.5.1
Release:        1
Summary:        An Open Source software construction tool
License:        MIT
URL:            https://github.com/sailfishos/scons/
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  fdupes
BuildRequires:  python3-lxml

%description
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Man pages for %{name}.

%prep
%setup -q -n %{name}-%{version}/upstream
sed -i 's|/usr/bin/env python|%{__python3}|' scripts/*

%build
%{__python3} scripts/scons.py --include-dir= -j1 SKIP_DOC=True

%install
%py3_install -- --install-scripts=%{_bindir} --install-data=%{_datadir}

%fdupes $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        CHANGES.txt README.rst RELEASE.txt

rm -f %{buildroot}%{_datadir}/*.1

%files
%license LICENSE
%{_bindir}/scons
%{_bindir}/scons-configure-cache
%{_bindir}/sconsign
%{python3_sitelib}/SCons
%{python3_sitelib}/SCons*.egg-info

%files doc
%doc %{_docdir}/%{name}-%{version}
