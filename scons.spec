Name:           scons
Version:        2.0.1
Release:        1

Summary:        An Open Source software construction tool

Group:          Development/Tools
License:        MIT
URL:            http://www.scons.org
Source:         http://prdownloads.sourceforge.net/scons/scons-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python

%description
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software.  SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax.  SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines.  SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched.  SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.


%prep
%setup -q 


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES --install-lib=%{_prefix}/lib/scons --install-scripts=%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}
mv $RPM_BUILD_ROOT%{_prefix}/man/* $RPM_BUILD_ROOT%{_mandir}


%clean
rm -rf $RPM_BUILD_ROOT

%docs_package 

%files
%defattr(-,root,root,-)
%doc  LICENSE.txt 
%{_bindir}/*
%{_prefix}/lib/scons
