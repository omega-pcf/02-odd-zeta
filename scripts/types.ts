/* eslint-disable */
/** This file was automatically generated from official JSON schemas. DO NOT MODIFY BY HAND. **/

/**
 * The (e.g., Git) commit hash or (e.g., Subversion) revision number of the work.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "commit".
 */
export type Commit = string;
/**
 * The DOI of the work (i.e., 10.5281/zenodo.1003150, not the resolver URL http://doi.org/10.5281/zenodo.1003150).
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "doi".
 */
export type Doi = string;
/**
 * An identifier for a work.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "identifier".
 */
export type Identifier =
  | {
      description?: IdentifierDescription;
      type: 'doi';
      value: Doi;
    }
  | {
      description?: IdentifierDescription;
      type: 'url';
      value: Url;
    }
  | {
      description?: IdentifierDescription;
      type: 'swh';
      value: SwhIdentifier;
    }
  | {
      description?: IdentifierDescription;
      type: 'other';
      value: string;
    };
/**
 * A description for a specific identifier value.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "identifier-description".
 */
export type IdentifierDescription = string;
/**
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "url".
 */
export type Url = string;
/**
 * The Software Heritage identifier (without further qualifiers such as origin, visit, anchor, path).
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "swh-identifier".
 */
export type SwhIdentifier = string;
/**
 * An SPDX license identifier.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "license".
 */
export type License =
  | (
      | '0BSD'
      | 'AAL'
      | 'Abstyles'
      | 'Adobe-2006'
      | 'Adobe-Glyph'
      | 'ADSL'
      | 'AFL-1.1'
      | 'AFL-1.2'
      | 'AFL-2.0'
      | 'AFL-2.1'
      | 'AFL-3.0'
      | 'Afmparse'
      | 'AGPL-1.0'
      | 'AGPL-1.0-only'
      | 'AGPL-1.0-or-later'
      | 'AGPL-3.0'
      | 'AGPL-3.0-only'
      | 'AGPL-3.0-or-later'
      | 'Aladdin'
      | 'AMDPLPA'
      | 'AML'
      | 'AMPAS'
      | 'ANTLR-PD'
      | 'ANTLR-PD-fallback'
      | 'Apache-1.0'
      | 'Apache-1.1'
      | 'Apache-2.0'
      | 'APAFML'
      | 'APL-1.0'
      | 'APSL-1.0'
      | 'APSL-1.1'
      | 'APSL-1.2'
      | 'APSL-2.0'
      | 'Artistic-1.0'
      | 'Artistic-1.0-cl8'
      | 'Artistic-1.0-Perl'
      | 'Artistic-2.0'
      | 'Bahyph'
      | 'Barr'
      | 'Beerware'
      | 'BitTorrent-1.0'
      | 'BitTorrent-1.1'
      | 'blessing'
      | 'BlueOak-1.0.0'
      | 'Borceux'
      | 'BSD-1-Clause'
      | 'BSD-2-Clause'
      | 'BSD-2-Clause-FreeBSD'
      | 'BSD-2-Clause-NetBSD'
      | 'BSD-2-Clause-Patent'
      | 'BSD-2-Clause-Views'
      | 'BSD-3-Clause'
      | 'BSD-3-Clause-Attribution'
      | 'BSD-3-Clause-Clear'
      | 'BSD-3-Clause-LBNL'
      | 'BSD-3-Clause-Modification'
      | 'BSD-3-Clause-No-Nuclear-License'
      | 'BSD-3-Clause-No-Nuclear-License-2014'
      | 'BSD-3-Clause-No-Nuclear-Warranty'
      | 'BSD-3-Clause-Open-MPI'
      | 'BSD-4-Clause'
      | 'BSD-4-Clause-Shortened'
      | 'BSD-4-Clause-UC'
      | 'BSD-Protection'
      | 'BSD-Source-Code'
      | 'BSL-1.0'
      | 'BUSL-1.1'
      | 'bzip2-1.0.5'
      | 'bzip2-1.0.6'
      | 'C-UDA-1.0'
      | 'CAL-1.0'
      | 'CAL-1.0-Combined-Work-Exception'
      | 'Caldera'
      | 'CATOSL-1.1'
      | 'CC-BY-1.0'
      | 'CC-BY-2.0'
      | 'CC-BY-2.5'
      | 'CC-BY-3.0'
      | 'CC-BY-3.0-AT'
      | 'CC-BY-3.0-US'
      | 'CC-BY-4.0'
      | 'CC-BY-NC-1.0'
      | 'CC-BY-NC-2.0'
      | 'CC-BY-NC-2.5'
      | 'CC-BY-NC-3.0'
      | 'CC-BY-NC-4.0'
      | 'CC-BY-NC-ND-1.0'
      | 'CC-BY-NC-ND-2.0'
      | 'CC-BY-NC-ND-2.5'
      | 'CC-BY-NC-ND-3.0'
      | 'CC-BY-NC-ND-3.0-IGO'
      | 'CC-BY-NC-ND-4.0'
      | 'CC-BY-NC-SA-1.0'
      | 'CC-BY-NC-SA-2.0'
      | 'CC-BY-NC-SA-2.5'
      | 'CC-BY-NC-SA-3.0'
      | 'CC-BY-NC-SA-4.0'
      | 'CC-BY-ND-1.0'
      | 'CC-BY-ND-2.0'
      | 'CC-BY-ND-2.5'
      | 'CC-BY-ND-3.0'
      | 'CC-BY-ND-4.0'
      | 'CC-BY-SA-1.0'
      | 'CC-BY-SA-2.0'
      | 'CC-BY-SA-2.0-UK'
      | 'CC-BY-SA-2.1-JP'
      | 'CC-BY-SA-2.5'
      | 'CC-BY-SA-3.0'
      | 'CC-BY-SA-3.0-AT'
      | 'CC-BY-SA-4.0'
      | 'CC-PDDC'
      | 'CC0-1.0'
      | 'CDDL-1.0'
      | 'CDDL-1.1'
      | 'CDL-1.0'
      | 'CDLA-Permissive-1.0'
      | 'CDLA-Sharing-1.0'
      | 'CECILL-1.0'
      | 'CECILL-1.1'
      | 'CECILL-2.0'
      | 'CECILL-2.1'
      | 'CECILL-B'
      | 'CECILL-C'
      | 'CERN-OHL-1.1'
      | 'CERN-OHL-1.2'
      | 'CERN-OHL-P-2.0'
      | 'CERN-OHL-S-2.0'
      | 'CERN-OHL-W-2.0'
      | 'ClArtistic'
      | 'CNRI-Jython'
      | 'CNRI-Python'
      | 'CNRI-Python-GPL-Compatible'
      | 'Condor-1.1'
      | 'copyleft-next-0.3.0'
      | 'copyleft-next-0.3.1'
      | 'CPAL-1.0'
      | 'CPL-1.0'
      | 'CPOL-1.02'
      | 'Crossword'
      | 'CrystalStacker'
      | 'CUA-OPL-1.0'
      | 'Cube'
      | 'curl'
      | 'D-FSL-1.0'
      | 'diffmark'
      | 'DOC'
      | 'Dotseqn'
      | 'DRL-1.0'
      | 'DSDP'
      | 'dvipdfm'
      | 'ECL-1.0'
      | 'ECL-2.0'
      | 'eCos-2.0'
      | 'EFL-1.0'
      | 'EFL-2.0'
      | 'eGenix'
      | 'Entessa'
      | 'EPICS'
      | 'EPL-1.0'
      | 'EPL-2.0'
      | 'ErlPL-1.1'
      | 'etalab-2.0'
      | 'EUDatagrid'
      | 'EUPL-1.0'
      | 'EUPL-1.1'
      | 'EUPL-1.2'
      | 'Eurosym'
      | 'Fair'
      | 'Frameworx-1.0'
      | 'FreeBSD-DOC'
      | 'FreeImage'
      | 'FSFAP'
      | 'FSFUL'
      | 'FSFULLR'
      | 'FTL'
      | 'GD'
      | 'GFDL-1.1'
      | 'GFDL-1.1-invariants-only'
      | 'GFDL-1.1-invariants-or-later'
      | 'GFDL-1.1-no-invariants-only'
      | 'GFDL-1.1-no-invariants-or-later'
      | 'GFDL-1.1-only'
      | 'GFDL-1.1-or-later'
      | 'GFDL-1.2'
      | 'GFDL-1.2-invariants-only'
      | 'GFDL-1.2-invariants-or-later'
      | 'GFDL-1.2-no-invariants-only'
      | 'GFDL-1.2-no-invariants-or-later'
      | 'GFDL-1.2-only'
      | 'GFDL-1.2-or-later'
      | 'GFDL-1.3'
      | 'GFDL-1.3-invariants-only'
      | 'GFDL-1.3-invariants-or-later'
      | 'GFDL-1.3-no-invariants-only'
      | 'GFDL-1.3-no-invariants-or-later'
      | 'GFDL-1.3-only'
      | 'GFDL-1.3-or-later'
      | 'Giftware'
      | 'GL2PS'
      | 'Glide'
      | 'Glulxe'
      | 'GLWTPL'
      | 'gnuplot'
      | 'GPL-1.0'
      | 'GPL-1.0-only'
      | 'GPL-1.0-or-later'
      | 'GPL-1.0+'
      | 'GPL-2.0'
      | 'GPL-2.0-only'
      | 'GPL-2.0-or-later'
      | 'GPL-2.0-with-autoconf-exception'
      | 'GPL-2.0-with-bison-exception'
      | 'GPL-2.0-with-classpath-exception'
      | 'GPL-2.0-with-font-exception'
      | 'GPL-2.0-with-GCC-exception'
      | 'GPL-2.0+'
      | 'GPL-3.0'
      | 'GPL-3.0-only'
      | 'GPL-3.0-or-later'
      | 'GPL-3.0-with-autoconf-exception'
      | 'GPL-3.0-with-GCC-exception'
      | 'GPL-3.0+'
      | 'gSOAP-1.3b'
      | 'HaskellReport'
      | 'Hippocratic-2.1'
      | 'HPND'
      | 'HPND-sell-variant'
      | 'HTMLTIDY'
      | 'IBM-pibs'
      | 'ICU'
      | 'IJG'
      | 'ImageMagick'
      | 'iMatix'
      | 'Imlib2'
      | 'Info-ZIP'
      | 'Intel'
      | 'Intel-ACPI'
      | 'Interbase-1.0'
      | 'IPA'
      | 'IPL-1.0'
      | 'ISC'
      | 'JasPer-2.0'
      | 'JPNIC'
      | 'JSON'
      | 'LAL-1.2'
      | 'LAL-1.3'
      | 'Latex2e'
      | 'Leptonica'
      | 'LGPL-2.0'
      | 'LGPL-2.0-only'
      | 'LGPL-2.0-or-later'
      | 'LGPL-2.0+'
      | 'LGPL-2.1'
      | 'LGPL-2.1-only'
      | 'LGPL-2.1-or-later'
      | 'LGPL-2.1+'
      | 'LGPL-3.0'
      | 'LGPL-3.0-only'
      | 'LGPL-3.0-or-later'
      | 'LGPL-3.0+'
      | 'LGPLLR'
      | 'Libpng'
      | 'libpng-2.0'
      | 'libselinux-1.0'
      | 'libtiff'
      | 'LiLiQ-P-1.1'
      | 'LiLiQ-R-1.1'
      | 'LiLiQ-Rplus-1.1'
      | 'Linux-OpenIB'
      | 'LPL-1.0'
      | 'LPL-1.02'
      | 'LPPL-1.0'
      | 'LPPL-1.1'
      | 'LPPL-1.2'
      | 'LPPL-1.3a'
      | 'LPPL-1.3c'
      | 'MakeIndex'
      | 'MirOS'
      | 'MIT'
      | 'MIT-0'
      | 'MIT-advertising'
      | 'MIT-CMU'
      | 'MIT-enna'
      | 'MIT-feh'
      | 'MIT-Modern-Variant'
      | 'MIT-open-group'
      | 'MITNFA'
      | 'Motosoto'
      | 'mpich2'
      | 'MPL-1.0'
      | 'MPL-1.1'
      | 'MPL-2.0'
      | 'MPL-2.0-no-copyleft-exception'
      | 'MS-PL'
      | 'MS-RL'
      | 'MTLL'
      | 'MulanPSL-1.0'
      | 'MulanPSL-2.0'
      | 'Multics'
      | 'Mup'
      | 'NAIST-2003'
      | 'NASA-1.3'
      | 'Naumen'
      | 'NBPL-1.0'
      | 'NCGL-UK-2.0'
      | 'NCSA'
      | 'Net-SNMP'
      | 'NetCDF'
      | 'Newsletr'
      | 'NGPL'
      | 'NIST-PD'
      | 'NIST-PD-fallback'
      | 'NLOD-1.0'
      | 'NLPL'
      | 'Nokia'
      | 'NOSL'
      | 'Noweb'
      | 'NPL-1.0'
      | 'NPL-1.1'
      | 'NPOSL-3.0'
      | 'NRL'
      | 'NTP'
      | 'NTP-0'
      | 'Nunit'
      | 'O-UDA-1.0'
      | 'OCCT-PL'
      | 'OCLC-2.0'
      | 'ODbL-1.0'
      | 'ODC-By-1.0'
      | 'OFL-1.0'
      | 'OFL-1.0-no-RFN'
      | 'OFL-1.0-RFN'
      | 'OFL-1.1'
      | 'OFL-1.1-no-RFN'
      | 'OFL-1.1-RFN'
      | 'OGC-1.0'
      | 'OGDL-Taiwan-1.0'
      | 'OGL-Canada-2.0'
      | 'OGL-UK-1.0'
      | 'OGL-UK-2.0'
      | 'OGL-UK-3.0'
      | 'OGTSL'
      | 'OLDAP-1.1'
      | 'OLDAP-1.2'
      | 'OLDAP-1.3'
      | 'OLDAP-1.4'
      | 'OLDAP-2.0'
      | 'OLDAP-2.0.1'
      | 'OLDAP-2.1'
      | 'OLDAP-2.2'
      | 'OLDAP-2.2.1'
      | 'OLDAP-2.2.2'
      | 'OLDAP-2.3'
      | 'OLDAP-2.4'
      | 'OLDAP-2.5'
      | 'OLDAP-2.6'
      | 'OLDAP-2.7'
      | 'OLDAP-2.8'
      | 'OML'
      | 'OpenSSL'
      | 'OPL-1.0'
      | 'OSET-PL-2.1'
      | 'OSL-1.0'
      | 'OSL-1.1'
      | 'OSL-2.0'
      | 'OSL-2.1'
      | 'OSL-3.0'
      | 'Parity-6.0.0'
      | 'Parity-7.0.0'
      | 'PDDL-1.0'
      | 'PHP-3.0'
      | 'PHP-3.01'
      | 'Plexus'
      | 'PolyForm-Noncommercial-1.0.0'
      | 'PolyForm-Small-Business-1.0.0'
      | 'PostgreSQL'
      | 'PSF-2.0'
      | 'psfrag'
      | 'psutils'
      | 'Python-2.0'
      | 'Qhull'
      | 'QPL-1.0'
      | 'Rdisc'
      | 'RHeCos-1.1'
      | 'RPL-1.1'
      | 'RPL-1.5'
      | 'RPSL-1.0'
      | 'RSA-MD'
      | 'RSCPL'
      | 'Ruby'
      | 'SAX-PD'
      | 'Saxpath'
      | 'SCEA'
      | 'Sendmail'
      | 'Sendmail-8.23'
      | 'SGI-B-1.0'
      | 'SGI-B-1.1'
      | 'SGI-B-2.0'
      | 'SHL-0.5'
      | 'SHL-0.51'
      | 'SimPL-2.0'
      | 'SISSL'
      | 'SISSL-1.2'
      | 'Sleepycat'
      | 'SMLNJ'
      | 'SMPPL'
      | 'SNIA'
      | 'Spencer-86'
      | 'Spencer-94'
      | 'Spencer-99'
      | 'SPL-1.0'
      | 'SSH-OpenSSH'
      | 'SSH-short'
      | 'SSPL-1.0'
      | 'StandardML-NJ'
      | 'SugarCRM-1.1.3'
      | 'SWL'
      | 'TAPR-OHL-1.0'
      | 'TCL'
      | 'TCP-wrappers'
      | 'TMate'
      | 'TORQUE-1.1'
      | 'TOSL'
      | 'TU-Berlin-1.0'
      | 'TU-Berlin-2.0'
      | 'UCL-1.0'
      | 'Unicode-DFS-2015'
      | 'Unicode-DFS-2016'
      | 'Unicode-TOU'
      | 'Unlicense'
      | 'UPL-1.0'
      | 'Vim'
      | 'VOSTROM'
      | 'VSL-1.0'
      | 'W3C'
      | 'W3C-19980720'
      | 'W3C-20150513'
      | 'Watcom-1.0'
      | 'Wsuipa'
      | 'WTFPL'
      | 'wxWindows'
      | 'X11'
      | 'Xerox'
      | 'XFree86-1.1'
      | 'xinetd'
      | 'Xnet'
      | 'xpp'
      | 'XSkat'
      | 'YPL-1.0'
      | 'YPL-1.1'
      | 'Zed'
      | 'Zend-2.0'
      | 'Zimbra-1.3'
      | 'Zimbra-1.4'
      | 'Zlib'
      | 'zlib-acknowledgement'
      | 'ZPL-1.1'
      | 'ZPL-2.0'
      | 'ZPL-2.1'
    )
  | [LicenseEnum, ...LicenseEnum[]];
