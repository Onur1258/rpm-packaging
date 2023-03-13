Name:		netflow2ng
Version:	0.0.3
Release:	2%{?dist}
Summary:	dsasdad

License:        MIT
URL:            https://github.com/synfinatic/netflow2ng
Source0:        %{name}-%{version}.tar.gz

BuildRequires:	epel-release
BuildRequires:	bash
BuildRequires:  make
BuildRequires:	golang
BuildRequires:	zeromq-devel
Requires:       golang
Requires:	zeromq-devel

%description
fasanfasjnas

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make
mkdir -p %{buildroot}/usr/local/bin
cp dist/netflow2ng-0.0.3 %{buildroot}/usr/local/bin

%files
/usr/local/bin/netflow2ng-0.0.3
