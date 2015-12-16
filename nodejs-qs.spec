%{?scl:%scl_package nodejs-qs}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-qs
Version:	1.2.2
Release:	1%{?dist}
Summary:	A querystring parser that supports nesting and arrays, with a depth limit
License:	BSD
URL:		https://github.com/hapijs/qs.git
Source0:	http://registry.npmjs.org/qs/-/qs-%{version}.tgz

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch:	%{nodejs_arches} noarch
%else
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	npm(lab)
%endif

%description
A querystring parsing and stringifying library with some added security.
%prep
%setup -q -n package
#%setup -q -T -D -a 1 -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/qs
cp -pr package.json lib index.js \
    %{buildroot}%{nodejs_sitelib}/qs

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
make test-cov
%endif

%files
%doc README.md LICENSE
%{nodejs_sitelib}/qs

%changelog
* Thu Aug 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.2-1
- New upstrem release
- change license
- change URL
- remove Source1 and Source10
- add LICENSE to %%doc
- updated Summary and %%description

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.6.5-4
- replace provides and requires with macro

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.5-3
- add ExclusiveArch logic

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.5-2
- restrict to compatible arches

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.5-1
- update to upstream release 0.6.5

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.5.6-2
- add macro to enable dependency generation in EPEL

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5.6-2
- Add support for software collections

* Wed Apr 10 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.6-1
- update to upstream release 0.5.6

* Fri Mar 22 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.5-1
- update to upstream release 0.5.5

* Sat Mar 16 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.4-1
- update to upstream release 0.5.4

* Wed Feb 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.3-3
- fix typo in %%description

* Wed Feb 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.3-2
- fix typo in %%summary

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.3-1
- initial package
