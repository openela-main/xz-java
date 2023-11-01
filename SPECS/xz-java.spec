%bcond_with bootstrap

Name:           xz-java
Version:        1.8
Release:        14%{?dist}
Summary:        Java implementation of XZ data compression
License:        Public Domain
URL:            http://tukaani.org/xz/java.html
BuildArch:      noarch

Source0:        http://tukaani.org/xz/xz-java-%{version}.zip

BuildRequires:  javapackages-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  ant
%endif

%description
A complete implementation of XZ data compression in Java.

It features full support for the .xz file format specification version 1.0.4,
single-threaded streamed compression and decompression, single-threaded
decompression with limited random access support, raw streams (no .xz headers)
for advanced users, including LZMA2 with preset dictionary.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c %{name}-%{version}

%mvn_file : %{name} xz

%build
# During documentation generation the upstream build.xml tries to download
# package-list from oracle.com. Create a dummy package-list to prevent that.
mkdir -p extdoc && touch extdoc/package-list

%ant maven -Dsourcever=1.6

%install
%mvn_artifact build/maven/xz-%{version}.pom build/jar/xz.jar

%mvn_install -J build/doc

%files -f .mfiles
%doc README THANKS
%license COPYING

%files javadoc -f .mfiles-javadoc
%license COPYING

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.8-14
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jun 09 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-13
- Rebuild to workaround DistroBaker issue

* Tue Jun 08 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-12
- Bootstrap Maven for CentOS Stream 9

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-11
- Bootstrap build
- Non-bootstrap build

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.8-8
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jun 19 2020 Mat Booth <mat.booth@redhat.com> - 1.8-7
- Allow building against Java 11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-4
- Mass rebuild for javapackages-tools 201902

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-3
- Mass rebuild for javapackages-tools 201901

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Michael Simacek <msimacek@redhat.com> - 1.8-1
- Update to upstream version 1.8

* Tue Jan  2 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-1
- Update to upstream version 1.7

* Mon Nov 27 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-5
- Make use of %%license macro

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Michael Simacek <msimacek@redhat.com> - 1.6-3
- Install with XMvn

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-1
- Update to upstream version 1.6

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-2
- Use .mfiles generated during build

* Mon Mar 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-1
- Update to upstream version 1.5

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Sep 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-1
- Update to upstream version 1.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-1
- Update to upstream version 1.3

* Tue Jan 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-1
- Update to upstream version 1.2

* Thu Jan 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.1-2
- Add patch for OSGi Manifest.

* Fri Aug 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Update to upstream version 1.1

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-3
- Install xz.jar symlink

* Thu Apr 5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> 1.0-2
- Fix issues found during package review
- Include missing COPYING files.
- Add missing RPM group.
- Comment on touching package-list.

* Wed Apr 4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> 1.0-1
- Initial packaging.
