Name:		texlive-babel-serbian
Version:	64571
Release:	1
Summary:	TeXLive babel-serbian package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbian.r64571.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbian.doc.r64571.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbian.source.r64571.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-serbian package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-serbian
%doc %{_texmfdistdir}/doc/generic/babel-serbian
#- source
%doc %{_texmfdistdir}/source/generic/babel-serbian

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
