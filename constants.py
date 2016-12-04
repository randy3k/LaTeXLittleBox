# https://github.com/kpym/SublimeLaTeXAccents/blob/master/latex_accents.py

# to check if it is sorted
# from operator import itemgetter
# sorted(latex_unicode_map, key=itemgetter(0)) == latex_unicode_map

latex_unicode_map = [
    ["$", "\\$"],
    ["&", "\\&"],
    ["¡", "{!`}"],
    ["£", "{\\pounds}"],
    ["§", "{\\S}"],
    ["©", "{\\copyright}"],
    ["±", "{\\pm}"],
    ["¶", "{\\P}"],
    ["·", "{\\cdot}"],
    ["¿", "{?`}"],
    ["À", "\\`{A}"],
    ["À", "\\`A"],
    ["Á", "\\'{A}"],
    ["Á", "\\'A"],
    ["Â", "\\^{A}"],
    ["Â", "\\^A"],
    ["Ã", "\\~{A}"],
    ["Ã", "\\~A"],
    ["Ä", "\\\"{A}"],
    ["Ä", "\\\"A"],
    ["Å", "{\\AA}"],
    ["Å", "\\AA{}"],
    ["Æ", "{\\AE}"],
    ["Æ", "\\AE{}"],
    ["Ç", "\\c{C}"],
    ["È", "\\`{E}"],
    ["È", "\\`E"],
    ["É", "\\'{E}"],
    ["É", "\\'E"],
    ["Ê", "\\^{E}"],
    ["Ê", "\\^E"],
    ["Ë", "\\\"{E}"],
    ["Ë", "\\\"E"],
    ["Ì", "\\`{I}"],
    ["Ì", "\\`I"],
    ["Í", "\\'{I}"],
    ["Í", "\\'I"],
    ["Î", "\\^{I}"],
    ["Î", "\\^I"],
    ["Ï", "\\\"{I}"],
    ["Ï", "\\\"I"],
    ["Ñ", "\\~{N}"],
    ["Ñ", "\\~N"],
    ["Ò", "\\`{O}"],
    ["Ò", "\\`O"],
    ["Ó", "\\'{O}"],
    ["Ó", "\\'O"],
    ["Ô", "\\^{O}"],
    ["Ô", "\\^O"],
    ["Õ", "\\~{O}"],
    ["Õ", "\\~O"],
    ["Ö", "\\\"{O}"],
    ["Ö", "\\\"O"],
    ["×", "{\\times}"],
    ["Ø", "{\\O}"],
    ["Ø", "\\O{}"],
    ["Ù", "\\`{U}"],
    ["Ù", "\\`U"],
    ["Ú", "\\'{U}"],
    ["Ú", "\\'U"],
    ["Û", "\\^{U}"],
    ["Û", "\\^U"],
    ["Ü", "\\\"{U}"],
    ["Ü", "\\\"U"],
    ["Ý", "\\'{Y}"],
    ["Ý", "\\'Y"],
    ["ß", "{\\ss}"],
    ["ß", "\\ss{}"],
    ["à", "\\`{a}"],
    ["à", "\\`a"],
    ["á", "\\'{a}"],
    ["á", "\\'a"],
    ["â", "\\^{a}"],
    ["â", "\\^a"],
    ["ã", "\\~{a}"],
    ["ã", "\\~a"],
    ["ä", "\\\"{a}"],
    ["ä", "\\\"a"],
    ["å", "{\\aa}"],
    ["å", "\\aa{}"],
    ["æ", "{\\ae}"],
    ["æ", "\\ae{}"],
    ["ç", "\\c{c}"],
    ["è", "\\`{e}"],
    ["è", "\\`e"],
    ["é", "\\'{e}"],
    ["é", "\\'e"],
    ["ê", "\\^{e}"],
    ["ê", "\\^e"],
    ["ë", "\\\"{e}"],
    ["ë", "\\\"e"],
    ["ì", "\\`{i}"],
    ["ì", "\\`i"],
    ["ì", "\\`{\\i}"],
    ["ì", "\\`\\i"],
    ["í", "\\'{i}"],
    ["í", "\\'i"],
    ["í", "\\'{\\i}"],
    ["í", "\\'\\i"],
    ["î", "\\^{i}"],
    ["î", "\\^i"],
    ["î", "\\^{\\i}"],
    ["î", "\\^\\i"],
    ["ï", "\\\"{i}"],
    ["ï", "\\\"i"],
    ["ï", "\\\"{\\i}"],
    ["ï", "\\\"\\i"],
    ["ñ", "\\~{n}"],
    ["ñ", "\\~n"],
    ["ò", "\\`{o}"],
    ["ò", "\\`o"],
    ["ó", "\\'{o}"],
    ["ó", "\\'o"],
    ["ô", "\\^{o}"],
    ["ô", "\\^o"],
    ["õ", "\\~{o}"],
    ["õ", "\\~o"],
    ["ö", "\\\"{o}"],
    ["ö", "\\\"o"],
    ["÷", "{\\div}"],
    ["ø", "{\\o}"],
    ["ø", "\\o{}"],
    ["ù", "\\`{u}"],
    ["ù", "\\`u"],
    ["ú", "\\'{u}"],
    ["ú", "\\'u"],
    ["û", "\\^{u}"],
    ["û", "\\^u"],
    ["ü", "\\\"{u}"],
    ["ü", "\\\"u"],
    ["ý", "\\'{y}"],
    ["ý", "\\'y"],
    ["ÿ", "\\\"{y}"],
    ["ÿ", "\\\"y"],
    ["Ą", "\\k{A}"],
    ["ą", "\\k{a}"],
    ["Ę", "\\k{E}"],
    ["ę", "\\k{e}"],
    ["Į", "\\k{I}"],
    ["į", "\\k{i}"],
    ["Ő", "\\H{O}"],
    ["ő", "\\H{o}"],
    ["Œ", "{\\OE}"],
    ["Œ", "\\OE{}"],
    ["œ", "{\\oe}"],
    ["œ", "\\oe{}"],
    ["Ř", "\\v{R}"],
    ["ř", "\\v{r}"],
    ["Š", "\\v{S}"],
    ["š", "\\v{s}"],
    ["Ű", "\\H{U}"],
    ["ű", "\\H{u}"],
    ["Ų", "\\k{U}"],
    ["ų", "\\k{u}"],
    ["Ÿ", "\\\"{Y}"],
    ["Ÿ", "\\\"Y"],
    ["Ž", "\\v{Z}"],
    ["ž", "\\v{z}"]
]

