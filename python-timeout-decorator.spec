# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%bcond_without tests
%global srcname timeout-decorator

Name:           python-%{srcname}
Version:        0.4.1
Release:        2%{?dist}
Summary:        Timeout decorator for Python

License:        MIT
URL:            https://github.com/pnpnpn/timeout-decorator
Source0:        %{pypi_source}

BuildArch:      noarch

%description
A python module which provides a timeout decorator.

%package -n python%{pyver}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pytest
%{?python_provide:%python_provide python%{pyver}-%{srcname}}

%description -n python%{pyver}-%{srcname}
A python module which provides a timeout decorator.

%prep
%autosetup -n %{srcname}-%{version}

%build
%{pyver_build}

%install
%{pyver_install}

%if %{with tests}
%check
python%{pyver} setup.py test
%endif

%files -n python%{pyver}-%{srcname}
%doc README.rst
%{pyver_sitelib}/timeout_decorator
%{pyver_sitelib}/timeout_decorator-%{version}-py?.?.egg-info

%changelog
* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Joel Capitao <jcapitao@redhat.com> - 0.4.1-1
- Initial packaging
