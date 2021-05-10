Name:           resteasy
Version:        3.0.26
Release:        8%{?_timestamp}%{?_commit_id}%{?dist}
Summary:        Framework for RESTful Web services and Java applications
License:        ASL 2.0
URL:            http://resteasy.jboss.org/
Source0:        https://github.com/dogtagpki/Resteasy/archive/%{version}%{?_phase}/%{name}-%{version}%{?_phase}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.tomcat:tomcat-servlet-api)

# Jackson 2
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)

BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:  mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec)
BuildRequires:  mvn(org.slf4j:slf4j-api)

%description
%global desc \
RESTEasy contains a JBoss project that provides frameworks to help\
build RESTful Web Services and RESTful Java applications. It is a fully\
certified and portable implementation of the JAX-RS specification.
%{desc}
%global extdesc %{desc}\
\
This package contains

%package -n     pki-%{name}
Summary:        Framework for RESTful Web services and Java applications
Obsoletes:      %{name} < %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

Requires:       pki-%{name}-atom-provider     = %{version}-%{release}
Requires:       pki-%{name}-client            = %{version}-%{release}
Requires:       pki-%{name}-core              = %{version}-%{release}
Requires:       pki-%{name}-jackson2-provider = %{version}-%{release}
Requires:       pki-%{name}-jaxb-provider     = %{version}-%{release}

# subpackages removed in fedora 32
Obsoletes:      %{name}-fastinfoset-provider < 3.0.26-1
Obsoletes:      %{name}-jackson-provider < 3.0.26-1
Obsoletes:      %{name}-jettison-provider < 3.0.26-1
Obsoletes:      %{name}-json-p-provider < 3.0.26-1
Obsoletes:      %{name}-multipart-provider < 3.0.26-1
Obsoletes:      %{name}-netty3 < 3.0.26-1
Obsoletes:      %{name}-optional < 3.0.26-1
Obsoletes:      %{name}-test < 3.0.26-1
Obsoletes:      %{name}-validator-provider-11 < 3.0.26-1
Obsoletes:      %{name}-yaml-provider < 3.0.26-1

%description -n pki-%{name}
%{desc}

%package -n     pki-%{name}-javadoc
Summary:        Javadoc for %{name}
Obsoletes:      %{name}-javadoc < %{version}-%{release}
Conflicts:      %{name}-javadoc < %{version}-%{release}
Provides:       %{name}-javadoc = %{version}-%{release}

%description -n pki-%{name}-javadoc
This package contains the API documentation for %{name}.

%package -n     pki-%{name}-core
Summary:        Core modules for %{name}
Obsoletes:      resteasy-jaxrs-api < 3.0.7
Obsoletes:      %{name}-core < %{version}-%{release}
Conflicts:      %{name}-core < %{version}-%{release}
Provides:       %{name}-core = %{version}-%{release}

%description -n pki-%{name}-core
%{extdesc} %{summary}.

%package -n     pki-%{name}-atom-provider
Summary:        Module atom-provider for %{name}
Obsoletes:      %{name}-atom-provider < %{version}-%{release}
Conflicts:      %{name}-atom-provider < %{version}-%{release}
Provides:       %{name}-atom-provider = %{version}-%{release}

%description -n pki-%{name}-atom-provider
%{extdesc} %{summary}.

%package -n     pki-%{name}-jackson2-provider
Summary:        Module jackson2-provider for %{name}
Obsoletes:      %{name}-jackson2-provider < %{version}-%{release}
Conflicts:      %{name}-jackson2-provider < %{version}-%{release}
Provides:       %{name}-jackson2-provider = %{version}-%{release}

%description -n pki-%{name}-jackson2-provider
%{extdesc} %{summary}.

%package -n     pki-%{name}-jaxb-provider
Summary:        Module jaxb-provider for %{name}
Obsoletes:      %{name}-jaxb-provider < %{version}-%{release}
Conflicts:      %{name}-jaxb-provider < %{version}-%{release}
Provides:       %{name}-jaxb-provider = %{version}-%{release}

%description -n pki-%{name}-jaxb-provider
%{extdesc} %{summary}.

