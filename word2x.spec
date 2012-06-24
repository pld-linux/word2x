Summary:	word2x convert word 6 documents to another format
Summary(pl):	Konwerter dokument�w MS Worda 6 do innych format�w
Name:		word2x
Version:	0.005
Release:	3
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	http://word2x.alcom.co.uk/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
URL:		http://word2x.alcom.co.uk
Vendor:		Duncan Simpson <dps@io.stargate.co.uk>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	libstdc++-devel

%description
word2x is a program that attempts to produce a component, if not
perfect rendition of a word 6 document. It guesses rather a lot from
context and can make mistakes.

%prep
%setup -q
%patch -p1

%build
chmod u+w *
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
aclocal
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install word2x rtest2 $RPM_BUILD_ROOT%{_bindir}
install word2x.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README INTERNALS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755, root, root) %{_bindir}/word2x
%attr(755, root, root) %{_bindir}/rtest2
%{_mandir}/man1/word2x.1*