/**
 * SPDX license list; releaseDate=2021-05-14; source=https://raw.githubusercontent.com/spdx/license-list-data/master/json/licenses.json
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "license-enum".
 */
export type LicenseEnum =
  | '0BSD'
  | 'AAL'
  | 'Abstyles'
  | 'Adobe-2006'
  | 'Adobe-Glyph'
  | 'ADSL'
  | 'AFL-1.1'
  | 'AFL-1.2'
  | 'AFL-2.0'
  | 'AFL-2.1'
  | 'AFL-3.0'
  | 'Afmparse'
  | 'AGPL-1.0'
  | 'AGPL-1.0-only'
  | 'AGPL-1.0-or-later'
  | 'AGPL-3.0'
  | 'AGPL-3.0-only'
  | 'AGPL-3.0-or-later'
  | 'Aladdin'
  | 'AMDPLPA'
  | 'AML'
  | 'AMPAS'
  | 'ANTLR-PD'
  | 'ANTLR-PD-fallback'
  | 'Apache-1.0'
  | 'Apache-1.1'
  | 'Apache-2.0'
  | 'APAFML'
  | 'APL-1.0'
  | 'APSL-1.0'
  | 'APSL-1.1'
  | 'APSL-1.2'
  | 'APSL-2.0'
  | 'Artistic-1.0'
  | 'Artistic-1.0-cl8'
  | 'Artistic-1.0-Perl'
  | 'Artistic-2.0'
  | 'Bahyph'
  | 'Barr'
  | 'Beerware'
  | 'BitTorrent-1.0'
  | 'BitTorrent-1.1'
  | 'blessing'
  | 'BlueOak-1.0.0'
  | 'Borceux'
  | 'BSD-1-Clause'
  | 'BSD-2-Clause'
  | 'BSD-2-Clause-FreeBSD'
  | 'BSD-2-Clause-NetBSD'
  | 'BSD-2-Clause-Patent'
  | 'BSD-2-Clause-Views'
  | 'BSD-3-Clause'
  | 'BSD-3-Clause-Attribution'
  | 'BSD-3-Clause-Clear'
  | 'BSD-3-Clause-LBNL'
  | 'BSD-3-Clause-Modification'
  | 'BSD-3-Clause-No-Nuclear-License'
  | 'BSD-3-Clause-No-Nuclear-License-2014'
  | 'BSD-3-Clause-No-Nuclear-Warranty'
  | 'BSD-3-Clause-Open-MPI'
  | 'BSD-4-Clause'
  | 'BSD-4-Clause-Shortened'
  | 'BSD-4-Clause-UC'
  | 'BSD-Protection'
  | 'BSD-Source-Code'
  | 'BSL-1.0'
  | 'BUSL-1.1'
  | 'bzip2-1.0.5'
  | 'bzip2-1.0.6'
  | 'C-UDA-1.0'
  | 'CAL-1.0'
  | 'CAL-1.0-Combined-Work-Exception'
  | 'Caldera'
  | 'CATOSL-1.1'
  | 'CC-BY-1.0'
  | 'CC-BY-2.0'
  | 'CC-BY-2.5'
  | 'CC-BY-3.0'
  | 'CC-BY-3.0-AT'
  | 'CC-BY-3.0-US'
  | 'CC-BY-4.0'
  | 'CC-BY-NC-1.0'
  | 'CC-BY-NC-2.0'
  | 'CC-BY-NC-2.5'
  | 'CC-BY-NC-3.0'
  | 'CC-BY-NC-4.0'
  | 'CC-BY-NC-ND-1.0'
  | 'CC-BY-NC-ND-2.0'
  | 'CC-BY-NC-ND-2.5'
  | 'CC-BY-NC-ND-3.0'
  | 'CC-BY-NC-ND-3.0-IGO'
  | 'CC-BY-NC-ND-4.0'
  | 'CC-BY-NC-SA-1.0'
  | 'CC-BY-NC-SA-2.0'
  | 'CC-BY-NC-SA-2.5'
  | 'CC-BY-NC-SA-3.0'
  | 'CC-BY-NC-SA-4.0'
  | 'CC-BY-ND-1.0'
  | 'CC-BY-ND-2.0'
  | 'CC-BY-ND-2.5'
  | 'CC-BY-ND-3.0'
  | 'CC-BY-ND-4.0'
  | 'CC-BY-SA-1.0'
  | 'CC-BY-SA-2.0'
  | 'CC-BY-SA-2.0-UK'
  | 'CC-BY-SA-2.1-JP'
  | 'CC-BY-SA-2.5'
  | 'CC-BY-SA-3.0'
  | 'CC-BY-SA-3.0-AT'
  | 'CC-BY-SA-4.0'
  | 'CC-PDDC'
  | 'CC0-1.0'
  | 'CDDL-1.0'
  | 'CDDL-1.1'
  | 'CDL-1.0'
  | 'CDLA-Permissive-1.0'
  | 'CDLA-Sharing-1.0'
  | 'CECILL-1.0'
  | 'CECILL-1.1'
  | 'CECILL-2.0'
  | 'CECILL-2.1'
  | 'CECILL-B'
  | 'CECILL-C'
  | 'CERN-OHL-1.1'
  | 'CERN-OHL-1.2'
  | 'CERN-OHL-P-2.0'
  | 'CERN-OHL-S-2.0'
  | 'CERN-OHL-W-2.0'
  | 'ClArtistic'
  | 'CNRI-Jython'
  | 'CNRI-Python'
  | 'CNRI-Python-GPL-Compatible'
  | 'Condor-1.1'
  | 'copyleft-next-0.3.0'
  | 'copyleft-next-0.3.1'
  | 'CPAL-1.0'
  | 'CPL-1.0'
  | 'CPOL-1.02'
  | 'Crossword'
  | 'CrystalStacker'
  | 'CUA-OPL-1.0'
  | 'Cube'
  | 'curl'
  | 'D-FSL-1.0'
  | 'diffmark'
  | 'DOC'
  | 'Dotseqn'
  | 'DRL-1.0'
  | 'DSDP'
  | 'dvipdfm'
  | 'ECL-1.0'
  | 'ECL-2.0'
  | 'eCos-2.0'
  | 'EFL-1.0'
  | 'EFL-2.0'
  | 'eGenix'
  | 'Entessa'
  | 'EPICS'
  | 'EPL-1.0'
  | 'EPL-2.0'
  | 'ErlPL-1.1'
  | 'etalab-2.0'
  | 'EUDatagrid'
  | 'EUPL-1.0'
  | 'EUPL-1.1'
  | 'EUPL-1.2'
  | 'Eurosym'
  | 'Fair'
  | 'Frameworx-1.0'
  | 'FreeBSD-DOC'
  | 'FreeImage'
  | 'FSFAP'
  | 'FSFUL'
  | 'FSFULLR'
  | 'FTL'
  | 'GD'
  | 'GFDL-1.1'
  | 'GFDL-1.1-invariants-only'
  | 'GFDL-1.1-invariants-or-later'
  | 'GFDL-1.1-no-invariants-only'
  | 'GFDL-1.1-no-invariants-or-later'
  | 'GFDL-1.1-only'
  | 'GFDL-1.1-or-later'
  | 'GFDL-1.2'
  | 'GFDL-1.2-invariants-only'
  | 'GFDL-1.2-invariants-or-later'
  | 'GFDL-1.2-no-invariants-only'
  | 'GFDL-1.2-no-invariants-or-later'
  | 'GFDL-1.2-only'
  | 'GFDL-1.2-or-later'
  | 'GFDL-1.3'
  | 'GFDL-1.3-invariants-only'
  | 'GFDL-1.3-invariants-or-later'
  | 'GFDL-1.3-no-invariants-only'
  | 'GFDL-1.3-no-invariants-or-later'
  | 'GFDL-1.3-only'
  | 'GFDL-1.3-or-later'
  | 'Giftware'
  | 'GL2PS'
  | 'Glide'
  | 'Glulxe'
  | 'GLWTPL'
  | 'gnuplot'
  | 'GPL-1.0'
  | 'GPL-1.0-only'
  | 'GPL-1.0-or-later'
  | 'GPL-1.0+'
  | 'GPL-2.0'
  | 'GPL-2.0-only'
  | 'GPL-2.0-or-later'
  | 'GPL-2.0-with-autoconf-exception'
  | 'GPL-2.0-with-bison-exception'
  | 'GPL-2.0-with-classpath-exception'
  | 'GPL-2.0-with-font-exception'
  | 'GPL-2.0-with-GCC-exception'
  | 'GPL-2.0+'
  | 'GPL-3.0'
  | 'GPL-3.0-only'
  | 'GPL-3.0-or-later'
  | 'GPL-3.0-with-autoconf-exception'
  | 'GPL-3.0-with-GCC-exception'
  | 'GPL-3.0+'
  | 'gSOAP-1.3b'
  | 'HaskellReport'
  | 'Hippocratic-2.1'
  | 'HPND'
  | 'HPND-sell-variant'
  | 'HTMLTIDY'
  | 'IBM-pibs'
  | 'ICU'
  | 'IJG'
  | 'ImageMagick'
  | 'iMatix'
  | 'Imlib2'
  | 'Info-ZIP'
  | 'Intel'
  | 'Intel-ACPI'
  | 'Interbase-1.0'
  | 'IPA'
  | 'IPL-1.0'
  | 'ISC'
  | 'JasPer-2.0'
  | 'JPNIC'
  | 'JSON'
  | 'LAL-1.2'
  | 'LAL-1.3'
  | 'Latex2e'
  | 'Leptonica'
  | 'LGPL-2.0'
  | 'LGPL-2.0-only'
  | 'LGPL-2.0-or-later'
  | 'LGPL-2.0+'
  | 'LGPL-2.1'
  | 'LGPL-2.1-only'
  | 'LGPL-2.1-or-later'
  | 'LGPL-2.1+'
  | 'LGPL-3.0'
  | 'LGPL-3.0-only'
  | 'LGPL-3.0-or-later'
  | 'LGPL-3.0+'
  | 'LGPLLR'
  | 'Libpng'
  | 'libpng-2.0'
  | 'libselinux-1.0'
  | 'libtiff'
  | 'LiLiQ-P-1.1'
  | 'LiLiQ-R-1.1'
  | 'LiLiQ-Rplus-1.1'
  | 'Linux-OpenIB'
  | 'LPL-1.0'
  | 'LPL-1.02'
  | 'LPPL-1.0'
  | 'LPPL-1.1'
  | 'LPPL-1.2'
  | 'LPPL-1.3a'
  | 'LPPL-1.3c'
  | 'MakeIndex'
  | 'MirOS'
  | 'MIT'
  | 'MIT-0'
  | 'MIT-advertising'
  | 'MIT-CMU'
  | 'MIT-enna'
  | 'MIT-feh'
  | 'MIT-Modern-Variant'
  | 'MIT-open-group'
  | 'MITNFA'
  | 'Motosoto'
  | 'mpich2'
  | 'MPL-1.0'
  | 'MPL-1.1'
  | 'MPL-2.0'
  | 'MPL-2.0-no-copyleft-exception'
  | 'MS-PL'
  | 'MS-RL'
  | 'MTLL'
  | 'MulanPSL-1.0'
  | 'MulanPSL-2.0'
  | 'Multics'
  | 'Mup'
  | 'NAIST-2003'
  | 'NASA-1.3'
  | 'Naumen'
  | 'NBPL-1.0'
  | 'NCGL-UK-2.0'
  | 'NCSA'
  | 'Net-SNMP'
  | 'NetCDF'
  | 'Newsletr'
  | 'NGPL'
  | 'NIST-PD'
  | 'NIST-PD-fallback'
  | 'NLOD-1.0'
  | 'NLPL'
  | 'Nokia'
  | 'NOSL'
  | 'Noweb'
  | 'NPL-1.0'
  | 'NPL-1.1'
  | 'NPOSL-3.0'
  | 'NRL'
  | 'NTP'
  | 'NTP-0'
  | 'Nunit'
  | 'O-UDA-1.0'
  | 'OCCT-PL'
  | 'OCLC-2.0'
  | 'ODbL-1.0'
  | 'ODC-By-1.0'
  | 'OFL-1.0'
  | 'OFL-1.0-no-RFN'
  | 'OFL-1.0-RFN'
  | 'OFL-1.1'
  | 'OFL-1.1-no-RFN'
  | 'OFL-1.1-RFN'
  | 'OGC-1.0'
  | 'OGDL-Taiwan-1.0'
  | 'OGL-Canada-2.0'
  | 'OGL-UK-1.0'
  | 'OGL-UK-2.0'
  | 'OGL-UK-3.0'
  | 'OGTSL'
  | 'OLDAP-1.1'
  | 'OLDAP-1.2'
  | 'OLDAP-1.3'
  | 'OLDAP-1.4'
  | 'OLDAP-2.0'
  | 'OLDAP-2.0.1'
  | 'OLDAP-2.1'
  | 'OLDAP-2.2'
  | 'OLDAP-2.2.1'
  | 'OLDAP-2.2.2'
  | 'OLDAP-2.3'
  | 'OLDAP-2.4'
  | 'OLDAP-2.5'
  | 'OLDAP-2.6'
  | 'OLDAP-2.7'
  | 'OLDAP-2.8'
  | 'OML'
  | 'OpenSSL'
  | 'OPL-1.0'
  | 'OSET-PL-2.1'
  | 'OSL-1.0'
  | 'OSL-1.1'
  | 'OSL-2.0'
  | 'OSL-2.1'
  | 'OSL-3.0'
  | 'Parity-6.0.0'
  | 'Parity-7.0.0'
  | 'PDDL-1.0'
  | 'PHP-3.0'
  | 'PHP-3.01'
  | 'Plexus'
  | 'PolyForm-Noncommercial-1.0.0'
  | 'PolyForm-Small-Business-1.0.0'
  | 'PostgreSQL'
  | 'PSF-2.0'
  | 'psfrag'
  | 'psutils'
  | 'Python-2.0'
  | 'Qhull'
  | 'QPL-1.0'
  | 'Rdisc'
  | 'RHeCos-1.1'
  | 'RPL-1.1'
  | 'RPL-1.5'
  | 'RPSL-1.0'
  | 'RSA-MD'
  | 'RSCPL'
  | 'Ruby'
  | 'SAX-PD'
  | 'Saxpath'
  | 'SCEA'
  | 'Sendmail'
  | 'Sendmail-8.23'
  | 'SGI-B-1.0'
  | 'SGI-B-1.1'
  | 'SGI-B-2.0'
  | 'SHL-0.5'
  | 'SHL-0.51'
  | 'SimPL-2.0'
  | 'SISSL'
  | 'SISSL-1.2'
  | 'Sleepycat'
  | 'SMLNJ'
  | 'SMPPL'
  | 'SNIA'
  | 'Spencer-86'
  | 'Spencer-94'
  | 'Spencer-99'
  | 'SPL-1.0'
  | 'SSH-OpenSSH'
  | 'SSH-short'
  | 'SSPL-1.0'
  | 'StandardML-NJ'
  | 'SugarCRM-1.1.3'
  | 'SWL'
  | 'TAPR-OHL-1.0'
  | 'TCL'
  | 'TCP-wrappers'
  | 'TMate'
  | 'TORQUE-1.1'
  | 'TOSL'
  | 'TU-Berlin-1.0'
  | 'TU-Berlin-2.0'
  | 'UCL-1.0'
  | 'Unicode-DFS-2015'
  | 'Unicode-DFS-2016'
  | 'Unicode-TOU'
  | 'Unlicense'
  | 'UPL-1.0'
  | 'Vim'
  | 'VOSTROM'
  | 'VSL-1.0'
  | 'W3C'
  | 'W3C-19980720'
  | 'W3C-20150513'
  | 'Watcom-1.0'
  | 'Wsuipa'
  | 'WTFPL'
  | 'wxWindows'
  | 'X11'
  | 'Xerox'
  | 'XFree86-1.1'
  | 'xinetd'
  | 'Xnet'
  | 'xpp'
  | 'XSkat'
  | 'YPL-1.0'
  | 'YPL-1.1'
  | 'Zed'
  | 'Zend-2.0'
  | 'Zimbra-1.3'
  | 'Zimbra-1.4'
  | 'Zlib'
  | 'zlib-acknowledgement'
  | 'ZPL-1.1'
  | 'ZPL-2.0'
  | 'ZPL-2.1';
