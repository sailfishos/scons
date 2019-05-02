Name:           scons
Version:        3.0.5
Release:        1
Summary:        An Open Source software construction tool
Group:          Development/Tools
License:        MIT
URL:            http://www.scons.org
Source:         http://prdownloads.sourceforge.net/scons/scons-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  fdupes
# Currently mer:core does not have this package. scons works without it,
# but manpages are not generated correctly.
# BuildRequires:  python3-lxml

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
Group:     Documentation
Requires:  %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Man pages for %{name}.

%prep
%setup -q -n %{name}-%{version}/upstream
sed -i 's|/usr/bin/env python|%{__python3}|' src/script/*

%build
%{__python3} bootstrap.py build/scons
cd build/scons
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build

%install
pushd build/scons
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install \
 --root=$RPM_BUILD_ROOT \
 --record=INSTALLED_FILES \
 --standard-lib \
 --install-scripts=%{_bindir} \
 --no-install-bat \
 --no-version-script
%fdupes $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
popd
install -m 644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        src/CHANGES.txt README.rst src/RELEASE.txt
mv $RPM_BUILD_ROOT%{_prefix}/man/* $RPM_BUILD_ROOT%{_mandir}

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/scons
%{_bindir}/scons-configure-cache
%{_bindir}/scons-time
%{_bindir}/sconsign
%{_libdir}/python3.*/site-packages/SCons
%{_libdir}/python3.*/site-packages/scons*.egg-info

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}
%{_mandir}/man1/%{name}*.*
