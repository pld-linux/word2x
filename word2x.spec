Summary:	word2x convert word 6 documents to another format
Name:		word2x
Version:	0.005
Release:	1
License:	GPL
Group:		Utilities/Text
Source:		http://word2x.alcom.co.uk/download/%{name}-%{version}.tar.gz
URL:		http://word2x.alcom.co.uk
Vendor:		Duncan Simpson <dps@io.stargate.co.uk>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
word2x is a program that attempts to produce a component, if not perfect
rendition of a word 6 document. It guesses rather a lot from context and
can make mistakes.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s word2x rtest2 $RPM_BUILD_ROOT%{_bindir}
install word2x.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755, root, root) %{_bindir}/word2x
%attr(755, root, root) %{_bindir}/rtest2
%{_mandir}/man1/word2x.1.gz