/**
 * An address.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "address".
 */
export type Address = string;
/**
 * An alias.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "alias".
 */
export type Alias = string;
/**
 * A city
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "city".
 */
export type City = string;
/**
 * The ISO 3166-1 alpha-2 country code for a country.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "country".
 */
export type Country =
  | 'AD'
  | 'AE'
  | 'AF'
  | 'AG'
  | 'AI'
  | 'AL'
  | 'AM'
  | 'AO'
  | 'AQ'
  | 'AR'
  | 'AS'
  | 'AT'
  | 'AU'
  | 'AW'
  | 'AX'
  | 'AZ'
  | 'BA'
  | 'BB'
  | 'BD'
  | 'BE'
  | 'BF'
  | 'BG'
  | 'BH'
  | 'BI'
  | 'BJ'
  | 'BL'
  | 'BM'
  | 'BN'
  | 'BO'
  | 'BQ'
  | 'BR'
  | 'BS'
  | 'BT'
  | 'BV'
  | 'BW'
  | 'BY'
  | 'BZ'
  | 'CA'
  | 'CC'
  | 'CD'
  | 'CF'
  | 'CG'
  | 'CH'
  | 'CI'
  | 'CK'
  | 'CL'
  | 'CM'
  | 'CN'
  | 'CO'
  | 'CR'
  | 'CU'
  | 'CV'
  | 'CW'
  | 'CX'
  | 'CY'
  | 'CZ'
  | 'DE'
  | 'DJ'
  | 'DK'
  | 'DM'
  | 'DO'
  | 'DZ'
  | 'EC'
  | 'EE'
  | 'EG'
  | 'EH'
  | 'ER'
  | 'ES'
  | 'ET'
  | 'FI'
  | 'FJ'
  | 'FK'
  | 'FM'
  | 'FO'
  | 'FR'
  | 'GA'
  | 'GB'
  | 'GD'
  | 'GE'
  | 'GF'
  | 'GG'
  | 'GH'
  | 'GI'
  | 'GL'
  | 'GM'
  | 'GN'
  | 'GP'
  | 'GQ'
  | 'GR'
  | 'GS'
  | 'GT'
  | 'GU'
  | 'GW'
  | 'GY'
  | 'HK'
  | 'HM'
  | 'HN'
  | 'HR'
  | 'HT'
  | 'HU'
  | 'ID'
  | 'IE'
  | 'IL'
  | 'IM'
  | 'IN'
  | 'IO'
  | 'IQ'
  | 'IR'
  | 'IS'
  | 'IT'
  | 'JE'
  | 'JM'
  | 'JO'
  | 'JP'
  | 'KE'
  | 'KG'
  | 'KH'
  | 'KI'
  | 'KM'
  | 'KN'
  | 'KP'
  | 'KR'
  | 'KW'
  | 'KY'
  | 'KZ'
  | 'LA'
  | 'LB'
  | 'LC'
  | 'LI'
  | 'LK'
  | 'LR'
  | 'LS'
  | 'LT'
  | 'LU'
  | 'LV'
  | 'LY'
  | 'MA'
  | 'MC'
  | 'MD'
  | 'ME'
  | 'MF'
  | 'MG'
  | 'MH'
  | 'MK'
  | 'ML'
  | 'MM'
  | 'MN'
  | 'MO'
  | 'MP'
  | 'MQ'
  | 'MR'
  | 'MS'
  | 'MT'
  | 'MU'
  | 'MV'
  | 'MW'
  | 'MX'
  | 'MY'
  | 'MZ'
  | 'NA'
  | 'NC'
  | 'NE'
  | 'NF'
  | 'NG'
  | 'NI'
  | 'NL'
  | 'NO'
  | 'NP'
  | 'NR'
  | 'NU'
  | 'NZ'
  | 'OM'
  | 'PA'
  | 'PE'
  | 'PF'
  | 'PG'
  | 'PH'
  | 'PK'
  | 'PL'
  | 'PM'
  | 'PN'
  | 'PR'
  | 'PS'
  | 'PT'
  | 'PW'
  | 'PY'
  | 'QA'
  | 'RE'
  | 'RO'
  | 'RS'
  | 'RU'
  | 'RW'
  | 'SA'
  | 'SB'
  | 'SC'
  | 'SD'
  | 'SE'
  | 'SG'
  | 'SH'
  | 'SI'
  | 'SJ'
  | 'SK'
  | 'SL'
  | 'SM'
  | 'SN'
  | 'SO'
  | 'SR'
  | 'SS'
  | 'ST'
  | 'SV'
  | 'SX'
  | 'SY'
  | 'SZ'
  | 'TC'
  | 'TD'
  | 'TF'
  | 'TG'
  | 'TH'
  | 'TJ'
  | 'TK'
  | 'TL'
  | 'TM'
  | 'TN'
  | 'TO'
  | 'TR'
  | 'TT'
  | 'TV'
  | 'TW'
  | 'TZ'
  | 'UA'
  | 'UG'
  | 'UM'
  | 'US'
  | 'UY'
  | 'UZ'
  | 'VA'
  | 'VC'
  | 'VE'
  | 'VG'
  | 'VI'
  | 'VN'
  | 'VU'
  | 'WF'
  | 'WS'
  | 'YE'
  | 'YT'
  | 'ZA'
  | 'ZM'
  | 'ZW';
