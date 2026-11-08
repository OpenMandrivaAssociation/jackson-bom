Name:		jackson-bom
Version:	2.23.0
Release:	1
Summary:	Bill of Materials for Jackson components
Group:		Development/Java
License:	ASL 2.0
URL:		https://github.com/FasterXML/jackson-bom
Source0:	https://github.com/FasterXML/jackson-bom/archive/refs/tags/jackson-bom-%{version}.tar.gz#/jackson-bom-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	mvn(com.fasterxml:oss-parent:pom::)
BuildRequires:	mvn(com.fasterxml.jackson:jackson-parent:pom::)
BuildRequires:	fasterxml-oss-parent >= 81
BuildRequires:	jackson-parent >= 2.23
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

%description
Bill of Materials for Jackson 2.23.0, and the jackson-base parent
POM that Jackson components extend. Annotations are managed at 2.23.
Core and databind are managed at 2.23.0. The managed Woodstox
version is 7.3.0 and stax2-api is 4.3.1.
Application projects import jackson-bom.

%prep
%setup -q -n jackson-bom-jackson-bom-%{version}

%files -f .mfiles
%doc LICENSE README.md SECURITY.md release-notes/VERSION-2.x
