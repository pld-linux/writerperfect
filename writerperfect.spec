Summary:	Converting WordPerfect(TM) documents into OpenOffice.org formats
Summary(pl.UTF-8):	Konwersja dokumentów WordPerfecta(TM) na formaty OpenOffice.org
Name:		writerperfect
Version:	0.8.1
Release:	1
License:	GPL v2
Group:		Applications/Publishing
Source0:	http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
# Source0-md5:	10b16968406458969348b3ab7b899d5f
URL:		http://libwpd.sourceforge.net/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libgsf-devel >= 1.12.0
BuildRequires:	libstdc++-devel
BuildRequires:	libvisio-devel
BuildRequires:	libwpd-devel >= 0.9.0
BuildRequires:	libwpg-devel >= 0.2.0
BuildRequires:	libwps-devel >= 0.2.0
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libgsf >= 1.12.0
Requires:	libwpd >= 0.9.0
Requires:	libwpg >= 0.2.0
Obsoletes:	wpd2odt
Obsoletes:	wpd2sxw
Obsoletes:	wps2odt
Obsoletes:	wps2sxw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for converting:
- WordPerfect(TM) or MS Works documents into OpenDocument Text format
- WordPerfect Graphics or Microsoft Visio documents into OpenDocument
  Graphics format

%description -l pl.UTF-8
Narzędzia do konwertowania dokumentów:
- WordPerfecta(TM) oraz MS Works do formatu OpenDocument Text
- WordPerfect Graphics oraz Microsoft Visio do OpenDocument Graphics

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/vsd2odg
%attr(755,root,root) %{_bindir}/wpd2odt
%attr(755,root,root) %{_bindir}/wpg2odg
%attr(755,root,root) %{_bindir}/wps2odt