/**
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "date".
 */
export type Date = string;
/**
 * An email address.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "email".
 */
export type Email = string;
/**
 * A fax number.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "fax".
 */
export type Fax = string;
/**
 * Identifier for an author, see https://orcid.org.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "orcid".
 */
export type Orcid = string;
/**
 * A post code.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "post-code".
 */
export type PostCode = string | number;
/**
 * A region.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "region".
 */
export type Region = string;
/**
 * A phone number.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "tel".
 */
export type Tel = string;
/**
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "version".
 */
export type Version = string | number;

/**
 * A file with citation metadata for software or datasets.
 */
export interface CitationFileFormat {
  /**
   * A description of the software or dataset.
   */
  abstract?: string;
  /**
   * The author(s) of the software or dataset.
   *
   * @minItems 1
   */
  authors: [Person | Entity, ...(Person | Entity)[]];
  /**
   * The version of CFF used for providing the citation metadata.
   */
  'cff-version': string;
  commit?: Commit;
  /**
   * The contact person, group, company, etc. for the software or dataset.
   *
   * @minItems 1
   */
  contact?: [Person | Entity, ...(Person | Entity)[]];
  /**
   * The date the work has been released.
   */
  'date-released'?: string;
  doi?: Doi;
  /**
   * The identifiers of the software or dataset.
   *
   * @minItems 1
   */
  identifiers?: [Identifier, ...Identifier[]];
  /**
   * Keywords that describe the work.
   *
   * @minItems 1
   */
  keywords?: [string, ...string[]];
  license?: License;
  /**
   * The URL of the license text under which the software or dataset is licensed (only for non-standard licenses not included in the SPDX License List).
   */
  'license-url'?: string;
  /**
   * A message to the human reader of the file to let them know what to do with the citation metadata.
   */
  message: string;
  'preferred-citation'?: Reference;
  /**
   * Reference(s) to other creative works.
   *
   * @minItems 1
   */
  references?: [Reference1, ...Reference1[]];
  /**
   * The URL of the software or dataset in a repository (when the repository is neither a source code repository nor a build artifact repository).
   */
  repository?: string;
  /**
   * The URL of the software in a build artifact/binary repository.
   */
  'repository-artifact'?: string;
  /**
   * The URL of the software or dataset in a source code repository.
   */
  'repository-code'?: string;
  /**
   * The name of the software or dataset.
   */
  title: string;
  /**
   * The type of the work.
   */
  type?: 'dataset' | 'software';
  /**
   * The URL of a landing page/website for the software or dataset.
   */
  url?: string;
  /**
   * The version of the software or dataset.
   */
  version?: string | number;
}
/**
 * A person.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "person".
 */
export interface Person {
  /**
   * The person's address.
   */
  address?: string;
  /**
   * The person's affilitation.
   */
  affiliation?: string;
  /**
   * The person's alias.
   */
  alias?: string;
  /**
   * The person's city.
   */
  city?: string;
  /**
   * The person's country.
   */
  country?:
    | 'AD'
    | 'AE'
    | 'AF'
    | 'AG'
    | 'AI'
    | 'AL'
    | 'AM'
    | 'AO'
    | 'AQ'
    | 'AR'
    | 'AS'
    | 'AT'
    | 'AU'
    | 'AW'
    | 'AX'
    | 'AZ'
    | 'BA'
    | 'BB'
    | 'BD'
    | 'BE'
    | 'BF'
    | 'BG'
    | 'BH'
    | 'BI'
    | 'BJ'
    | 'BL'
    | 'BM'
    | 'BN'
    | 'BO'
    | 'BQ'
    | 'BR'
    | 'BS'
    | 'BT'
    | 'BV'
    | 'BW'
    | 'BY'
    | 'BZ'
    | 'CA'
    | 'CC'
    | 'CD'
    | 'CF'
    | 'CG'
    | 'CH'
    | 'CI'
    | 'CK'
    | 'CL'
    | 'CM'
    | 'CN'
    | 'CO'
    | 'CR'
    | 'CU'
    | 'CV'
    | 'CW'
    | 'CX'
    | 'CY'
    | 'CZ'
    | 'DE'
    | 'DJ'
    | 'DK'
    | 'DM'
    | 'DO'
    | 'DZ'
    | 'EC'
    | 'EE'
    | 'EG'
    | 'EH'
    | 'ER'
    | 'ES'
    | 'ET'
    | 'FI'
    | 'FJ'
    | 'FK'
    | 'FM'
    | 'FO'
    | 'FR'
    | 'GA'
    | 'GB'
    | 'GD'
    | 'GE'
    | 'GF'
    | 'GG'
    | 'GH'
    | 'GI'
    | 'GL'
    | 'GM'
    | 'GN'
    | 'GP'
    | 'GQ'
    | 'GR'
    | 'GS'
    | 'GT'
    | 'GU'
    | 'GW'
    | 'GY'
    | 'HK'
    | 'HM'
    | 'HN'
    | 'HR'
    | 'HT'
    | 'HU'
    | 'ID'
    | 'IE'
    | 'IL'
    | 'IM'
    | 'IN'
    | 'IO'
    | 'IQ'
    | 'IR'
    | 'IS'
    | 'IT'
    | 'JE'
    | 'JM'
    | 'JO'
    | 'JP'
    | 'KE'
    | 'KG'
    | 'KH'
    | 'KI'
    | 'KM'
    | 'KN'
    | 'KP'
    | 'KR'
    | 'KW'
    | 'KY'
    | 'KZ'
    | 'LA'
    | 'LB'
    | 'LC'
    | 'LI'
    | 'LK'
    | 'LR'
    | 'LS'
    | 'LT'
    | 'LU'
    | 'LV'
    | 'LY'
    | 'MA'
    | 'MC'
    | 'MD'
    | 'ME'
    | 'MF'
    | 'MG'
    | 'MH'
    | 'MK'
    | 'ML'
    | 'MM'
    | 'MN'
    | 'MO'
    | 'MP'
    | 'MQ'
    | 'MR'
    | 'MS'
    | 'MT'
    | 'MU'
    | 'MV'
    | 'MW'
    | 'MX'
    | 'MY'
    | 'MZ'
    | 'NA'
    | 'NC'
    | 'NE'
    | 'NF'
    | 'NG'
    | 'NI'
    | 'NL'
    | 'NO'
    | 'NP'
    | 'NR'
    | 'NU'
    | 'NZ'
    | 'OM'
    | 'PA'
    | 'PE'
    | 'PF'
    | 'PG'
    | 'PH'
    | 'PK'
    | 'PL'
    | 'PM'
    | 'PN'
    | 'PR'
    | 'PS'
    | 'PT'
    | 'PW'
    | 'PY'
    | 'QA'
    | 'RE'
    | 'RO'
    | 'RS'
    | 'RU'
    | 'RW'
    | 'SA'
    | 'SB'
    | 'SC'
    | 'SD'
    | 'SE'
    | 'SG'
    | 'SH'
    | 'SI'
    | 'SJ'
    | 'SK'
    | 'SL'
    | 'SM'
    | 'SN'
    | 'SO'
    | 'SR'
    | 'SS'
    | 'ST'
    | 'SV'
    | 'SX'
    | 'SY'
    | 'SZ'
    | 'TC'
    | 'TD'
    | 'TF'
    | 'TG'
    | 'TH'
    | 'TJ'
    | 'TK'
    | 'TL'
    | 'TM'
    | 'TN'
    | 'TO'
    | 'TR'
    | 'TT'
    | 'TV'
    | 'TW'
    | 'TZ'
    | 'UA'
    | 'UG'
    | 'UM'
    | 'US'
    | 'UY'
    | 'UZ'
    | 'VA'
    | 'VC'
    | 'VE'
    | 'VG'
    | 'VI'
    | 'VN'
    | 'VU'
    | 'WF'
    | 'WS'
    | 'YE'
    | 'YT'
    | 'ZA'
    | 'ZM'
    | 'ZW';
  /**
   * The person's email address.
   */
  email?: string;
  /**
   * The person's family names.
   */
  'family-names'?: string;
  /**
   * The person's fax number.
   */
  fax?: string;
  /**
   * The person's given names.
   */
  'given-names'?: string;
  /**
   * The person's name particle, e.g., a nobiliary particle or a preposition meaning 'of' or 'from' (for example 'von' in 'Alexander von Humboldt').
   */
  'name-particle'?: string;
  /**
   * The person's name-suffix, e.g. 'Jr.' for Sammy Davis Jr. or 'III' for Frank Edwin Wright III.
   */
  'name-suffix'?: string;
  /**
   * The person's ORCID.
   */
  orcid?: string;
  /**
   * The person's post-code.
   */
  'post-code'?: string | number;
  /**
   * The person's region.
   */
  region?: string;
  /**
   * The person's phone number.
   */
  tel?: string;
  /**
   * The person's website.
   */
  website?: string;
}
/**
 * An entity, i.e., an institution, team, research group, company, conference, etc., as opposed to a single natural person.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "entity".
 */
export interface Entity {
  /**
   * The entity's address.
   */
  address?: string;
  /**
   * The entity's alias.
   */
  alias?: string;
  /**
   * The entity's city.
   */
  city?: string;
  /**
   * The entity's country.
   */
  country?:
    | 'AD'
    | 'AE'
    | 'AF'
    | 'AG'
    | 'AI'
    | 'AL'
    | 'AM'
    | 'AO'
    | 'AQ'
    | 'AR'
    | 'AS'
    | 'AT'
    | 'AU'
    | 'AW'
    | 'AX'
    | 'AZ'
    | 'BA'
    | 'BB'
    | 'BD'
    | 'BE'
    | 'BF'
    | 'BG'
    | 'BH'
    | 'BI'
    | 'BJ'
    | 'BL'
    | 'BM'
    | 'BN'
    | 'BO'
    | 'BQ'
    | 'BR'
    | 'BS'
    | 'BT'
    | 'BV'
    | 'BW'
    | 'BY'
    | 'BZ'
    | 'CA'
    | 'CC'
    | 'CD'
    | 'CF'
    | 'CG'
    | 'CH'
    | 'CI'
    | 'CK'
    | 'CL'
    | 'CM'
    | 'CN'
    | 'CO'
    | 'CR'
    | 'CU'
    | 'CV'
    | 'CW'
    | 'CX'
    | 'CY'
    | 'CZ'
    | 'DE'
    | 'DJ'
    | 'DK'
    | 'DM'
    | 'DO'
    | 'DZ'
    | 'EC'
    | 'EE'
    | 'EG'
    | 'EH'
    | 'ER'
    | 'ES'
    | 'ET'
    | 'FI'
    | 'FJ'
    | 'FK'
    | 'FM'
    | 'FO'
    | 'FR'
    | 'GA'
    | 'GB'
    | 'GD'
    | 'GE'
    | 'GF'
    | 'GG'
    | 'GH'
    | 'GI'
    | 'GL'
    | 'GM'
    | 'GN'
    | 'GP'
    | 'GQ'
    | 'GR'
    | 'GS'
    | 'GT'
    | 'GU'
    | 'GW'
    | 'GY'
    | 'HK'
    | 'HM'
    | 'HN'
    | 'HR'
    | 'HT'
    | 'HU'
    | 'ID'
    | 'IE'
    | 'IL'
    | 'IM'
    | 'IN'
    | 'IO'
    | 'IQ'
    | 'IR'
    | 'IS'
    | 'IT'
    | 'JE'
    | 'JM'
    | 'JO'
    | 'JP'
    | 'KE'
    | 'KG'
    | 'KH'
    | 'KI'
    | 'KM'
    | 'KN'
    | 'KP'
    | 'KR'
    | 'KW'
    | 'KY'
    | 'KZ'
    | 'LA'
    | 'LB'
    | 'LC'
    | 'LI'
    | 'LK'
    | 'LR'
    | 'LS'
    | 'LT'
    | 'LU'
    | 'LV'
    | 'LY'
    | 'MA'
    | 'MC'
    | 'MD'
    | 'ME'
    | 'MF'
    | 'MG'
    | 'MH'
    | 'MK'
    | 'ML'
    | 'MM'
    | 'MN'
    | 'MO'
    | 'MP'
    | 'MQ'
    | 'MR'
    | 'MS'
    | 'MT'
    | 'MU'
    | 'MV'
    | 'MW'
    | 'MX'
    | 'MY'
    | 'MZ'
    | 'NA'
    | 'NC'
    | 'NE'
    | 'NF'
    | 'NG'
    | 'NI'
    | 'NL'
    | 'NO'
    | 'NP'
    | 'NR'
    | 'NU'
    | 'NZ'
    | 'OM'
    | 'PA'
    | 'PE'
    | 'PF'
    | 'PG'
    | 'PH'
    | 'PK'
    | 'PL'
    | 'PM'
    | 'PN'
    | 'PR'
    | 'PS'
    | 'PT'
    | 'PW'
    | 'PY'
    | 'QA'
    | 'RE'
    | 'RO'
    | 'RS'
    | 'RU'
    | 'RW'
    | 'SA'
    | 'SB'
    | 'SC'
    | 'SD'
    | 'SE'
    | 'SG'
    | 'SH'
    | 'SI'
    | 'SJ'
    | 'SK'
    | 'SL'
    | 'SM'
    | 'SN'
    | 'SO'
    | 'SR'
    | 'SS'
    | 'ST'
    | 'SV'
    | 'SX'
    | 'SY'
    | 'SZ'
    | 'TC'
    | 'TD'
    | 'TF'
    | 'TG'
    | 'TH'
    | 'TJ'
    | 'TK'
    | 'TL'
    | 'TM'
    | 'TN'
    | 'TO'
    | 'TR'
    | 'TT'
    | 'TV'
    | 'TW'
    | 'TZ'
    | 'UA'
    | 'UG'
    | 'UM'
    | 'US'
    | 'UY'
    | 'UZ'
    | 'VA'
    | 'VC'
    | 'VE'
    | 'VG'
    | 'VI'
    | 'VN'
    | 'VU'
    | 'WF'
    | 'WS'
    | 'YE'
    | 'YT'
    | 'ZA'
    | 'ZM'
    | 'ZW';
  /**
   * The entity's ending date, e.g., when the entity is a conference.
   */
  'date-end'?: string;
  /**
   * The entity's starting date, e.g., when the entity is a conference.
   */
  'date-start'?: string;
  /**
   * The entity's email address.
   */
  email?: string;
  /**
   * The entity's fax number.
   */
  fax?: string;
  /**
   * The entity's location, e.g., when the entity is a conference.
   */
  location?: string;
  /**
   * The entity's name.
   */
  name: string;
  /**
   * The entity's orcid.
   */
  orcid?: string;
  /**
   * The entity's post code.
   */
  'post-code'?: string | number;
  /**
   * The entity's region.
   */
  region?: string;
  /**
   * The entity's telephone number.
   */
  tel?: string;
  /**
   * The entity's website.
   */
  website?: string;
}
/**
 * A reference to another work that should be cited instead of the software or dataset itself.
 */