math_commands = [
    ("\\alpha", ),
    ("\\beta", ),
    ("\\gamma", ),
    ("\\delta", ),
    ("\\epsilon", ),
    ("\\varepsilon", ),
    ("\\zeta", ),
    ("\\eta", ),
    ("\\theta", ),
    ("\\vartheta", ),
    ("\\iota", ),
    ("\\kappa", ),
    ("\\lambda", ),
    ("\\mu", ),
    ("\\nu", ),
    ("\\xi", ),
    ("\\pi", ),
    ("\\rho", ),
    ("\\sigma", ),
    ("\\tau", ),
    ("\\upsilon", ),
    ("\\phi", ),
    ("\\varphi", ),
    ("\\chi", ),
    ("\\psi", ),
    ("\\omega", ),
    ("\\digamma", ),
    ("\\Gamma", ),
    ("\\Delta", ),
    ("\\Theta", ),
    ("\\Lambda", ),
    ("\\Xi", ),
    ("\\Pi", ),
    ("\\Sigma", ),
    ("\\Phi", ),
    ("\\Psi", ),
    ("\\Omega", ),

    ("\\infty", ),
    ("\\varnothing", ),

    ("\\quad", ),
    ("\\qquad", ),

    ("\\bigcup", ),
    ("\\bigcap", ),
    ("\\langle", ),
    ("\\rangle", ),
    ("\\bigcup", ),
    ("\\bigcap", ),

    ("\\leftarrow", ),
    ("\\longleftarrow", ),
    ("\\Leftarrow", ),
    ("\\Longleftarrow", ),
    ("\\rightarrow", ),
    ("\\longrightarrow", ),
    ("\\Rightarrow", ),
    ("\\Longrightarrow", ),
    ("\\leftrightarrow", ),
    ("\\longleftrightarrow", ),
    ("\\Leftrightarrow", ),
    ("\\Longleftrightarrow", ),
    ("\\uparrow", ),
    ("\\downarrow", ),

    ("\\mathit", ),
    ("\\mathbf", ),
    ("\\mathbb", ),
    ("\\mathrm", ),
    ("\\mathsf", ),
    ("\\mathcal", ),

    ("\\partial", ),

    ("\\sum_{}^{}", "sum_{$1}^{$2}$0"),
    ("\\prod_{}^{}", "prod_{$1}^{$2}$0"),
    ("\\int_{}^{}", "int_{$1}^{$2}$0"),
    ("\\frac{}{}", "frac{$1}{$2}$0"),
    ("\\overset{}{}", "overset{$1}{$2}$0"),
    ("\\overbrace{}{}", "overbrace{$1}{$2}$0"),
    ("\\underset{}{}", "underset{$1}{$2}$0"),
    ("\\underbrace{}{}", "underbrace{$1}{$2}$0"),

    ("\\binom{}{}", "binom{$1}{$2}$0"),
    ("\\text{}", "text{$1}$0")
]

general_commands = [
    ("\\usagepacage", ),
    ("\\includegraphics", ),
    ("\\part{}", "part{$1}"),
    ("\\part*{}", "part*{$1}"),
    ("\\chapter{}", "chapter{$1}"),
    ("\\chapter*{}", "chapter*{$1}"),
    ("\\section{}", "section{$1}"),
    ("\\section*{}", "section*{$1}"),
    ("\\subsection{}", "subsection{$1}"),
    ("\\subsection*{}", "subsection*{$1}"),

    ("\\underline{}", "underline{$1}"),
    ("\\textbf{}", "textbf{$1}"),
    ("\\texttt{}", "texttt{$1}"),
    ("\\textit{}", "textit{$1}"),

    ("\\bibliographystyle{}", "bibliographystyle{$1}"),
    ("\\bibliography{}", "bibliography{$1}"),
    ("\\addbibresource{}", "addbibresource{$1}")
]


arrow_map = {
    "<-": "\\leftarrow",
    "<--": "\\longleftarrow",
    "->": "\\rightarrow",
    "-->": "\\longrightarrow",
    "<->": "\\leftrightarrow",
    "<-->": "\\longleftrightarrow",
    "<=": "\\Leftarrow",
    "<==": "\\Longleftarrow",
    "=>": "\\Rightarrow",
    "==>": "\\Longrightarrow",
    "<=>": "\\Leftrightarrow",
    "<==>": "\\Longleftrightarrow"
}
