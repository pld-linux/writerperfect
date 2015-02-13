Summary:	Converting WordPerfect(TM) documents into OpenOffice.org formats
Summary(pl.UTF-8):	Konwersja dokumentów WordPerfecta(TM) na formaty OpenOffice.org
Name:		writerperfect
Version:	0.9.2
Release:	1
License:	GPL v2
Group:		Applications/Publishing
Source0:	http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
# Source0-md5:	2ae8b25f99054964a968e0a908475840
URL:		http://libwpd.sourceforge.net/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libabw-devel >= 0.1
BuildRequires:	libcdr-devel >= 0.1
BuildRequires:	libe-book-devel >= 0.1
BuildRequires:	libepubgen-devel >= 0.0
BuildRequires:	libetonyek-devel >= 0.1
BuildRequires:	libfreehand-devel >= 0.1
BuildRequires:	libgsf-devel >= 1.12.0
BuildRequires:	libmspub-devel >= 0.1
BuildRequires:	libmwaw-devel >= 0.3
BuildRequires:	libodfgen-devel >= 0.1
BuildRequires:	libpagemaker-devel >= 0.0
BuildRequires:	librevenge-devel >= 0.0.1
BuildRequires:	libstdc++-devel >= 6:4.3
BuildRequires:	libvisio-devel >= 0.1
BuildRequires:	libwpd-devel >= 0.10
BuildRequires:	libwpg-devel >= 0.3
BuildRequires:	libwps-devel >= 0.3
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libabw >= 0.1
Requires:	libcdr >= 0.1
Requires:	libe-book >= 0.1
Requires:	libetonyek >= 0.1
Requires:	libfreehand >= 0.1
Requires:	libgsf >= 1.12.0
Requires:	libmspub >= 0.1
Requires:	libmwaw >= 0.3
Requires:	libodfgen >= 0.1
Requires:	librevenge >= 0.0.1
Requires:	libvisio >= 0.1
Requires:	libwpd >= 0.10
Requires:	libwpg >= 0.3
Requires:	libwps >= 0.3
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
CXXFLAGS="%{rpmcxxflags} -std=c++0x"
%configure \
	--disable-silent-rules \
	--with-libgsf \
	--with-sharedptr=c++11
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
%attr(755,root,root) %{_bindir}/abw2epub
%attr(755,root,root) %{_bindir}/abw2odt
%attr(755,root,root) %{_bindir}/cdr2epub
%attr(755,root,root) %{_bindir}/cdr2odg
%attr(755,root,root) %{_bindir}/cmx2epub
%attr(755,root,root) %{_bindir}/cmx2odg
%attr(755,root,root) %{_bindir}/ebook2epub
%attr(755,root,root) %{_bindir}/ebook2odt
%attr(755,root,root) %{_bindir}/fh2epub
%attr(755,root,root) %{_bindir}/fh2odg
%attr(755,root,root) %{_bindir}/key2epub
%attr(755,root,root) %{_bindir}/key2odp
%attr(755,root,root) %{_bindir}/mwaw2epub
%attr(755,root,root) %{_bindir}/mwaw2odf
%attr(755,root,root) %{_bindir}/pages2epub
%attr(755,root,root) %{_bindir}/pages2odt
%attr(755,root,root) %{_bindir}/pmd2epub
%attr(755,root,root) %{_bindir}/pmd2odg
%attr(755,root,root) %{_bindir}/pub2epub
%attr(755,root,root) %{_bindir}/pub2odg
%attr(755,root,root) %{_bindir}/vsd2epub
%attr(755,root,root) %{_bindir}/vsd2odg
%attr(755,root,root) %{_bindir}/vss2epub
%attr(755,root,root) %{_bindir}/vss2odg
%attr(755,root,root) %{_bindir}/wks2ods
%attr(755,root,root) %{_bindir}/wpd2epub
%attr(755,root,root) %{_bindir}/wpd2odt
%attr(755,root,root) %{_bindir}/wpg2epub
%attr(755,root,root) %{_bindir}/wpg2odg
%attr(755,root,root) %{_bindir}/wps2epub
%attr(755,root,root) %{_bindir}/wps2odt