export interface Reference {
  /**
   * The abbreviation of a work.
   */
  abbreviation?: string;
  /**
   * The abstract of a work.
   */
  abstract?: string;
  /**
   * The author(s) of a work.
   *
   * @minItems 1
   */
  authors: [Person | Entity, ...(Person | Entity)[]];
  /**
   * The DOI of the work (i.e., 10.5281/zenodo.1003150, not the resolver URL http://doi.org/10.5281/zenodo.1003150).
   */
  'collection-doi'?: string;
  /**
   * The title of a collection or proceedings.
   */
  'collection-title'?: string;
  /**
   * The type of a collection.
   */
  'collection-type'?: string;
  commit?: Commit;
  conference?: Entity1;
  /**
   * The contact person, group, company, etc. for a work.
   *
   * @minItems 1
   */
  contact?: [Person | Entity, ...(Person | Entity)[]];
  /**
   * The copyright information pertaining to the work.
   */
  copyright?: string;
  /**
   * The data type of a data set.
   */
  'data-type'?: string;
  /**
   * The name of the database where a work was accessed/is stored.
   */
  database?: string;
  'database-provider'?: Entity2;
  /**
   * The date the work was accessed.
   */
  'date-accessed'?: string;
  /**
   * The date the work has been downloaded.
   */
  'date-downloaded'?: string;
  /**
   * The date the work has been published.
   */
  'date-published'?: string;
  /**
   * The date the work has been released.
   */
  'date-released'?: string;
  /**
   * The department where a work has been produced.
   */
  department?: string;
  /**
   * The DOI of the work (i.e., 10.5281/zenodo.1003150, not the resolver URL http://doi.org/10.5281/zenodo.1003150).
   */
  doi?: string;
  /**
   * The edition of the work.
   */
  edition?: string;
  /**
   * The editor(s) of a work.
   *
   * @minItems 1
   */
  editors?: [Person | Entity, ...(Person | Entity)[]];
  /**
   * The editor(s) of a series in which a work has been published.
   *
   * @minItems 1
   */
  'editors-series'?: [Person | Entity, ...(Person | Entity)[]];
  /**
   * The end page of the work.
   */
  end?: number | string;
  /**
   * An entry in the collection that constitutes the work.
   */
  entry?: string;
  /**
   * The name of the electronic file containing the work.
   */
  filename?: string;
  /**
   * The format in which a work is represented.
   */
  format?: string;
  /**
   * The identifier(s) of the work.
   *
   * @minItems 1
   */
  identifiers?: [Identifier, ...Identifier[]];
  institution?: Entity3;
  /**
   * The ISBN of the work.
   */
  isbn?: string;
  /**
   * The ISSN of the work.
   */
  issn?: string;
  /**
   * The issue of a periodical in which a work appeared.
   */
  issue?: string | number;
  /**
   * The publication date of the issue of a periodical in which a work appeared.
   */
  'issue-date'?: string;
  /**
   * The name of the issue of a periodical in which the work appeared.
   */
  'issue-title'?: string;
  /**
   * The name of the journal/magazine/newspaper/periodical where the work was published.
   */
  journal?: string;
  /**
   * Keywords pertaining to the work.
   *
   * @minItems 1
   */
  keywords?: [string, ...string[]];
  /**
   * The language identifier(s) of the work according to ISO 639 language strings.
   *
   * @minItems 1
   */
  languages?: [string, ...string[]];
  license?: License;
  /**
   * The URL of the license text under which the work is licensed (only for non-standard licenses not included in the SPDX License List).
   */
  'license-url'?: string;
  /**
   * The line of code in the file where the work ends.
   */
  'loc-end'?: number | string;
  /**
   * The line of code in the file where the work starts.
   */
  'loc-start'?: number | string;
  location?: Entity4;
  /**
   * The medium of the work.
   */
  medium?: string;
  /**
   * The month in which a work has been published.
   */
  month?: number | ('1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12');
  /**
   * The NIHMSID of a work.
   */
  nihmsid?: string;
  /**
   * Notes pertaining to the work.
   */
  notes?: string;
  /**
   * The accession number for a work.
   */
  number?: string | number;
  /**
   * The number of volumes making up the collection in which the work has been published.
   */
  'number-volumes'?: number | string;
  /**
   * The number of pages of the work.
   */
  pages?: number | string;
  /**
   * The states for which a patent is granted.
   *
   * @minItems 1
   */
  'patent-states'?: [string, ...string[]];
  /**
   * The PMCID of a work.
   */
  pmcid?: string;
  publisher?: Entity5;
  /**
   * The recipient(s) of a personal communication.
   *
   * @minItems 1
   */
  recipients?: [Entity | Person, ...(Entity | Person)[]];
  /**
   * The URL of the work in a repository (when the repository is neither a source code repository nor a build artifact repository).
   */
  repository?: string;
  /**
   * The URL of the work in a build artifact/binary repository.
   */
  'repository-artifact'?: string;
  /**
   * The URL of the work in a source code repository.
   */
  'repository-code'?: string;
  /**
   * The scope of the reference, e.g., the section of the work it adheres to.
   */
  scope?: string;
  /**
   * The section of a work that is referenced.
   */
  section?: string | number;
  /**
   * The sender(s) of a personal communication.
   *
   * @minItems 1
   */
  senders?: [Entity | Person, ...(Entity | Person)[]];
  /**
   * The start page of the work.
   */
  start?: number | string;
  /**
   * The publication status of the work.
   */
  status?: 'abstract' | 'advance-online' | 'in-preparation' | 'in-press' | 'preprint' | 'submitted';
  /**
   * The term being referenced if the work is a dictionary or encyclopedia.
   */
  term?: string;
  /**
   * The type of the thesis that is the work.
   */
  'thesis-type'?: string;
  /**
   * The title of the work.
   */
  title: string;
  /**
   * The translator(s) of a work.
   *
   * @minItems 1
   */
  translators?: [Entity | Person, ...(Entity | Person)[]];
  /**
   * The type of the work.
   */
  type:
    | 'art'
    | 'article'
    | 'audiovisual'
    | 'bill'
    | 'blog'
    | 'book'
    | 'catalogue'
    | 'conference-paper'
    | 'conference'
    | 'data'
    | 'database'
    | 'dictionary'
    | 'edited-work'
    | 'encyclopedia'
    | 'film-broadcast'
    | 'generic'
    | 'government-document'
    | 'grant'
    | 'hearing'
    | 'historical-work'
    | 'legal-case'
    | 'legal-rule'
    | 'magazine-article'
    | 'manual'
    | 'map'
    | 'multimedia'
    | 'music'
    | 'newspaper-article'
    | 'pamphlet'
    | 'patent'
    | 'personal-communication'
    | 'proceedings'
    | 'report'
    | 'serial'
    | 'slides'
    | 'software-code'
    | 'software-container'
    | 'software-executable'
    | 'software-virtual-machine'
    | 'software'
    | 'sound-recording'
    | 'standard'
    | 'statute'
    | 'thesis'
    | 'unpublished'
    | 'video'
    | 'website';
  /**
   * The URL of the work.
   */
  url?: string;
  /**
   * The version of the work.
   */
  version?: string | number;
  /**
   * The volume of the periodical in which a work appeared.
   */
  volume?: number | string;
  /**
   * The title of the volume in which the work appeared.
   */
  'volume-title'?: string;
  /**
   * The year in which a work has been published.
   */
  year?: number | string;
  /**
   * The year of the original publication.
   */
  'year-original'?: number | string;
}
/**
 * An entity, i.e., an institution, team, research group, company, conference, etc., as opposed to a single natural person.
 */
export interface Entity1 {
  /**
   * The entity's address.
   */
  address?: string;
  /**
   * The entity's alias.
   */
  alias?: string;
  /**
   * The entity's city.
   */
  city?: string;
  /**
   * The entity's country.
   */
  country?:
    | 'AD'
    | 'AE'
    | 'AF'
    | 'AG'
    | 'AI'
    | 'AL'
    | 'AM'
    | 'AO'
    | 'AQ'
    | 'AR'
    | 'AS'
    | 'AT'
    | 'AU'
    | 'AW'
    | 'AX'
    | 'AZ'
    | 'BA'
    | 'BB'
    | 'BD'
    | 'BE'
    | 'BF'
    | 'BG'
    | 'BH'
    | 'BI'
    | 'BJ'
    | 'BL'
    | 'BM'
    | 'BN'
    | 'BO'
    | 'BQ'
    | 'BR'
    | 'BS'
    | 'BT'
    | 'BV'
    | 'BW'
    | 'BY'
    | 'BZ'
    | 'CA'
    | 'CC'
    | 'CD'
    | 'CF'
    | 'CG'
    | 'CH'
    | 'CI'
    | 'CK'
    | 'CL'
    | 'CM'
    | 'CN'
    | 'CO'
    | 'CR'
    | 'CU'
    | 'CV'
    | 'CW'
    | 'CX'
    | 'CY'
    | 'CZ'
    | 'DE'
    | 'DJ'
    | 'DK'
    | 'DM'
    | 'DO'
    | 'DZ'
    | 'EC'
    | 'EE'
    | 'EG'
    | 'EH'
    | 'ER'
    | 'ES'
    | 'ET'
    | 'FI'
    | 'FJ'
    | 'FK'
    | 'FM'
    | 'FO'
    | 'FR'
    | 'GA'
    | 'GB'
    | 'GD'
    | 'GE'
    | 'GF'
    | 'GG'
    | 'GH'
    | 'GI'
    | 'GL'
    | 'GM'
    | 'GN'
    | 'GP'
    | 'GQ'
    | 'GR'
    | 'GS'
    | 'GT'
    | 'GU'
    | 'GW'
    | 'GY'
    | 'HK'
    | 'HM'
    | 'HN'
    | 'HR'
    | 'HT'
    | 'HU'
    | 'ID'
    | 'IE'
    | 'IL'
    | 'IM'
    | 'IN'
    | 'IO'
    | 'IQ'
    | 'IR'
    | 'IS'
    | 'IT'
    | 'JE'
    | 'JM'
    | 'JO'
    | 'JP'
    | 'KE'
    | 'KG'
    | 'KH'
    | 'KI'
    | 'KM'
    | 'KN'
    | 'KP'
    | 'KR'
    | 'KW'
    | 'KY'
    | 'KZ'
    | 'LA'
    | 'LB'
    | 'LC'
    | 'LI'
    | 'LK'
    | 'LR'
    | 'LS'
    | 'LT'
    | 'LU'
    | 'LV'
    | 'LY'
    | 'MA'
    | 'MC'
    | 'MD'
    | 'ME'
    | 'MF'
    | 'MG'
    | 'MH'
    | 'MK'
    | 'ML'
    | 'MM'
    | 'MN'
    | 'MO'
    | 'MP'
    | 'MQ'
    | 'MR'
    | 'MS'
    | 'MT'
    | 'MU'
    | 'MV'
    | 'MW'
    | 'MX'
    | 'MY'
    | 'MZ'
    | 'NA'
    | 'NC'
    | 'NE'
    | 'NF'
    | 'NG'
    | 'NI'
    | 'NL'
    | 'NO'
    | 'NP'
    | 'NR'
    | 'NU'
    | 'NZ'
    | 'OM'
    | 'PA'
    | 'PE'
    | 'PF'
    | 'PG'
    | 'PH'
    | 'PK'
    | 'PL'
    | 'PM'
    | 'PN'
    | 'PR'
    | 'PS'
    | 'PT'
    | 'PW'
    | 'PY'
    | 'QA'
    | 'RE'
    | 'RO'
    | 'RS'
    | 'RU'
    | 'RW'
    | 'SA'
    | 'SB'
    | 'SC'
    | 'SD'
    | 'SE'
    | 'SG'
    | 'SH'
    | 'SI'
    | 'SJ'
    | 'SK'
    | 'SL'
    | 'SM'
    | 'SN'
    | 'SO'
    | 'SR'
    | 'SS'
    | 'ST'
    | 'SV'
    | 'SX'
    | 'SY'
    | 'SZ'
    | 'TC'
    | 'TD'
    | 'TF'
    | 'TG'
    | 'TH'
    | 'TJ'
    | 'TK'
    | 'TL'
    | 'TM'
    | 'TN'
    | 'TO'
    | 'TR'
    | 'TT'
    | 'TV'
    | 'TW'
    | 'TZ'
    | 'UA'
    | 'UG'
    | 'UM'
    | 'US'
    | 'UY'
    | 'UZ'
    | 'VA'
    | 'VC'
    | 'VE'
    | 'VG'
    | 'VI'
    | 'VN'
    | 'VU'
    | 'WF'
    | 'WS'
    | 'YE'
    | 'YT'
    | 'ZA'
    | 'ZM'
    | 'ZW';
  /**
   * The entity's ending date, e.g., when the entity is a conference.
   */
  'date-end'?: string;
  /**
   * The entity's starting date, e.g., when the entity is a conference.
   */
  'date-start'?: string;
  /**
   * The entity's email address.
   */
  email?: string;
  /**
   * The entity's fax number.
   */
  fax?: string;
  /**
   * The entity's location, e.g., when the entity is a conference.
   */
  location?: string;
  /**
   * The entity's name.
   */
  name: string;
  /**
   * The entity's orcid.
   */
  orcid?: string;
  /**
   * The entity's post code.
   */
  'post-code'?: string | number;
  /**
   * The entity's region.
   */
  region?: string;
  /**
   * The entity's telephone number.
   */
  tel?: string;
  /**
   * The entity's website.
   */
  website?: string;
}
/**
 * An entity, i.e., an institution, team, research group, company, conference, etc., as opposed to a single natural person.
 */
