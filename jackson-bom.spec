Name:		jackson-bom
Version:	2.23.0
Release:	2
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
BuildRequires:	python
BuildSystem:	maven
# The file attribute generator only emits the pom-typed coordinate.
# Gradle's catalog asks for the untyped name.
Provides:	mvn(com.fasterxml.jackson:jackson-bom) = %{version}

%description
Bill of Materials for Jackson 2.23.0, and the jackson-base parent
POM that Jackson components extend. Annotations are managed at 2.23.
Core and databind are managed at 2.23.0. The managed Woodstox
version is 7.3.0 and stax2-api is 4.3.1.
Application projects import jackson-bom.

%prep
%setup -q -n jackson-bom-jackson-bom-%{version}

%check
python - <<'PY'
import xml.etree.ElementTree as ET
NS = {"m": "http://maven.apache.org/POM/4.0.0"}
root = ET.parse("%{buildroot}/usr/share/maven-poms/jackson-bom.pom").getroot()
props = {}
for el in root.find("m:properties", NS):
    props[el.tag.split("}")[-1]] = (el.text or "").strip()
core = props["jackson.version"]
ann = props["jackson.version.annotations"]
if core != "%{version}" or ann != "2.23":
    raise SystemExit("bad bom %s %s" % (core, ann))
art = root.find("m:artifactId", NS).text
if art != "jackson-bom":
    raise SystemExit("bad artifact " + art)
print("jackson_bom_ok", core, ann)
PY

%files -f .mfiles
%doc LICENSE README.md SECURITY.md release-notes/VERSION-2.x
