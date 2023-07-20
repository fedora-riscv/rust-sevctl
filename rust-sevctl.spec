# Generated by rust2rpm 22
%bcond_without check

%global crate sevctl

Name:           rust-sevctl
Version:        0.4.1
Release:        1%{?dist}
Summary:        Administrative utility for AMD SEV

License:        Apache-2.0
URL:            https://crates.io/crates/sevctl
Source0:        %{crates_source}
Source1:        LICENSE.dependencies

# SEV is an AMD x86_64 CPU feature so doesn't make sense to
# try to build on other arches
ExclusiveArch:  x86_64

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Administrative utility for AMD SEV.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# Zlib OR Apache-2.0 OR MIT
License:        Apache-2.0 AND MIT
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/sevctl

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
cp -pav %{SOURCE1} .
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
* Wed Jul 19 2023 Tyler Fanelli <tfanelli@redhat.com> - 0.4.1-1
* Update to 0.4.1
- Remove patch to update sev dependency.

* Wed May 03 2023 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-4
- Rebuild for openssl crate >= v0.10.48 (RUSTSEC-2023-{0022,0023,0024})

* Thu Feb 09 2023 Sergio Lopez <slp@redhat.com> - 0.3.2-3
- Include a patch to update sev dependency

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Tyler Fanelli <tfanelli@redhat.com> - 0.3.2-1
- Update to 0.3.2 (rhbz#2143857)

* Thu Aug 25 2022 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-2
- Regenerate with rust2rpm v22 and specify License for binary package.

* Thu Aug 25 2022 Cole Robinson <crobinso@redhat.com> - 0.3.0-1
- Update to 0.3.0 (rhbz #2097875)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.0-4
- Rebuild with package notes

* Tue Feb 15 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.0-3
- Rebuild with package notes

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan  4 2022 Daniel P. Berrangé <berrange@redhat.com> - 0.2.0-1
- Update to 0.2.0 release (rhbz #2034304)
- Restrict build arch to x86_64 only

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.1.0-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Connor Kuehl <ckuehl@redhat.com> - 0.1.0-1
- Initial package