export interface Entity2 {
  /**
   * The entity's address.
   */
  address?: string;
  /**
   * The entity's alias.
   */
  alias?: string;
  /**
   * The entity's city.
   */
  city?: string;
  /**
   * The entity's country.
   */
  country?:
    | 'AD'
    | 'AE'
    | 'AF'
    | 'AG'
    | 'AI'
    | 'AL'
    | 'AM'
    | 'AO'
    | 'AQ'
    | 'AR'
    | 'AS'
    | 'AT'
    | 'AU'
    | 'AW'
    | 'AX'
    | 'AZ'
    | 'BA'
    | 'BB'
    | 'BD'
    | 'BE'
    | 'BF'
    | 'BG'
    | 'BH'
    | 'BI'
    | 'BJ'
    | 'BL'
    | 'BM'
    | 'BN'
    | 'BO'
    | 'BQ'
    | 'BR'
    | 'BS'
    | 'BT'
    | 'BV'
    | 'BW'
    | 'BY'
    | 'BZ'
    | 'CA'
    | 'CC'
    | 'CD'
    | 'CF'
    | 'CG'
    | 'CH'
    | 'CI'
    | 'CK'
    | 'CL'
    | 'CM'
    | 'CN'
    | 'CO'
    | 'CR'
    | 'CU'
    | 'CV'
    | 'CW'
    | 'CX'
    | 'CY'
    | 'CZ'
    | 'DE'
    | 'DJ'
    | 'DK'
    | 'DM'
    | 'DO'
    | 'DZ'
    | 'EC'
    | 'EE'
    | 'EG'
    | 'EH'
    | 'ER'
    | 'ES'
    | 'ET'
    | 'FI'
    | 'FJ'
    | 'FK'
    | 'FM'
    | 'FO'
    | 'FR'
    | 'GA'
    | 'GB'
    | 'GD'
    | 'GE'
    | 'GF'
    | 'GG'
    | 'GH'
    | 'GI'
    | 'GL'
    | 'GM'
    | 'GN'
    | 'GP'
    | 'GQ'
    | 'GR'
    | 'GS'
    | 'GT'
    | 'GU'
    | 'GW'
    | 'GY'
    | 'HK'
    | 'HM'
    | 'HN'
    | 'HR'
    | 'HT'
    | 'HU'
    | 'ID'
    | 'IE'
    | 'IL'
    | 'IM'
    | 'IN'
    | 'IO'
    | 'IQ'
    | 'IR'
    | 'IS'
    | 'IT'
    | 'JE'
    | 'JM'
    | 'JO'
    | 'JP'
    | 'KE'
    | 'KG'
    | 'KH'
    | 'KI'
    | 'KM'
    | 'KN'
    | 'KP'
    | 'KR'
    | 'KW'
    | 'KY'
    | 'KZ'
    | 'LA'
    | 'LB'
    | 'LC'
    | 'LI'
    | 'LK'
    | 'LR'
    | 'LS'
    | 'LT'
    | 'LU'
    | 'LV'
    | 'LY'
    | 'MA'
    | 'MC'
    | 'MD'
    | 'ME'
    | 'MF'
    | 'MG'
    | 'MH'
    | 'MK'
    | 'ML'
    | 'MM'
    | 'MN'
    | 'MO'
    | 'MP'
    | 'MQ'
    | 'MR'
    | 'MS'
    | 'MT'
    | 'MU'
    | 'MV'
    | 'MW'
    | 'MX'
    | 'MY'
    | 'MZ'
    | 'NA'
    | 'NC'
    | 'NE'
    | 'NF'
    | 'NG'
    | 'NI'
    | 'NL'
    | 'NO'
    | 'NP'
    | 'NR'
    | 'NU'
    | 'NZ'
    | 'OM'
    | 'PA'
    | 'PE'
    | 'PF'
    | 'PG'
    | 'PH'
    | 'PK'
    | 'PL'
    | 'PM'
    | 'PN'
    | 'PR'
    | 'PS'
    | 'PT'
    | 'PW'
    | 'PY'
    | 'QA'
    | 'RE'
    | 'RO'
    | 'RS'
    | 'RU'
    | 'RW'
    | 'SA'
    | 'SB'
    | 'SC'
    | 'SD'
    | 'SE'
    | 'SG'
    | 'SH'
    | 'SI'
    | 'SJ'
    | 'SK'
    | 'SL'
    | 'SM'
    | 'SN'
    | 'SO'
    | 'SR'
    | 'SS'
    | 'ST'
    | 'SV'
    | 'SX'
    | 'SY'
    | 'SZ'
    | 'TC'
    | 'TD'
    | 'TF'
    | 'TG'
    | 'TH'
    | 'TJ'
    | 'TK'
    | 'TL'
    | 'TM'
    | 'TN'
    | 'TO'
    | 'TR'
    | 'TT'
    | 'TV'
    | 'TW'
    | 'TZ'
    | 'UA'
    | 'UG'
    | 'UM'
    | 'US'
    | 'UY'
    | 'UZ'
    | 'VA'
    | 'VC'
    | 'VE'
    | 'VG'
    | 'VI'
    | 'VN'
    | 'VU'
    | 'WF'
    | 'WS'
    | 'YE'
    | 'YT'
    | 'ZA'
    | 'ZM'
    | 'ZW';
  /**
   * The entity's ending date, e.g., when the entity is a conference.
   */
  'date-end'?: string;
  /**
   * The entity's starting date, e.g., when the entity is a conference.
   */
  'date-start'?: string;
  /**
   * The entity's email address.
   */
  email?: string;
  /**
   * The entity's fax number.
   */
  fax?: string;
  /**
   * The entity's location, e.g., when the entity is a conference.
   */
  location?: string;
  /**
   * The entity's name.
   */
  name: string;
  /**
   * The entity's orcid.
   */
  orcid?: string;
  /**
   * The entity's post code.
   */
  'post-code'?: string | number;
  /**
   * The entity's region.
   */
  region?: string;
  /**
   * The entity's telephone number.
   */
  tel?: string;
  /**
   * The entity's website.
   */
  website?: string;
}
/**
 * An entity, i.e., an institution, team, research group, company, conference, etc., as opposed to a single natural person.
 */
export interface Entity3 {
  /**
   * The entity's address.
   */
  address?: string;
  /**
   * The entity's alias.
   */
  alias?: string;
  /**
   * The entity's city.
   */
  city?: string;
  /**
   * The entity's country.
   */
  country?:
    | 'AD'
    | 'AE'
    | 'AF'
    | 'AG'
    | 'AI'
    | 'AL'
    | 'AM'
    | 'AO'
    | 'AQ'
    | 'AR'
    | 'AS'
    | 'AT'
    | 'AU'
    | 'AW'
    | 'AX'
    | 'AZ'
    | 'BA'
    | 'BB'
    | 'BD'
    | 'BE'
    | 'BF'
    | 'BG'
    | 'BH'
    | 'BI'
    | 'BJ'
    | 'BL'
    | 'BM'
    | 'BN'
    | 'BO'
    | 'BQ'
    | 'BR'
    | 'BS'
    | 'BT'
    | 'BV'
    | 'BW'
    | 'BY'
    | 'BZ'
    | 'CA'
    | 'CC'
    | 'CD'
    | 'CF'
    | 'CG'
    | 'CH'
    | 'CI'
    | 'CK'
    | 'CL'
    | 'CM'
    | 'CN'
    | 'CO'
    | 'CR'
    | 'CU'
    | 'CV'
    | 'CW'
    | 'CX'
    | 'CY'
    | 'CZ'
    | 'DE'
    | 'DJ'
    | 'DK'
    | 'DM'
    | 'DO'
    | 'DZ'
    | 'EC'
    | 'EE'
    | 'EG'
    | 'EH'
    | 'ER'
    | 'ES'
    | 'ET'
    | 'FI'
    | 'FJ'
    | 'FK'
    | 'FM'
    | 'FO'
    | 'FR'
    | 'GA'
    | 'GB'
    | 'GD'
    | 'GE'
    | 'GF'
    | 'GG'
    | 'GH'
    | 'GI'
    | 'GL'
    | 'GM'
    | 'GN'
    | 'GP'
    | 'GQ'
    | 'GR'
    | 'GS'
    | 'GT'
    | 'GU'
    | 'GW'
    | 'GY'
    | 'HK'
    | 'HM'
    | 'HN'
    | 'HR'
    | 'HT'
    | 'HU'
    | 'ID'
    | 'IE'
    | 'IL'
    | 'IM'
    | 'IN'
    | 'IO'
    | 'IQ'
    | 'IR'
    | 'IS'
    | 'IT'
    | 'JE'
    | 'JM'
    | 'JO'
    | 'JP'
    | 'KE'
    | 'KG'
    | 'KH'
    | 'KI'
    | 'KM'
    | 'KN'
    | 'KP'
    | 'KR'
    | 'KW'
    | 'KY'
    | 'KZ'
    | 'LA'
    | 'LB'
    | 'LC'
    | 'LI'
    | 'LK'
    | 'LR'
    | 'LS'
    | 'LT'
    | 'LU'
    | 'LV'
    | 'LY'
    | 'MA'
    | 'MC'
    | 'MD'
    | 'ME'
    | 'MF'
    | 'MG'
    | 'MH'
    | 'MK'
    | 'ML'
    | 'MM'
    | 'MN'
    | 'MO'
    | 'MP'
    | 'MQ'
    | 'MR'
    | 'MS'
    | 'MT'
    | 'MU'
    | 'MV'
    | 'MW'
    | 'MX'
    | 'MY'
    | 'MZ'
    | 'NA'
    | 'NC'
    | 'NE'
    | 'NF'
    | 'NG'
    | 'NI'
    | 'NL'
    | 'NO'
    | 'NP'
    | 'NR'
    | 'NU'
    | 'NZ'
    | 'OM'
    | 'PA'
    | 'PE'
    | 'PF'
    | 'PG'
    | 'PH'
    | 'PK'
    | 'PL'
    | 'PM'
    | 'PN'
    | 'PR'
    | 'PS'
    | 'PT'
    | 'PW'
    | 'PY'
    | 'QA'
    | 'RE'
    | 'RO'
    | 'RS'
    | 'RU'
    | 'RW'
    | 'SA'
    | 'SB'
    | 'SC'
    | 'SD'
    | 'SE'
    | 'SG'
    | 'SH'
    | 'SI'
    | 'SJ'
    | 'SK'
    | 'SL'
    | 'SM'
    | 'SN'
    | 'SO'
    | 'SR'
    | 'SS'
    | 'ST'
    | 'SV'
    | 'SX'
    | 'SY'
    | 'SZ'
    | 'TC'
    | 'TD'
    | 'TF'
    | 'TG'
    | 'TH'
    | 'TJ'
    | 'TK'
    | 'TL'
    | 'TM'
    | 'TN'
    | 'TO'
    | 'TR'
    | 'TT'
    | 'TV'
    | 'TW'
    | 'TZ'
    | 'UA'
    | 'UG'
    | 'UM'
    | 'US'
    | 'UY'
    | 'UZ'
    | 'VA'
    | 'VC'
    | 'VE'
    | 'VG'
    | 'VI'
    | 'VN'
    | 'VU'
    | 'WF'
    | 'WS'
    | 'YE'
    | 'YT'
    | 'ZA'
    | 'ZM'
    | 'ZW';
  /**
   * The entity's ending date, e.g., when the entity is a conference.
   */
  'date-end'?: string;
  /**
   * The entity's starting date, e.g., when the entity is a conference.
   */
  'date-start'?: string;
  /**
   * The entity's email address.
   */
  email?: string;
  /**
   * The entity's fax number.
   */
  fax?: string;
  /**
   * The entity's location, e.g., when the entity is a conference.
   */
  location?: string;
  /**
   * The entity's name.
   */
  name: string;
  /**
   * The entity's orcid.
   */
  orcid?: string;
  /**
   * The entity's post code.
   */
  'post-code'?: string | number;
  /**
   * The entity's region.
   */
  region?: string;
  /**
   * The entity's telephone number.
   */
  tel?: string;
  /**
   * The entity's website.
   */
  website?: string;
}
/**
 * An entity, i.e., an institution, team, research group, company, conference, etc., as opposed to a single natural person.
 */
