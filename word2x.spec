Summary:	word2x convert word 6 documents to another format
Summary(pl):	Konwerter dokumentów MS Worda 6 do innych formatów
Name:		word2x
Version:	0.005
Release:	4
License:	GPL
Vendor:		Duncan Simpson <dps@io.stargate.co.uk>
Group:		Applications/Text
Source0:	http://word2x.alcom.co.uk/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
Patch1:		%{name}-gcc3.patch
URL:		http://word2x.alcom.co.uk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
word2x is a program that attempts to produce a component, if not
perfect rendition of a word 6 document. It guesses rather a lot from
context and can make mistakes.

%description -l pl
word2x jest programem, który próbuje zrobiæ kompletny, je¿eli nie
doskona³y obraz dokumentu Worda 6. Program opiera siê bardziej na
zgadywaniu z kontekstu i mo¿e robiæ b³êdy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
chmod u+w *
cp -f /usr/share/automake/config.* .
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install word2x rtest2 $RPM_BUILD_ROOT%{_bindir}
install word2x.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INTERNALS
%attr(755, root, root) %{_bindir}/word2x
%attr(755, root, root) %{_bindir}/rtest2
%{_mandir}/man1/word2x.1*
