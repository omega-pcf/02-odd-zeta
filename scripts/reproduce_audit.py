#!/usr/bin/env python3
import os
import re
import subprocess
import shutil
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = PROJECT_ROOT / "src"
CHAPTERS_DIR = SRC_DIR / "chapters"
TMP_DIR = PROJECT_ROOT / "tmp"
MAIN_TEX = PROJECT_ROOT / "main.tex"
UNIFIED_TEX = TMP_DIR / "manuscript_unified.tex"
BIB_FILE = SRC_DIR / "bibliography.bib"

# Audit target (original author draft)
ORIGINAL_MANUSCRIPT = Path("/home/aficio/Downloads/odd_zeta_manuscript_final.tex")
DIFF_HTML = TMP_DIR / "manuscript_diff.html"
DIFF_TXT = TMP_DIR / "manuscript_diff.txt"

PREAMBLE_MAPPING = r"""\documentclass[11pt,fleqn]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amsthm}
\usepackage{mathtools}
\usepackage{amssymb}
\usepackage{tikz-cd}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{array}
\usepackage{graphicx}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage[capitalize,nameinlink]{cleveref}
\usepackage{setspace}
\usepackage{geometry}
\geometry{margin=1in}

% Sigma class emulators
\newcommand{\Abstract}[1]{\begin{abstract} #1 \end{abstract}}
\newcommand{\Keywords}[1]{\par\vspace{1em}\noindent\textbf{Keywords:} #1}
\newcommand{\Classification}[1]{\par\vspace{0.5em}\noindent\textbf{AMS Classification:} #1}
\newcommand{\ShortArticleName}[1]{}
\newcommand{\ArticleName}[1]{\title{#1}}
\newcommand{\Author}[1]{\author{#1}}
\newcommand{\AuthorNameForHeading}[1]{}
\newcommand{\Address}[1]{\date{#1}}
\newcommand{\EmailD}[1]{}
\newcommand{\ArticleDates}[1]{\date{#1}}
\newcommand{\LastPageEnding}{}
\newcommand{\FirstPageHeading}{}
\newcommand{\PaperNumber}[1]{}
\newcommand{\mail}[1]{\href{mailto:#1}{#1}}

% Theorems for article class
\newtheorem{Theorem}{Theorem}[section]
\newtheorem*{Theorem*}{Theorem}
\newtheorem{Corollary}[Theorem]{Corollary}
\newtheorem{Lemma}[Theorem]{Lemma}
\newtheorem{Proposition}[Theorem]{Proposition}
\newtheorem{Conjecture}[Theorem]{Conjecture}
\newtheorem{Observation}[Theorem]{Observation}

\theoremstyle{definition}
\newtheorem{Definition}[Theorem]{Definition}
\newtheorem{Note}[Theorem]{Note}
\newtheorem{Example}[Theorem]{Example}
\newtheorem{Remark}[Theorem]{Remark}
% Missing environments from the monolithic source
\newtheorem{openproblem}[Theorem]{Open Problem}

% Custom macros extracted from main.tex
"""

def extract_custom_macros(main_tex_path):
    macros = []
    with open(main_tex_path, "r", encoding="utf-8") as f:
        in_custom_section = False
        for line in f:
            if "CUSTOM COMMANDS" in line:
                in_custom_section = True
                continue
            if in_custom_section and line.startswith("\\newcommand"):
                macros.append(line.strip())
            if in_custom_section and line.strip() == "":
                continue
            if in_custom_section and line.startswith("%%%"):
                if "PREPRINT CUSTOMIZATION" in line:
                    in_custom_section = False
    return "\n".join(macros)

def get_chapter_order(main_tex_path):
    chapters = []
    with open(main_tex_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Look for \input{src/chapters/...} or \input{chapters/...}
            match = re.search(r'\\input\{([^}]+)\}', line)
            if match and not line.startswith("%"):
                chapters.append(match.group(1))
    return chapters

def get_file_content(relative_path):
    bases = [PROJECT_ROOT, SRC_DIR, CHAPTERS_DIR]
    
    path = None
    for base in bases:
        test_path = base / relative_path
        if not test_path.suffix:
            test_path = test_path.with_suffix(".tex")
        if test_path.exists():
            path = test_path
            break
            
    if not path or not path.exists():
        print(f"Warning: File {relative_path} not found")
        return f"\n%% MISSING FILE: {relative_path}\n"
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace("src/images/", "../images/")
    return content

def generate_unified():
    TMP_DIR.mkdir(exist_ok=True)
    
    custom_macros = extract_custom_macros(MAIN_TEX)
    chapters = get_chapter_order(MAIN_TEX)
    
    full_latex = PREAMBLE_MAPPING
    full_latex += custom_macros
    full_latex += "\n\n\\begin{document}\n\\maketitle\n\n\\tableofcontents\n\\newpage\n"
    
    for chapter in chapters:
        full_latex += f"\n%% ================= FILE: {chapter} =================\n"
        full_latex += get_file_content(chapter)
        full_latex += "\n"
    
    if BIB_FILE.exists():
        shutil.copy2(BIB_FILE, TMP_DIR / "bibliography.bib")
        full_latex += r"""
\bibliographystyle{plain}
\bibliography{bibliography}
"""
    
    full_latex += "\n\\end{document}\n"
    
    with open(UNIFIED_TEX, "w", encoding="utf-8") as f:
        f.write(full_latex)
    
    print(f"✅ Unified TeX generated at {UNIFIED_TEX}")

def run_diff():
    if not ORIGINAL_MANUSCRIPT.exists():
        print(f"❌ Error: Original manuscript not found at {ORIGINAL_MANUSCRIPT}")
        return

    print("🔍 Generating diff reports...")
    
    cmd_html = [
        "git", "diff", "--no-index", "--color=always", "--histogram", "-w",
        "--color-moved=zebra", str(ORIGINAL_MANUSCRIPT), str(UNIFIED_TEX)
    ]
    
    try:
        res = subprocess.run(cmd_html, capture_output=True)
        aha_res = subprocess.run(["aha", "--black", "--title", "Manuscript Progress Diff"], 
                                 input=res.stdout, capture_output=True)
        with open(DIFF_HTML, "wb") as f:
            f.write(aha_res.stdout)
        print(f"✅ Visual HTML diff saved to {DIFF_HTML}")
    except Exception as e:
        print(f"⚠️ Failed to generate HTML diff: {e}")

    cmd_txt = [
        "git", "diff", "--no-index", "--histogram", "-w",
        str(ORIGINAL_MANUSCRIPT), str(UNIFIED_TEX)
    ]
    try:
        res = subprocess.run(cmd_txt, capture_output=True, text=True)
        with open(DIFF_TXT, "w", encoding="utf-8") as f:
            f.write(res.stdout)
        print(f"✅ Plain text diff saved to {DIFF_TXT}")
    except Exception as e:
        print(f"⚠️ Failed to generate text diff: {e}")

if __name__ == "__main__":
    generate_unified()
    run_diff()
