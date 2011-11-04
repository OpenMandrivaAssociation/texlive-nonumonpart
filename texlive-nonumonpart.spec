# revision 22114
# category Package
# catalog-ctan /macros/latex/contrib/nonumonpart
# catalog-date 2011-04-15 12:43:28 +0200
# catalog-license lppl1.2
# catalog-version 1
Name:		texlive-nonumonpart
Version:	1
Release:	1
Summary:	Prevent page numbers on part pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nonumonpart
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonumonpart.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonumonpart.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonumonpart.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package bundles the answer to the long-standing FAQ about
removing page numbers on \part pages. The package accepts no
options and defines no user commands; the user needs only to
load it, and the requirement is met.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