%package -n     pki-%{name}-client
Summary:        Client for %{name}
Obsoletes:      %{name}-client < %{version}-%{release}
Conflicts:      %{name}-client < %{version}-%{release}
Provides:       %{name}-client = %{version}-%{release}

%description -n pki-%{name}-client
%{extdesc} %{summary}.

%prep
%autosetup -n %{name}-%{version}%{?_phase} -p 1

%pom_disable_module arquillian
%pom_disable_module eagledns
%pom_disable_module jboss-modules
%pom_disable_module profiling-tests
%pom_disable_module resteasy-bom
%pom_disable_module resteasy-cache
%pom_disable_module resteasy-cdi
%pom_disable_module resteasy-dependencies-bom
%pom_disable_module resteasy-guice
%pom_disable_module resteasy-jaxrs-testsuite
%pom_disable_module resteasy-jsapi
%pom_disable_module resteasy-jsapi-testing
%pom_disable_module resteasy-links
%pom_disable_module resteasy-servlet-initializer
%pom_disable_module resteasy-spring
%pom_disable_module resteasy-wadl
%pom_disable_module resteasy-wadl-undertow-connector
%pom_disable_module security
%pom_disable_module server-adapters
%pom_disable_module testsuite
%pom_disable_module tjws

pushd providers
%pom_disable_module fastinfoset
%pom_disable_module jackson
%pom_disable_module jettison
%pom_disable_module json-p-ee7
%pom_disable_module multipart
%pom_disable_module resteasy-html
%pom_disable_module resteasy-validator-provider-11
%pom_disable_module yaml
popd

find -name '*.jar' -print -delete

%pom_remove_plugin :maven-clover2-plugin

# remove activation.jar dependencies
%pom_remove_dep -r javax.activation:activation resteasy-jaxrs resteasy-spring

# remove resteasy-dependencies pom
%pom_remove_dep "org.jboss.resteasy:resteasy-dependencies"

# remove redundant jcip-dependencies dep from resteasy-jaxrs
%pom_remove_dep net.jcip:jcip-annotations resteasy-jaxrs

# remove junit dependency from all modules
%pom_remove_dep junit:junit resteasy-client
%pom_remove_dep junit:junit providers/resteasy-atom
%pom_remove_dep junit:junit providers/jaxb
%pom_remove_dep junit:junit resteasy-jaxrs

# depend on servlet-api from pki-servlet-4.0-api
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api resteasy-jaxrs
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/abdera-atom
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/jaxb
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/jackson2

# add dependencies for EE APIs that were removed in Java 11
%pom_add_dep javax.xml.bind:jaxb-api resteasy-jaxrs

%pom_remove_plugin :maven-clean-plugin

%mvn_package ":resteasy-jaxrs" core
%mvn_package ":providers-pom" core
%mvn_package ":resteasy-jaxrs-all" core
%mvn_package ":resteasy-pom" core
%mvn_package ":resteasy-atom-provider" atom-provider
%mvn_package ":resteasy-jackson2-provider" jackson2-provider
%mvn_package ":resteasy-jaxb-provider" jaxb-provider
%mvn_package ":resteasy-client" client

# Disable useless artifacts generation, package __noinstall do not work
%pom_add_plugin org.apache.maven.plugins:maven-source-plugin . '
<configuration>
 <skipSource>true</skipSource>
</configuration>'

%build
%mvn_build -f

%install
%mvn_install

%files -n pki-%{name}
%doc README.md
%license License.html

%files -n pki-%{name}-core -f .mfiles-core
%license License.html

%files -n pki-%{name}-atom-provider -f .mfiles-atom-provider
%license License.html

%files -n pki-%{name}-jackson2-provider -f .mfiles-jackson2-provider
%license License.html

%files -n pki-%{name}-jaxb-provider -f .mfiles-jaxb-provider
%license License.html

%files -n pki-%{name}-client -f .mfiles-client
%license License.html

%files -n pki-%{name}-javadoc -f .mfiles-javadoc
%license License.html

%changelog
* Wed Sep 22 2021 Dogtag PKI Team <devel@lists.dogtagpki.org> 3.0.26-0
- To list changes in <branch> since <tag>:
  $ git log --pretty=oneline --abbrev-commit --no-decorate <tag>..<branch>
