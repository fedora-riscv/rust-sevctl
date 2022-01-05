# Generated by rust2rpm 17
%bcond_without check
%global __cargo_skip_build 0

%global crate sevctl

Name:           rust-%{crate}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Administrative utility for AMD SEV

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/sevctl
Source:         %{crates_source}

# SEV is an AMD x86_64 CPU feature so doesn't make sense to
# try to build on other arches
ExclusiveArch:  x86_64

BuildRequires:  rust-packaging

%global _description %{expand:
Administrative utility for AMD SEV.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%doc README.md
%license LICENSE
%{_bindir}/sevctl

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Tue Jan  4 2022 Daniel P. Berrangé <berrange@redhat.com> - 0.2.0-1
- Update to 0.2.0 release (rhbz #2034304)
- Restrict build arch to x86_64 only

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.1.0-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Connor Kuehl <ckuehl@redhat.com> - 0.1.0-1
- Initial package
