Name:		json-simple
Version:	4.0.1
Release:	1
Summary:	JSON encoding and decoding
Group:		Development/Java
License:	ASL 2.0
URL:		https://github.com/cliftonlabs/json-simple
Source0:	https://github.com/cliftonlabs/json-simple/archive/refs/tags/json-simple-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

%description
JSON.simple 4.0.1 reads and writes JSON. Chain helpers append to
JsonArray and JsonObject, and JsonException.getPosition returns a long.
A solidus is left unescaped. The lexer class is already generated, so
the build does not run JFlex. Velocity Tools calls Jsoner.deserialize
and the JsonObject and JsonArray accessors.

%prep
%autosetup -n json-simple-json-simple-%{version}
# The POM pins compiler 3.8.1 and JFlex 1.8.2. Those plugins are
# removed. Yylex.java is already in the tree.
python - <<'PY'
import xml.etree.ElementTree as ET
NS = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace("", NS)

def local(tag):
    return tag.split("}", 1)[-1]

tree = ET.parse("pom.xml")
root = tree.getroot()
for node in list(root):
    if local(node.tag) in {"build", "profiles"}:
        root.remove(node)
tree.write("pom.xml", encoding="utf-8", xml_declaration=True)
PY

%files -f .mfiles
%doc LICENSE README
