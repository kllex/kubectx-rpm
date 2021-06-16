%global with_bundled 0
%global with_debug 0
%global with_unit_test 0
%global _dwz_low_mem_die_limit 0

Name:           kubectx
Version:        0.9.3
Release:        1%{?dist}
Summary:        kubectx helps you switch between clusters back and forth
License:        Apache License 2.0
URL:            https://github.com/ahmetb/kubectx
Source0:        v%{version}.tar.gz

ExclusiveArch:  %{go_arches}
BuildRequires:  compiler(golang)
BuildRequires:  coreutils
BuildRequires:  git

%description
kubectx helps you switch between clusters back and forth.
kubens helps you switch between Kubernetes namespaces smoothly.

%prep
%setup -q -n %{name}-%{version}

%build
export CGO_ENABLED=0
go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')" -o bin/kubectx ./cmd/kubectx
go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')" -o bin/kubens ./cmd/kubens

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}/etc/bash_completion.d/
install -p -m 755 bin/kubectx %{buildroot}%{_bindir}
install -p -m 755 bin/kubens %{buildroot}%{_bindir}
install -p -m 644 completion/kubectx.bash %{buildroot}/etc/bash_completion.d/
install -p -m 644 completion/kubens.bash %{buildroot}/etc/bash_completion.d/

%files
%license LICENSE
%doc README.md CONTRIBUTING.md completion
%{_bindir}/kubectx
%{_bindir}/kubens
/etc/bash_completion.d/kubectx.bash
/etc/bash_completion.d/kubens.bash

%changelog
* Thu Jun 17 2021 Alexander Knezevic-Lütke <akl@web.de> - %{version}-1
- new upstream version

