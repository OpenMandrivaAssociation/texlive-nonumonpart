Name:		texlive-nonumonpart
Version:	22114
Release:	2
Summary:	Prevent page numbers on part pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nonumonpart
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonumonpart.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonumonpart.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonumonpart.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package bundles the answer to the long-standing FAQ about
removing page numbers on \part pages. The package accepts no
options and defines no user commands; the user needs only to
load it, and the requirement is met.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nonumonpart/nonumonpart.sty
%doc %{_texmfdistdir}/doc/latex/nonumonpart/LISEZMOI
%doc %{_texmfdistdir}/doc/latex/nonumonpart/README
%doc %{_texmfdistdir}/doc/latex/nonumonpart/nonumonpart-en.pdf
%doc %{_texmfdistdir}/doc/latex/nonumonpart/nonumonpart-fr.pdf
%doc %{_texmfdistdir}/doc/latex/nonumonpart/nonumonpart.pdf
#- source
%doc %{_texmfdistdir}/source/latex/nonumonpart/Makefile
%doc %{_texmfdistdir}/source/latex/nonumonpart/nonumonpart.dtx
%doc %{_texmfdistdir}/source/latex/nonumonpart/nonumonpart.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