export interface Entity4 {
  /**
   * The entity's address.
   */
  address?: string;
  /**
   * The entity's alias.
   */
  alias?: string;
  /**
   * The entity's city.
   */
  city?: string;
  /**
   * The entity's country.
   */
  country?:
    | 'AD'
    | 'AE'
    | 'AF'
    | 'AG'
    | 'AI'
    | 'AL'
    | 'AM'
    | 'AO'
    | 'AQ'
    | 'AR'
    | 'AS'
    | 'AT'
    | 'AU'
    | 'AW'
    | 'AX'
    | 'AZ'
    | 'BA'
    | 'BB'
    | 'BD'
    | 'BE'
    | 'BF'
    | 'BG'
    | 'BH'
    | 'BI'
    | 'BJ'
    | 'BL'
    | 'BM'
    | 'BN'
    | 'BO'
    | 'BQ'
    | 'BR'
    | 'BS'
    | 'BT'
    | 'BV'
    | 'BW'
    | 'BY'
    | 'BZ'
    | 'CA'
    | 'CC'
    | 'CD'
    | 'CF'
    | 'CG'
    | 'CH'
    | 'CI'
    | 'CK'
    | 'CL'
    | 'CM'
    | 'CN'
    | 'CO'
    | 'CR'
    | 'CU'
    | 'CV'
    | 'CW'
    | 'CX'
    | 'CY'
    | 'CZ'
    | 'DE'
    | 'DJ'
    | 'DK'
    | 'DM'
    | 'DO'
    | 'DZ'
    | 'EC'
    | 'EE'
    | 'EG'
    | 'EH'
    | 'ER'
    | 'ES'
    | 'ET'
    | 'FI'
    | 'FJ'
    | 'FK'
    | 'FM'
    | 'FO'
    | 'FR'
    | 'GA'
    | 'GB'
    | 'GD'
    | 'GE'
    | 'GF'
    | 'GG'
    | 'GH'
    | 'GI'
    | 'GL'
    | 'GM'
    | 'GN'
    | 'GP'
    | 'GQ'
    | 'GR'
    | 'GS'
    | 'GT'
    | 'GU'
    | 'GW'
    | 'GY'
    | 'HK'
    | 'HM'
    | 'HN'
    | 'HR'
    | 'HT'
    | 'HU'
    | 'ID'
    | 'IE'
    | 'IL'
    | 'IM'
    | 'IN'
    | 'IO'
    | 'IQ'
    | 'IR'
    | 'IS'
    | 'IT'
    | 'JE'
    | 'JM'
    | 'JO'
    | 'JP'
    | 'KE'
    | 'KG'
    | 'KH'
    | 'KI'
    | 'KM'
    | 'KN'
    | 'KP'
    | 'KR'
    | 'KW'
    | 'KY'
    | 'KZ'
    | 'LA'
    | 'LB'
    | 'LC'
    | 'LI'
    | 'LK'
    | 'LR'
    | 'LS'
    | 'LT'
    | 'LU'
    | 'LV'
    | 'LY'
    | 'MA'
    | 'MC'
    | 'MD'
    | 'ME'
    | 'MF'
    | 'MG'
    | 'MH'
    | 'MK'
    | 'ML'
    | 'MM'
    | 'MN'
    | 'MO'
    | 'MP'
    | 'MQ'
    | 'MR'
    | 'MS'
    | 'MT'
    | 'MU'
    | 'MV'
    | 'MW'
    | 'MX'
    | 'MY'
    | 'MZ'
    | 'NA'
    | 'NC'
    | 'NE'
    | 'NF'
    | 'NG'
    | 'NI'
    | 'NL'
    | 'NO'
    | 'NP'
    | 'NR'
    | 'NU'
    | 'NZ'
    | 'OM'
    | 'PA'
    | 'PE'
    | 'PF'
    | 'PG'
    | 'PH'
    | 'PK'
    | 'PL'
    | 'PM'
    | 'PN'
    | 'PR'
    | 'PS'
    | 'PT'
    | 'PW'
    | 'PY'
    | 'QA'
    | 'RE'
    | 'RO'
    | 'RS'
    | 'RU'
    | 'RW'
    | 'SA'
    | 'SB'
    | 'SC'
    | 'SD'
    | 'SE'
    | 'SG'
    | 'SH'
    | 'SI'
    | 'SJ'
    | 'SK'
    | 'SL'
    | 'SM'
    | 'SN'
    | 'SO'
    | 'SR'
    | 'SS'
    | 'ST'
    | 'SV'
    | 'SX'
    | 'SY'
    | 'SZ'
    | 'TC'
    | 'TD'
    | 'TF'
    | 'TG'
    | 'TH'
    | 'TJ'
    | 'TK'
    | 'TL'
    | 'TM'
    | 'TN'
    | 'TO'
    | 'TR'
    | 'TT'
    | 'TV'
    | 'TW'
    | 'TZ'
    | 'UA'
    | 'UG'
    | 'UM'
    | 'US'
    | 'UY'
    | 'UZ'
    | 'VA'
    | 'VC'
    | 'VE'
    | 'VG'
    | 'VI'
    | 'VN'
    | 'VU'
    | 'WF'
    | 'WS'
    | 'YE'
    | 'YT'
    | 'ZA'
    | 'ZM'
    | 'ZW';
  /**
   * The entity's ending date, e.g., when the entity is a conference.
   */
  'date-end'?: string;
  /**
   * The entity's starting date, e.g., when the entity is a conference.
   */
  'date-start'?: string;
  /**
   * The entity's email address.
   */
  email?: string;
  /**
   * The entity's fax number.
   */
  fax?: string;
  /**
   * The entity's location, e.g., when the entity is a conference.
   */
  location?: string;
  /**
   * The entity's name.
   */
  name: string;
  /**
   * The entity's orcid.
   */
  orcid?: string;
  /**
   * The entity's post code.
   */
  'post-code'?: string | number;
  /**
   * The entity's region.
   */
  region?: string;
  /**
   * The entity's telephone number.
   */
  tel?: string;
  /**
   * The entity's website.
   */
  website?: string;
}
/**
 * An entity, i.e., an institution, team, research group, company, conference, etc., as opposed to a single natural person.
 */
export interface Entity5 {
  /**
   * The entity's address.
   */
  address?: string;
  /**
   * The entity's alias.
   */
  alias?: string;
  /**
   * The entity's city.
   */
  city?: string;
  /**
   * The entity's country.
   */
  country?:
    | 'AD'
    | 'AE'
    | 'AF'
    | 'AG'
    | 'AI'
    | 'AL'
    | 'AM'
    | 'AO'
    | 'AQ'
    | 'AR'
    | 'AS'
    | 'AT'
    | 'AU'
    | 'AW'
    | 'AX'
    | 'AZ'
    | 'BA'
    | 'BB'
    | 'BD'
    | 'BE'
    | 'BF'
    | 'BG'
    | 'BH'
    | 'BI'
    | 'BJ'
    | 'BL'
    | 'BM'
    | 'BN'
    | 'BO'
    | 'BQ'
    | 'BR'
    | 'BS'
    | 'BT'
    | 'BV'
    | 'BW'
    | 'BY'
    | 'BZ'
    | 'CA'
    | 'CC'
    | 'CD'
    | 'CF'
    | 'CG'
    | 'CH'
    | 'CI'
    | 'CK'
    | 'CL'
    | 'CM'
    | 'CN'
    | 'CO'
    | 'CR'
    | 'CU'
    | 'CV'
    | 'CW'
    | 'CX'
    | 'CY'
    | 'CZ'
    | 'DE'
    | 'DJ'
    | 'DK'
    | 'DM'
    | 'DO'
    | 'DZ'
    | 'EC'
    | 'EE'
    | 'EG'
    | 'EH'
    | 'ER'
    | 'ES'
    | 'ET'
    | 'FI'
    | 'FJ'
    | 'FK'
    | 'FM'
    | 'FO'
    | 'FR'
    | 'GA'
    | 'GB'
    | 'GD'
    | 'GE'
    | 'GF'
    | 'GG'
    | 'GH'
    | 'GI'
    | 'GL'
    | 'GM'
    | 'GN'
    | 'GP'
    | 'GQ'
    | 'GR'
    | 'GS'
    | 'GT'
    | 'GU'
    | 'GW'
    | 'GY'
    | 'HK'
    | 'HM'
    | 'HN'
    | 'HR'
    | 'HT'
    | 'HU'
    | 'ID'
    | 'IE'
    | 'IL'
    | 'IM'
    | 'IN'
    | 'IO'
    | 'IQ'
    | 'IR'
    | 'IS'
    | 'IT'
    | 'JE'
    | 'JM'
    | 'JO'
    | 'JP'
    | 'KE'
    | 'KG'
    | 'KH'
    | 'KI'
    | 'KM'
    | 'KN'
    | 'KP'
    | 'KR'
    | 'KW'
    | 'KY'
    | 'KZ'
    | 'LA'
    | 'LB'
    | 'LC'
    | 'LI'
    | 'LK'
    | 'LR'
    | 'LS'
    | 'LT'
    | 'LU'
    | 'LV'
    | 'LY'
    | 'MA'
    | 'MC'
    | 'MD'
    | 'ME'
    | 'MF'
    | 'MG'
    | 'MH'
    | 'MK'
    | 'ML'
    | 'MM'
    | 'MN'
    | 'MO'
    | 'MP'
    | 'MQ'
    | 'MR'
    | 'MS'
    | 'MT'
    | 'MU'
    | 'MV'
    | 'MW'
    | 'MX'
    | 'MY'
    | 'MZ'
    | 'NA'
    | 'NC'
    | 'NE'
    | 'NF'
    | 'NG'
    | 'NI'
    | 'NL'
    | 'NO'
    | 'NP'
    | 'NR'
    | 'NU'
    | 'NZ'
    | 'OM'
    | 'PA'
    | 'PE'
    | 'PF'
    | 'PG'
    | 'PH'
    | 'PK'
    | 'PL'
    | 'PM'
    | 'PN'
    | 'PR'
    | 'PS'
    | 'PT'
    | 'PW'
    | 'PY'
    | 'QA'
    | 'RE'
    | 'RO'
    | 'RS'
    | 'RU'
    | 'RW'
    | 'SA'
    | 'SB'
    | 'SC'
    | 'SD'
    | 'SE'
    | 'SG'
    | 'SH'
    | 'SI'
    | 'SJ'
    | 'SK'
    | 'SL'
    | 'SM'
    | 'SN'
    | 'SO'
    | 'SR'
    | 'SS'
    | 'ST'
    | 'SV'
    | 'SX'
    | 'SY'
    | 'SZ'
    | 'TC'
    | 'TD'
    | 'TF'
    | 'TG'
    | 'TH'
    | 'TJ'
    | 'TK'
    | 'TL'
    | 'TM'
    | 'TN'
    | 'TO'
    | 'TR'
    | 'TT'
    | 'TV'
    | 'TW'
    | 'TZ'
    | 'UA'
    | 'UG'
    | 'UM'
    | 'US'
    | 'UY'
    | 'UZ'
    | 'VA'
    | 'VC'
    | 'VE'
    | 'VG'
    | 'VI'
    | 'VN'
    | 'VU'
    | 'WF'
    | 'WS'
    | 'YE'
    | 'YT'
    | 'ZA'
    | 'ZM'
    | 'ZW';
  /**
   * The entity's ending date, e.g., when the entity is a conference.
   */
  'date-end'?: string;
  /**
   * The entity's starting date, e.g., when the entity is a conference.
   */
  'date-start'?: string;
  /**
   * The entity's email address.
   */
  email?: string;
  /**
   * The entity's fax number.
   */
  fax?: string;
  /**
   * The entity's location, e.g., when the entity is a conference.
   */
  location?: string;
  /**
   * The entity's name.
   */
  name: string;
  /**
   * The entity's orcid.
   */
  orcid?: string;
  /**
   * The entity's post code.
   */
  'post-code'?: string | number;
  /**
   * The entity's region.
   */
  region?: string;
  /**
   * The entity's telephone number.
   */
  tel?: string;
  /**
   * The entity's website.
   */
  website?: string;
}
/**
 * A reference to a work.
 *
 * This interface was referenced by `CitationFileFormat`'s JSON-Schema
 * via the `definition` "reference".
 */
