Name:		jackson-bom
Version:	2.21.8
Release:	1
Summary:	Bill of Materials for Jackson components
Group:		Development/Java
License:	ASL 2.0
URL:		https://github.com/FasterXML/jackson-bom
Source0:	https://github.com/FasterXML/jackson-bom/archive/refs/tags/jackson-bom-%{version}.tar.gz#/jackson-bom-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	mvn(com.fasterxml:oss-parent:pom::)
BuildRequires:	mvn(com.fasterxml.jackson:jackson-parent:pom::)
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

%description
Bill of Materials for Jackson 2.21.8, and the jackson-base parent
POM that Jackson components extend. Annotations stay at 2.21.
Core and databind are managed at 2.21.8.
Application projects import jackson-bom.

%prep
%setup -q -n jackson-bom-jackson-bom-%{version}

%files -f .mfiles
%doc LICENSE README.md SECURITY.md release-notes/VERSION-2.x
