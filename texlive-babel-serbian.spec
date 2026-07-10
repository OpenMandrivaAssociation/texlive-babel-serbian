%global tl_name babel-serbian
%global tl_revision 64571

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2a
Release:	%{tl_revision}.1
Summary:	Babel/Polyglossia support for Serbian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/serbian
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbian.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for Serbian documents written in Latin, in
babel.