export interface Reference1 {
  /**
   * The abbreviation of a work.
   */
  abbreviation?: string;
  /**
   * The abstract of a work.
   */
  abstract?: string;
  /**
   * The author(s) of a work.
   *
   * @minItems 1
   */
  authors: [Person | Entity, ...(Person | Entity)[]];
  /**
   * The DOI of the work (i.e., 10.5281/zenodo.1003150, not the resolver URL http://doi.org/10.5281/zenodo.1003150).
   */
  'collection-doi'?: string;
  /**
   * The title of a collection or proceedings.
   */
  'collection-title'?: string;
  /**
   * The type of a collection.
   */
  'collection-type'?: string;
  commit?: Commit;
  conference?: Entity1;
  /**
   * The contact person, group, company, etc. for a work.
   *
   * @minItems 1
   */
  contact?: [Person | Entity, ...(Person | Entity)[]];
  /**
   * The copyright information pertaining to the work.
   */
  copyright?: string;
  /**
   * The data type of a data set.
   */
  'data-type'?: string;
  /**
   * The name of the database where a work was accessed/is stored.
   */
  database?: string;
  'database-provider'?: Entity2;
  /**
   * The date the work was accessed.
   */
  'date-accessed'?: string;
  /**
   * The date the work has been downloaded.
   */
  'date-downloaded'?: string;
  /**
   * The date the work has been published.
   */
  'date-published'?: string;
  /**
   * The date the work has been released.
   */
  'date-released'?: string;
  /**
   * The department where a work has been produced.
   */
  department?: string;
  /**
   * The DOI of the work (i.e., 10.5281/zenodo.1003150, not the resolver URL http://doi.org/10.5281/zenodo.1003150).
   */
  doi?: string;
  /**
   * The edition of the work.
   */
  edition?: string;
  /**
   * The editor(s) of a work.
   *
   * @minItems 1
   */
  editors?: [Person | Entity, ...(Person | Entity)[]];
  /**
   * The editor(s) of a series in which a work has been published.
   *
   * @minItems 1
   */
  'editors-series'?: [Person | Entity, ...(Person | Entity)[]];
  /**
   * The end page of the work.
   */
  end?: number | string;
  /**
   * An entry in the collection that constitutes the work.
   */
  entry?: string;
  /**
   * The name of the electronic file containing the work.
   */
  filename?: string;
  /**
   * The format in which a work is represented.
   */
  format?: string;
  /**
   * The identifier(s) of the work.
   *
   * @minItems 1
   */
  identifiers?: [Identifier, ...Identifier[]];
  institution?: Entity3;
  /**
   * The ISBN of the work.
   */
  isbn?: string;
  /**
   * The ISSN of the work.
   */
  issn?: string;
  /**
   * The issue of a periodical in which a work appeared.
   */
  issue?: string | number;
  /**
   * The publication date of the issue of a periodical in which a work appeared.
   */
  'issue-date'?: string;
  /**
   * The name of the issue of a periodical in which the work appeared.
   */
  'issue-title'?: string;
  /**
   * The name of the journal/magazine/newspaper/periodical where the work was published.
   */
  journal?: string;
  /**
   * Keywords pertaining to the work.
   *
   * @minItems 1
   */
  keywords?: [string, ...string[]];
  /**
   * The language identifier(s) of the work according to ISO 639 language strings.
   *
   * @minItems 1
   */
  languages?: [string, ...string[]];
  license?: License;
  /**
   * The URL of the license text under which the work is licensed (only for non-standard licenses not included in the SPDX License List).
   */
  'license-url'?: string;
  /**
   * The line of code in the file where the work ends.
   */
  'loc-end'?: number | string;
  /**
   * The line of code in the file where the work starts.
   */
  'loc-start'?: number | string;
  location?: Entity4;
  /**
   * The medium of the work.
   */
  medium?: string;
  /**
   * The month in which a work has been published.
   */
  month?: number | ('1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12');
  /**
   * The NIHMSID of a work.
   */
  nihmsid?: string;
  /**
   * Notes pertaining to the work.
   */
  notes?: string;
  /**
   * The accession number for a work.
   */
  number?: string | number;
  /**
   * The number of volumes making up the collection in which the work has been published.
   */
  'number-volumes'?: number | string;
  /**
   * The number of pages of the work.
   */
  pages?: number | string;
  /**
   * The states for which a patent is granted.
   *
   * @minItems 1
   */
  'patent-states'?: [string, ...string[]];
  /**
   * The PMCID of a work.
   */
  pmcid?: string;
  publisher?: Entity5;
  /**
   * The recipient(s) of a personal communication.
   *
   * @minItems 1
   */
  recipients?: [Entity | Person, ...(Entity | Person)[]];
  /**
   * The URL of the work in a repository (when the repository is neither a source code repository nor a build artifact repository).
   */
  repository?: string;
  /**
   * The URL of the work in a build artifact/binary repository.
   */
  'repository-artifact'?: string;
  /**
   * The URL of the work in a source code repository.
   */
  'repository-code'?: string;
  /**
   * The scope of the reference, e.g., the section of the work it adheres to.
   */
  scope?: string;
  /**
   * The section of a work that is referenced.
   */
  section?: string | number;
  /**
   * The sender(s) of a personal communication.
   *
   * @minItems 1
   */
  senders?: [Entity | Person, ...(Entity | Person)[]];
  /**
   * The start page of the work.
   */
  start?: number | string;
  /**
   * The publication status of the work.
   */
  status?: 'abstract' | 'advance-online' | 'in-preparation' | 'in-press' | 'preprint' | 'submitted';
  /**
   * The term being referenced if the work is a dictionary or encyclopedia.
   */
  term?: string;
  /**
   * The type of the thesis that is the work.
   */
  'thesis-type'?: string;
  /**
   * The title of the work.
   */
  title: string;
  /**
   * The translator(s) of a work.
   *
   * @minItems 1
   */
  translators?: [Entity | Person, ...(Entity | Person)[]];
  /**
   * The type of the work.
   */
  type:
    | 'art'
    | 'article'
    | 'audiovisual'
    | 'bill'
    | 'blog'
    | 'book'
    | 'catalogue'
    | 'conference-paper'
    | 'conference'
    | 'data'
    | 'database'
    | 'dictionary'
    | 'edited-work'
    | 'encyclopedia'
    | 'film-broadcast'
    | 'generic'
    | 'government-document'
    | 'grant'
    | 'hearing'
    | 'historical-work'
    | 'legal-case'
    | 'legal-rule'
    | 'magazine-article'
    | 'manual'
    | 'map'
    | 'multimedia'
    | 'music'
    | 'newspaper-article'
    | 'pamphlet'
    | 'patent'
    | 'personal-communication'
    | 'proceedings'
    | 'report'
    | 'serial'
    | 'slides'
    | 'software-code'
    | 'software-container'
    | 'software-executable'
    | 'software-virtual-machine'
    | 'software'
    | 'sound-recording'
    | 'standard'
    | 'statute'
    | 'thesis'
    | 'unpublished'
    | 'video'
    | 'website';
  /**
   * The URL of the work.
   */
  url?: string;
  /**
   * The version of the work.
   */
  version?: string | number;
  /**
   * The volume of the periodical in which a work appeared.
   */
  volume?: number | string;
  /**
   * The title of the volume in which the work appeared.
   */
  'volume-title'?: string;
  /**
   * The year in which a work has been published.
   */
  year?: number | string;
  /**
   * The year of the original publication.
   */
  'year-original'?: number | string;
}


// --- Zenodo Types ---

/**
 * Metadata for Zenodo depositions as defined in the official API documentation.
 */
export interface ZenodoDepositionMetadata {
  /**
   * The type of the upload.
   */
  upload_type:
    | 'publication'
    | 'poster'
    | 'presentation'
    | 'dataset'
    | 'image'
    | 'video'
    | 'software'
    | 'lesson'
    | 'physicalobject'
    | 'other';
  /**
   * Mandatory if upload_type is 'publication'.
   */
  publication_type?:
    | 'annotationcollection'
    | 'book'
    | 'section'
    | 'conferencepaper'
    | 'datamanagementplan'
    | 'article'
    | 'patent'
    | 'preprint'
    | 'deliverable'
    | 'milestone'
    | 'proposal'
    | 'report'
    | 'softwaredocumentation'
    | 'taxonomictreatment'
    | 'technicalnote'
    | 'thesis'
    | 'workingpaper'
    | 'other';
  /**
   * Mandatory if upload_type is 'image'.
   */
  image_type?: 'figure' | 'plot' | 'drawing' | 'diagram' | 'photo' | 'other';
  /**
   * Date of publication in ISO8601 format (YYYY-MM-DD).
   */
  publication_date?: string;
  /**
   * Title of deposition.
   */
  title: string;
  creators: {
    /**
     * Family name, Given names
     */
    name: string;
    affiliation?: string;
    orcid?: string;
    gnd?: string;
    [k: string]: unknown;
  }[];
  /**
   * Abstract or description (allows limited HTML tags).
   */
  description: string;
  access_right?: 'open' | 'embargoed' | 'restricted' | 'closed';
  /**
   * License identifier (e.g., cc-by-4.0).
   */
  license?: string;
  embargo_date?: string;
  access_conditions?: string;
  doi?: string;
  prereserve_doi?: boolean;
  keywords?: string[];
  notes?: string;
  related_identifiers?: {
    identifier: string;
    relation:
      | 'isCitedBy'
      | 'cites'
      | 'isSupplementTo'
      | 'isSupplementedBy'
      | 'isContinuedBy'
      | 'continues'
      | 'isDescribedBy'
      | 'describes'
      | 'hasMetadata'
      | 'isMetadataFor'
      | 'isNewVersionOf'
      | 'isPreviousVersionOf'
      | 'isPartOf'
      | 'hasPart'
      | 'isReferencedBy'
      | 'references'
      | 'isDocumentedBy'
      | 'documents'
      | 'isCompiledBy'
      | 'compiles'
      | 'isVariantFormOf'
      | 'isOriginalFormof'
      | 'isIdenticalTo'
      | 'isAlternateIdentifier'
      | 'isReviewedBy'
      | 'reviews'
      | 'isDerivedFrom'
      | 'isSourceOf'
      | 'requires'
      | 'isRequiredBy'
      | 'isObsoletedBy'
      | 'obsoletes';
    resource_type?: string;
    [k: string]: unknown;
  }[];
  contributors?: {
    name: string;
    type:
      | 'ContactPerson'
      | 'DataCollector'
      | 'DataCurator'
      | 'DataManager'
      | 'Distributor'
      | 'Editor'
      | 'HostingInstitution'
      | 'Producer'
      | 'ProjectLeader'
      | 'ProjectManager'
      | 'ProjectMember'
      | 'RegistrationAgency'
      | 'RegistrationAuthority'
      | 'RelatedPerson'
      | 'Researcher'
      | 'ResearchGroup'
      | 'RightsHolder'
      | 'Supervisor'
      | 'Sponsor'
      | 'WorkPackageLeader'
      | 'Other';
    affiliation?: string;
    orcid?: string;
    [k: string]: unknown;
  }[];
  references?: string[];
  communities?: {
    identifier: string;
    [k: string]: unknown;
  }[];
  grants?: {
    id: string;
    [k: string]: unknown;
  }[];
  journal_title?: string;
  journal_volume?: string;
  journal_issue?: string;
  journal_pages?: string;
  conference_title?: string;
  conference_acronym?: string;
  conference_dates?: string;
  conference_place?: string;
  conference_url?: string;
  version?: string;
  /**
   * ISO 639-2 or 639-3 code
   */
  language?: string;
  method?: string;
  [k: string]: unknown;
}


// --- Manual Extensions & Citestyle Integration ---

import type { CslItem } from '@citestyle/types';
export type { CslItem };

/** Helper to ensure our mapping is type-safe */
export interface CitationMetadataState {
  version: string;
  csl: CslItem[];
}