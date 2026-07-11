%global tl_name scalerel
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8
Release:	%{tl_revision}.1
Summary:	Constrained scaling and stretching of objects
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scalerel
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scalerel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scalerel.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides four commands for vertically scaling and stretching
objects. Its primary function is the ability to scale/stretch and shift
one object to conform to the size of a specified second object. This
feature can be useful in both equations and schematic diagrams.
Additionally, the scaling and stretching commands offer constraints on
maximum width and/or minimum aspect ratio, which are often used to
preserve legibility or for the sake of general appearance.

