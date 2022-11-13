Name:		texlive-scalerel
Version:	42809
Release:	1
Summary:	Constrained scaling and stretching of objects
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scalerel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scalerel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scalerel.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides four commands for vertically scaling and
stretching objects. Its primary function is the ability to
scale/stretch and shift one object to conform to the size of a
specified second object. This feature can be useful in both
equations and schematic diagrams. Additionally, the scaling and
stretching commands offer constraints on maximum width and/or
minimum aspect ratio, which are often used to preserve
legibility or for the sake of general appearance.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/scalerel/scalerel.sty
%doc %{_texmfdistdir}/doc/latex/scalerel/README
%doc %{_texmfdistdir}/doc/latex/scalerel/scalerel.pdf
%doc %{_texmfdistdir}/doc/latex/scalerel/scalerel.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
