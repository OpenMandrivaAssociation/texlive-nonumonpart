%global tl_name nonumonpart
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	Prevent page numbers on part pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nonumonpart
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nonumonpart.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nonumonpart.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nonumonpart.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package bundles the answer to the long-standing FAQ about removing
page numbers on \part pages. The package accepts no options and defines
no user commands; the user needs only to load it, and the requirement is
met.

